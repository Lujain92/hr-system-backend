from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    """
    Serializer for the Candidate model.

    Fields:
        id (int): The unique identifier for the candidate.
        full_name (str): The full name of the candidate.
        date_of_birth (date): The date of birth of the candidate.
        years_of_experience (int): The number of years of experience the candidate has.
        department (str): The department to which the candidate belongs (IT, HR, Finance).
        resume (File): The resume file uploaded by the candidate.
        registration_date (datetime): The date and time when the candidate registered.
    """
    class Meta:
        model = Candidate
        fields = '__all__'
