from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# User-related Models
class Baby(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField(verbose_name="Date of Birth")
    GENDER_CHOICES = [('Boy', 'Boy'), ('Girl', 'Girl')]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name

class PersonalJournal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return f"Journal entry for {self.user.username} on {self.entry_date.strftime('%Y-%m-%d')}"

# Baby-specific Log Models
class GrowthLog(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, related_name='growth_logs')
    log_date = models.DateField()
    height_cm = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Height (cm)")
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)")

class SleepLog(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, related_name='sleep_logs')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def duration(self):
        if self.end_time and self.start_time:
            return self.end_time - self.start_time
        return None

class FeedingLog(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, related_name='feeding_logs')
    feeding_time = models.DateTimeField()
    # --- CORRECTED MODEL DEFINITION ---
    FEEDING_TYPE_CHOICES = [
        ('Breast Milk', 'Breast Milk'),
        ('Formula', 'Formula'),
        ('Solids', 'Solids'),
    ]
    feeding_type = models.CharField(max_length=20, choices=FEEDING_TYPE_CHOICES)
    amount_ml = models.PositiveIntegerField(verbose_name="Amount (ml)", blank=True, null=True)
    notes = models.TextField(blank=True) # Added the missing 'notes' field

class Appointment(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, related_name='appointments')
    doctor_name = models.CharField(max_length=100)
    appt_datetime = models.DateTimeField(verbose_name="Appointment Date & Time")
    purpose = models.TextField()

class Milestone(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, related_name='milestones')
    milestone_title = models.CharField(max_length=100)
    milestone_date = models.DateField()
    notes = models.TextField(blank=True)

# Informational Models (Managed by Admin)
class Recipe(models.Model):
    TARGET_AUDIENCE_CHOICES = [
        ('Baby', 'Baby'),
        ('Mother', 'Mother'),
    ]
    recipe_name = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    target_audience = models.CharField(max_length=10, choices=TARGET_AUDIENCE_CHOICES)

    def __str__(self):
        return self.recipe_name

# New model for the standard list of vaccines
class Vaccine(models.Model):
    name = models.CharField(max_length=100)
    recommended_age_weeks = models.IntegerField(help_text="Recommended age in weeks for the vaccination.")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} (at {self.recommended_age_weeks} weeks)"

# This model tracks which baby has received which vaccine
class Vaccination(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    date_administered = models.DateField()

    class Meta:
        # Ensures a baby can't have the same vaccine record twice
        unique_together = ('baby', 'vaccine')

    def __str__(self):
        return f"{self.baby.name} - {self.vaccine.name}"
