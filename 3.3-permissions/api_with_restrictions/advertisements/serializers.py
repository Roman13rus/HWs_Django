from django.contrib.auth.models import User
import django.core.exceptions
import django.core.validators
from django.forms import ValidationError
from rest_framework import serializers

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)
   

    def validate(self, data):

        """Метод для валидации. Вызывается при создании и обновлении."""

        # TODO: добавьте требуемую валидацию

        creator_adv = self.context['request'].user.adv.filter(status='OPEN')
        if creator_adv.count() >= 10 and self.context['request'].method == 'POST':
            raise ValidationError("Открытых объявлений не может быть болше 10")
        elif self.context['request'].method == 'PATCH' and data['status'] == 'OPEN' and creator_adv.count() == 10:
            raise ValidationError("Открытых объявлений не может быть болше 10")
        elif self.context['request'].method == 'PATCH' and data['status'] == 'CLOSED':
            return data
        return data
