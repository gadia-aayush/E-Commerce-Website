from donation_form.models import Donationreqs
from rest_framework import viewsets,permissions
from .serializers import DonationRquestsSerializers

#Donation_Request Viewset
class DonationRequestViewSet(viewsets.ModelViewSet):
    queryset = Donationreqs.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DonationRquestsSerializers