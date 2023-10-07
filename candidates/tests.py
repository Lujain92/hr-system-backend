from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Candidate
from django.core.files.uploadedfile import SimpleUploadedFile

class CandidateAPITests(TestCase):
    """
    Test cases for the Candidate API endpoints.
    """

    def setUp(self):
        """
        Set up the test client for making API requests.
        """
        self.client = APIClient()

    def create_candidate(self, full_name='Alice Smith', years_of_experience=8, department='HR'):
        """
        Helper method to create a candidate instance for testing.
        
        Args:
            full_name (str): Full name of the candidate.
            years_of_experience (int): Years of experience of the candidate.
            department (str): Department of the candidate.
        
        Returns:
            Candidate: The created Candidate instance.
        """
        resume_content = b'This is a sample resume content.'
        resume_file = SimpleUploadedFile("resume.pdf", resume_content, content_type="application/pdf")
        return Candidate.objects.create(
            full_name=full_name,
            date_of_birth='1985-03-15',
            years_of_experience=years_of_experience,
            department=department,
            resume=resume_file
        )
    
    def test_register_candidate(self):
        """
        Test case for registering a new candidate.
        """
        resume_content = b'This is a sample resume content.' 
        resume_file = SimpleUploadedFile("resume.pdf", resume_content, content_type="application/pdf")

        data = {
            'full_name': 'John Doe',
            'date_of_birth': '1990-01-01',
            'years_of_experience': 5,
            'department': 'IT',
            'resume': resume_file
        }
        response = self.client.post('/candidates/register/', data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Candidate.objects.count(), 1)

   
    def test_list_candidates(self):
        """
        Test case for listing candidates.
        """
        candidate= self.create_candidate()
        response = self.client.get('/candidates/list/',HTTP_X_ADMIN='1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['full_name'], 'Alice Smith')

    def test_download_resume(self):
        """
        Test case for downloading a candidate's resume.
        """

        candidate= self.create_candidate()
        response = self.client.get(f'/candidates/download/{candidate.id}/',HTTP_X_ADMIN='1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_download_resume_nonexistent_candidate(self):
        """
        Test case for attempting to download the resume of a nonexistent candidate.
        """

        candidate= self.create_candidate()
        response = self.client.get(f'/candidates/download/999/',HTTP_X_ADMIN='1')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
