from rest_framework import viewsets
from stocks.serializers import ServicesSerializer, UserServiceSerializer, UserSerializer
from stocks.models import Services, UserService, User


class ServicesViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Services.objects.all().order_by('name')
    serializer_class = ServicesSerializer  # Сериализатор для модели


class UserServicesViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = UserService.objects.all().order_by('order_date')
    serializer_class = UserServiceSerializer  # Сериализатор для модели


class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint, который позволяет просматривать и редактировать акции компаний
        """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = User.objects.all().order_by('user_name')
    serializer_class = UserSerializer  # Сериализатор для модели
