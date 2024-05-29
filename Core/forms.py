from django.forms import ModelForm
from Core.models import JournalEntry
from django import forms

class JournalEntryForm(ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = JournalEntry
        fields = ['student_name', 'student_id_no', 'internship_supervisor', 'host_organisation_supervisor',
                  'start_date', 'end_date', 'internship_host_organisation', 'internship_job_title',
                  'job_description', 'job_responsibilities', 'date', 'monday_hours', 'tuesday_hours',
                  'wednesday_hours', 'thursday_hours', 'friday_hours', 'weekly_hours', 'total_hours',
                  'take_away', 'new_learning', 'interesting_points', 'comments', 'areas_for_clarity',
                  'future_use']
