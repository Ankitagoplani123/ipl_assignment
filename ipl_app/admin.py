from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from ipl_app.models import matches, deliveries, temp_model


@admin.register(matches)
class MatchAdmin(ImportExportModelAdmin):
    pass


@admin.register(deliveries)
class DeliveryAdmin(ImportExportModelAdmin):
    pass


admin.site.register(temp_model)
