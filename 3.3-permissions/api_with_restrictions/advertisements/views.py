from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.db.models import Q

from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsOwnerOrAdmin
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement, Favorite
from .serializers import AdvertisementSerializer

from django_filters.rest_framework import DjangoFilterBackend
from .filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        
        if user.is_authenticated:
            return queryset.filter(
                Q(status__in=['OPEN', 'CLOSED']) |
                Q(status='DRAFT', creator=user)
            )
            
        return queryset.filter(status__in=['OPEN', 'CLOSED'])

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        if self.action in ['create', 'favorite']:
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsOwnerOrAdmin()]
    
    @action(detail=True, methods=['post', 'delete'])
    def favorite(self, request, pk=None):
        advertisement = self.get_object()
        
        if advertisement.creator == request.user:
            return Response(
                {'error': 'Нельзя добавить свое объявление в избранное'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if request.method == 'POST':
            favorite, created = Favorite.objects.get_or_create(
                user=request.user,
                advertisement=advertisement
            )
            
            if not created:
                return Response(
                    {'error': 'Уже в избранном'},
                    status=status.HTTP_400_BAD_REQUEST
                )
                
            return Response(
                {'status': 'added'},
                status=status.HTTP_201_CREATED
            )
        
        if request.method == 'DELETE':
            deleted, _ = Favorite.objects.filter(
                user=request.user,
                advertisement=advertisement
            ).delete()
            
            if not deleted:
                return Response(
                    {'error': 'Не в избранном'},
                    status=status.HTTP_404_NOT_FOUND
                )
                
            return Response(
                {'status': 'removed'},
                status=status.HTTP_204_NO_CONTENT
            )
    
   
