import django_filters

from app.models import SAP


class SAPFilter(django_filters.FilterSet):
    class Meta:
        model = SAP
        fields = ('name', 'count', 'distance')
