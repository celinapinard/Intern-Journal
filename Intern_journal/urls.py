from django.contrib import admin
from django.urls import path
from Core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('journalentry/', views.journal_entry, name='journalentry'),
    path('journalentry/edit/<int:pk>/', views.edit_journal_entry, name='journalentry_edit'),
    path('journalentry/<int:pk>/', views.journalentry_detail, name='journalentry_detail'),
    path('journalentry_list/', views.list_journal_entries, name='journalentry_list'),
]
