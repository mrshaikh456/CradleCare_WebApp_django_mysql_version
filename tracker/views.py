from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import (
    CustomUserCreationForm, BabyForm, GrowthLogForm, 
    SleepLogForm, FeedingLogForm, AppointmentForm, MilestoneForm,
    PersonalJournalForm
)
from .models import (
    Baby, GrowthLog, SleepLog, FeedingLog, Appointment, Milestone, Recipe,
    PersonalJournal, Vaccine, Vaccination
)

# --- AUTHENTICATION VIEWS ---
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Welcome back, {username}!")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to CradleCare.')
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('login')


# --- CORE VIEWS ---
@login_required
def dashboard(request):
    babies = Baby.objects.filter(user=request.user)
    return render(request, 'tracker/dashboard.html', {'babies': babies})

@login_required
def add_baby(request):
    if request.method == 'POST':
        form = BabyForm(request.POST)
        if form.is_valid():
            baby = form.save(commit=False)
            baby.user = request.user
            baby.save()
            messages.success(request, f'Profile for {baby.name} has been created.')
            return redirect('dashboard')
    else:
        form = BabyForm()
    return render(request, 'tracker/add_baby.html', {'form': form})

@login_required
def baby_detail(request, baby_id):
    baby = get_object_or_404(Baby, id=baby_id, user=request.user)
    return render(request, 'tracker/baby_detail.html', {'baby': baby})


# --- TRACKER VIEWS ---
@login_required
def growth_tracker(request, baby_id):
    baby = get_object_or_404(Baby, id=baby_id, user=request.user)
    
    if request.method == 'POST':
        form = GrowthLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.baby = baby
            log.save()
            messages.success(request, 'Growth log has been added successfully.')
            return redirect('growth_tracker', baby_id=baby.id)
    else:
        form = GrowthLogForm()

    logs = GrowthLog.objects.filter(baby=baby).order_by('-log_date')
    
    context = {'baby': baby, 'form': form, 'logs': logs}
    return render(request, 'tracker/growth_tracker.html', context)

@login_required
def sleep_tracker(request, baby_id):
    baby = get_object_or_404(Baby, id=baby_id, user=request.user)
    
    if request.method == 'POST':
        form = SleepLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.baby = baby
            log.save()
            messages.success(request, 'Sleep session has been added successfully.')
            return redirect('sleep_tracker', baby_id=baby.id)
    else:
        form = SleepLogForm()

    logs = SleepLog.objects.filter(baby=baby).order_by('-start_time')
    
    context = {'baby': baby, 'form': form, 'logs': logs}
    return render(request, 'tracker/sleep_tracker.html', context)

@login_required
def feeding_tracker(request, baby_id):
    baby = get_object_or_404(Baby, id=baby_id, user=request.user)
    
    if request.method == 'POST':
        form = FeedingLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.baby = baby
            log.save()
            messages.success(request, 'Feeding log has been added successfully.')
            return redirect('feeding_tracker', baby_id=baby.id)
    else:
        form = FeedingLogForm()

    logs = FeedingLog.objects.filter(baby=baby).order_by('-feeding_time')
    
    context = {'baby': baby, 'form': form, 'logs': logs}
    return render(request, 'tracker/feeding_tracker.html', context)
    

# --- SECONDARY & ADVANCED FEATURES ---

@login_required
def appointment_tracker(request, baby_id):
    baby = get_object_or_404(Baby, id=baby_id, user=request.user)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.baby = baby
            log.save()
            messages.success(request, 'Appointment has been scheduled successfully.')
            return redirect('appointment_tracker', baby_id=baby.id)
    else:
        form = AppointmentForm()

    appointments = Appointment.objects.filter(baby=baby).order_by('-appt_datetime')
    
    context = {'baby': baby, 'form': form, 'appointments': appointments}
    return render(request, 'tracker/appointment_tracker.html', context)

@login_required
def milestone_tracker(request, baby_id):
    baby = get_object_or_404(Baby, id=baby_id, user=request.user)
    
    if request.method == 'POST':
        form = MilestoneForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.baby = baby
            log.save()
            messages.success(request, 'Milestone has been recorded successfully.')
            return redirect('milestone_tracker', baby_id=baby.id)
    else:
        form = MilestoneForm()

    milestones = Milestone.objects.filter(baby=baby).order_by('-milestone_date')
    
    context = {'baby': baby, 'form': form, 'milestones': milestones}
    return render(request, 'tracker/milestone_tracker.html', context)

@login_required
def recipe_book(request):
    mother_recipes = Recipe.objects.filter(target_audience='Mother')
    baby_recipes = Recipe.objects.filter(target_audience='Baby')
    
    context = {
        'mother_recipes': mother_recipes,
        'baby_recipes': baby_recipes,
    }
    return render(request, 'tracker/recipes.html', context)

@login_required
def personal_journal(request):
    if request.method == 'POST':
        form = PersonalJournalForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            messages.success(request, 'Your journal entry has been saved.')
            return redirect('personal_journal')
    else:
        form = PersonalJournalForm()

    entries = PersonalJournal.objects.filter(user=request.user).order_by('-entry_date')

    context = {
        'form': form,
        'entries': entries
    }
    return render(request, 'tracker/personal_journal.html', context)

@login_required
def vaccination_schedule(request, baby_id):
    baby = get_object_or_404(Baby, id=baby_id, user=request.user)
    
    # --- THIS IS THE FIX ---
    # We now get the vaccine_id directly from the request, bypassing the form.
    if request.method == 'POST':
        vaccine_id = request.POST.get('vaccine_id')
        if vaccine_id:
            vaccine_to_mark = get_object_or_404(Vaccine, id=vaccine_id)
            
            # Use the provided date or default to today
            date_administered = request.POST.get('date_administered') or timezone.now().date()

            Vaccination.objects.update_or_create(
                baby=baby, 
                vaccine=vaccine_to_mark,
                defaults={'date_administered': date_administered}
            )
            messages.success(request, f"{vaccine_to_mark.name} has been marked as complete.")
        
        # Redirect after processing to prevent form resubmission issues
        return redirect('vaccination_schedule', baby_id=baby.id)

    # --- Prepare the schedule for display (this logic remains the same) ---
    standard_vaccines = Vaccine.objects.all().order_by('recommended_age_weeks')
    completed_vaccinations = Vaccination.objects.filter(baby=baby, date_administered__isnull=False).values_list('vaccine_id', flat=True)
    
    today = timezone.now().date()
    schedule = []

    for vaccine in standard_vaccines:
        due_date = baby.dob + timedelta(weeks=vaccine.recommended_age_weeks)
        status = ''

        if vaccine.id in completed_vaccinations:
            status = 'Done'
        elif today >= due_date:
            status = 'Due'
        elif today >= due_date - timedelta(weeks=2):
            status = 'Due Soon'
        else:
            status = 'Pending'
        
        item = {
            'vaccine': vaccine,
            'due_date': due_date,
            'status': status,
        }
        schedule.append(item)

    context = {
        'baby': baby,
        'schedule': schedule,
        'today': today,
    }
    return render(request, 'tracker/vaccination_schedule.html', context)

# --- DELETE VIEWS ---

@login_required
def delete_growth_log(request, log_id):
    log_to_delete = get_object_or_404(GrowthLog, id=log_id, baby__user=request.user)
    baby_id = log_to_delete.baby.id

    if request.method == 'POST':
        log_to_delete.delete()
        messages.success(request, 'The growth log has been deleted successfully.')
        return redirect('growth_tracker', baby_id=baby_id)

    context = {
        'item': log_to_delete,
        'item_type': 'Growth Log',
        'cancel_url': request.META.get('HTTP_REFERER', '/'),
    }
    return render(request, 'delete_confirm.html', context)

@login_required
def delete_sleep_log(request, log_id):
    log_to_delete = get_object_or_404(SleepLog, id=log_id, baby__user=request.user)
    baby_id = log_to_delete.baby.id

    if request.method == 'POST':
        log_to_delete.delete()
        messages.success(request, 'The sleep session has been deleted successfully.')
        return redirect('sleep_tracker', baby_id=baby_id)

    context = {
        'item': log_to_delete,
        'item_type': 'Sleep Session',
        'cancel_url': request.META.get('HTTP_REFERER', '/'),
    }
    return render(request, 'delete_confirm.html', context)

@login_required
def delete_feeding_log(request, log_id):
    log_to_delete = get_object_or_404(FeedingLog, id=log_id, baby__user=request.user)
    baby_id = log_to_delete.baby.id

    if request.method == 'POST':
        log_to_delete.delete()
        messages.success(request, 'The feeding log has been deleted successfully.')
        return redirect('feeding_tracker', baby_id=baby_id)

    context = {
        'item': log_to_delete,
        'item_type': 'Feeding Log',
        'cancel_url': request.META.get('HTTP_REFERER', '/'),
    }
    return render(request, 'delete_confirm.html', context)

@login_required
def delete_appointment(request, log_id):
    log_to_delete = get_object_or_404(Appointment, id=log_id, baby__user=request.user)
    baby_id = log_to_delete.baby.id

    if request.method == 'POST':
        log_to_delete.delete()
        messages.success(request, 'The appointment has been deleted successfully.')
        return redirect('appointment_tracker', baby_id=baby_id)

    context = {
        'item': log_to_delete,
        'item_type': 'Appointment',
        'cancel_url': request.META.get('HTTP_REFERER', '/'),
    }
    return render(request, 'delete_confirm.html', context)

@login_required
def delete_milestone(request, log_id):
    log_to_delete = get_object_or_404(Milestone, id=log_id, baby__user=request.user)
    baby_id = log_to_delete.baby.id

    if request.method == 'POST':
        log_to_delete.delete()
        messages.success(request, 'The milestone has been deleted successfully.')
        return redirect('milestone_tracker', baby_id=baby_id)

    context = {
        'item': log_to_delete,
        'item_type': 'Milestone',
        'cancel_url': request.META.get('HTTP_REFERER', '/'),
    }
    return render(request, 'delete_confirm.html', context)