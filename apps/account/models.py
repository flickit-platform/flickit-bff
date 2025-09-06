from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from common.validators import validate_file_size

from uuid import uuid4


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, display_name, **extra_fields):
        if not email:
            raise ValueError('Email must be provided')

        user = self.model(
            email=self.normalize_email(email),
            display_name=display_name,
            **extra_fields
        )

        if password is None:
            user.set_unusable_password()

        user.save(using=self._db)
        return user

    def create_user(self, email, password, display_name, **extra_fields):
        return self._create_user(email, password, display_name, **extra_fields)

    def create_superuser(self, email, password, display_name, **extra_fields):
        return self._create_user(email, password, display_name, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid4)
    email = models.EmailField(unique=True, max_length=254,
                              error_messages={'unique': "A user with this email address already exists."})
    display_name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='user/images', null=True, validators=[validate_file_size])
    bio = models.CharField(null=True, max_length=400)
    linkedin = models.URLField(null=True, blank=True)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['display_name']

    @property
    def is_superuser(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_staff(self):
        return True

    class Meta:
        db_table = 'fau_user'
