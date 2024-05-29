from django.shortcuts import render, redirect
from django.contrib import messages
from .models import JournalEntry
from Core.forms import JournalEntryForm
from django.shortcuts import get_object_or_404

def home(request):
    journal_entries = JournalEntry.objects.all()
    print(journal_entries)  # Add this line for debugging
    return render(request, 'home.html', {'journalentry_list': journal_entries})

def journal_entry(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('journalentry_list')
    else:
        form = JournalEntryForm()
    
    entries = JournalEntry.objects.all()
    
    return render(request, 'journalentry.html', {'form': form, 'entries': entries})
def edit_journal_entry(request, pk):
    entry = JournalEntry.objects.get(pk=pk)
    if request.method == 'POST':
        form = JournalEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Journal entry has been updated.')
            return redirect('home')  # Redirect to the home page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = JournalEntryForm(instance=entry)
    return render(request, 'journalentry_edit.html', {'form': form})

def journalentry_detail(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk)
    return render(request, 'journalentry_detail.html', {'entry': entry})

def list_journal_entries(request):
    entries = JournalEntry.objects.all()
    return render(request, 'journalentry_list.html', {'entries': entries})