from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, uid, password=None, is_admin=False, is_staff=False, is_active=True):
        if not uid:
            raise ValueError("User must have an uid")
        """if not password:
            raise ValueError("User must have a password")"""

        user = self.model(
            uid=uid
        )
        #user.full_name = full_name
        #user.set_password(password)  # change password to hash
        #user.profile_picture = profile_picture
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, uid, password=None, **extra_fields):
        if not uid:
            raise ValueError("User must have a uid")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            uid=uid
        )
        user.displayname = uid
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    uid_validator = UnicodeUsernameValidator()

    """ユーザー AbstractUserをコピペし編集"""
    uid = models.CharField(
        _('username'),
        primary_key=True,
        max_length=32,
        help_text=_(
            'Required. 32 characters or fewer. Letters, digits and @/./+/-/_ only.'
        ),
        validators=[uid_validator],
    )

    displayname = models.CharField(
        max_length=32,
        unique=False,
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the users can log into this admin site.'),
    )

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    photo_url = models.CharField(
        max_length=128,
        unique=False,
        null=True,
    )

    role = models.IntegerField(
        unique=False,
        null=True,
    )

    objects = UserManager()

    USERNAME_FIELD = 'uid'
    REQUIRED_FIELDS = ['password']

    class Meta:
        verbose_name = _('users')
        verbose_name_plural = _('users')

    # 既存メソッドの変更
    def get_full_name(self):
        return self.displayname
