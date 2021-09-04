from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("must have email")
        if not password:
            raise ValueError("must have user password")
        user = self.model(
            email = email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser): 
    kakao_id    = models.BigIntegerField(null=True)
    name        = models.CharField(max_length=200, null=True)
    profile_url = models.CharField(max_length=2000, null=True)
    email       = models.EmailField(unique=True)
    password    = models.CharField(max_length=200, null=True)

    USERNAME_FIELD = 'email'    
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta: 
        db_table = 'users'