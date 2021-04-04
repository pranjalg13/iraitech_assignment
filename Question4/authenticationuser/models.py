from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models

class Account(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    phone_no = models.CharField(max_length= 10)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 
    # Email & Password are required by default in required
    # Phone_no is not given as required

    # The user, identify by email
    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    # For specific permission
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    # For checking user is staff or admin
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
