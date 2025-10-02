from django import forms
from django.contrib.auth.forms import UserCreationForm
# --- Import PersonalJournal model ---
from .models import (
    Baby, GrowthLog, SleepLog, FeedingLog, Appointment, Milestone, Recipe,
    PersonalJournal, Vaccination
)

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class BabyForm(forms.ModelForm):
    class Meta:
        model = Baby
        fields = ['name', 'dob', 'gender']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

class GrowthLogForm(forms.ModelForm):
    class Meta:
        model = GrowthLog
        fields = ['log_date', 'height_cm', 'weight_kg']
        widgets = {
            'log_date': forms.DateInput(attrs={'type': 'date'}),
        }

class SleepLogForm(forms.ModelForm):
    class Meta:
        model = SleepLog
        fields = ['start_time', 'end_time']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class FeedingLogForm(forms.ModelForm):
    class Meta:
        model = FeedingLog
        # --- CORRECTED FIELD NAME HERE ---
        fields = ['feeding_time', 'feeding_type', 'amount_ml', 'notes']
        widgets = {
            'feeding_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor_name', 'appt_datetime', 'purpose']
        widgets = {
            'appt_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'purpose': forms.Textarea(attrs={'rows': 3}),
        }

class MilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = ['milestone_title', 'milestone_date', 'notes']
        widgets = {
            'milestone_date': forms.DateInput(attrs={'type': 'date'}),
        }

# --- NEW FORM ---
class PersonalJournalForm(forms.ModelForm):
    class Meta:
        model = PersonalJournal
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }

# New form to mark a vaccine as administered
class VaccinationUpdateForm(forms.ModelForm):
    date_administered = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Vaccination
        fields = ['date_administered']
