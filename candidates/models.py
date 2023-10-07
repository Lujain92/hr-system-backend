from django.db import models

class Candidate(models.Model):
    """
    Model representing a job candidate.

    Attributes:
        full_name (str): The full name of the candidate.
        date_of_birth (date): The date of birth of the candidate.
        years_of_experience (int): The number of years of experience the candidate has.
        department (str): The department to which the candidate belongs (IT, HR, Finance).
        resume (File): The resume file uploaded by the candidate.
        registration_date (datetime): The date and time when the candidate registered.
    """
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    years_of_experience = models.IntegerField()
    DEPARTMENT_CHOICES = (
        ('IT', 'IT'),
        ('HR', 'HR'),
        ('Finance', 'Finance'),
    )
    department = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES)
    resume = models.FileField(upload_to='resumes/')
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
