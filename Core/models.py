

from django.db import models

class JournalEntry(models.Model):
    student_name = models.CharField(max_length=100)
    student_id_no = models.CharField(max_length=10)
    internship_supervisor = models.CharField(max_length=100)
    host_organisation_supervisor = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    internship_host_organisation = models.CharField(max_length=100)
    internship_job_title = models.CharField(max_length=100)
    job_description = models.TextField(max_length=500)
    job_responsibilities = models.TextField(max_length=500)
    date = models.DateField()
    monday_hours = models.PositiveIntegerField()
    tuesday_hours = models.PositiveIntegerField()
    wednesday_hours = models.PositiveIntegerField()
    thursday_hours = models.PositiveIntegerField()
    friday_hours = models.PositiveIntegerField()
    weekly_hours = models.PositiveIntegerField()
    total_hours = models.PositiveIntegerField()
    take_away = models.TextField(max_length=500)
    new_learning = models.TextField(max_length=500)
    interesting_points = models.TextField(max_length=500)
    comments = models.TextField(max_length=500)
    areas_for_clarity = models.TextField(max_length=500)
    future_use = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    