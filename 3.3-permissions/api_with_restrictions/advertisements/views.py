from advertisements.permissions import IsDelOrReadOnly
from advertisements.filters import AdvertisementFilter
from advertisements.serializers import AdvertisementSerializer
from advertisements.models import Advertisement
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_class = AdvertisementFilter

    
    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsDelOrReadOnly()]
        return []
