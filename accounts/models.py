from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email adreses',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    city = models.ForeignKey('scraping.City', on_delete=models.SET_NULL,
                             null=True, blank=True)
    language = models.ForeignKey('scraping.Language', on_delete=models.SET_NULL,
                             null=True, blank=True)
    send_email = models.BooleanField(default=True)

    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin