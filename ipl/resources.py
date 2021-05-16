from import_export import resources
from ipl_app.models import matches, deliveries


class MatchResources(resources.ModelResource):
    class Meta:
        model = matches


class DeliveryResources(resources.ModelResource):
    class Meta:
        model = deliveries
