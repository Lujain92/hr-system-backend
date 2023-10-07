from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from .models import Candidate
from .serializers import CandidateSerializer
import os

@api_view(['POST'])
def register_candidate(request):
    """
    API endpoint to register a new candidate.

    Args:
        request (HttpRequest): The HTTP request object containing candidate data in the request body.

    Returns:
        Response: JSON response indicating the success or failure of the registration process.
    """
    serializer = CandidateSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def list_candidates(request):
    """
    API endpoint to list all candidates (accessible to admin users only).

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        Response: JSON response containing a list of candidate data.
    """
    if 'X-ADMIN' in request.headers and request.headers['X-ADMIN'] == '1':
        candidates = Candidate.objects.all().order_by('-registration_date')
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'Permission denied.'}, status=403)

@api_view(['GET'])
def download_resume(request, candidate_id):
    """
    API endpoint to download a candidate's resume file (accessible to admin users only).

    Args:
        request (HttpRequest): The HTTP request object.
        candidate_id (int): The ID of the candidate whose resume needs to be downloaded.

    Returns:
        Response: FileResponse containing the candidate's resume file for download.
    """
    if 'X-ADMIN' in request.headers and request.headers['X-ADMIN'] == '1':
        candidate = get_object_or_404(Candidate, id=candidate_id)
        
        if os.path.exists(candidate.resume.path):
            resume_file = open(candidate.resume.path, 'rb')
            response = FileResponse(resume_file)
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(candidate.resume.path)}"'
            return response
        else:
            return Response({'error': 'Resume file not found.'}, status=404)
    else:
        return Response({'error': 'Permission denied.'}, status=403)