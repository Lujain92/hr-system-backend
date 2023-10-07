from django.contrib import admin
from .models import Candidate

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'date_of_birth', 'years_of_experience', 'department')
    search_fields = ('full_name', 'department')
    list_filter = ('department', 'registration_date')

admin.site.register(Candidate, CandidateAdmin)
