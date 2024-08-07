from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from users.models import User

user = get_object_or_404(User)
content_type = ContentType.objects.get_for_model(User)
# получить запись о необходимых правах доступа
permission = Permission.objects.get(
    codename="change_description",
    content_type=content_type,
)
# и установить права для пользователя
user.user_permissions.add(permission)