from django.contrib import admin
from .models import Baby, GrowthLog, SleepLog, FeedingLog, Appointment, Milestone, Recipe, Vaccine, Vaccination

# --- Custom Admin Configurations ---

@admin.register(Vaccination)
class VaccinationAdmin(admin.ModelAdmin):
    """
    Custom admin view for Vaccination records.
    This view is configured to be read-only for administrators.
    """
    list_display = ('baby', 'vaccine', 'date_administered')
    list_filter = ('baby', 'vaccine')
    search_fields = ('baby__name', 'vaccine__name')
    
    def has_add_permission(self, request):
        # This is the key change: it removes the "+ Add" button for Vaccination records.
        return False

    def has_change_permission(self, request, obj=None):
        # Optional: You can make it fully read-only by also disabling changes.
        # For now, we'll allow changes to fix dates, but not additions.
        return True

# --- Standard Model Registrations ---

# These models are registered normally, allowing full CRUD operations in the admin panel.
admin.site.register(Baby)
admin.site.register(GrowthLog)
admin.site.register(SleepLog)
admin.site.register(FeedingLog)
admin.site.register(Appointment)
admin.site.register(Milestone)
admin.site.register(Recipe)
admin.site.register(Vaccine)

