from django.db import models
from django.conf import settings

from django.contrib.auth import models as auth_models

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserManager(auth_models.BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False, is_owner=False):
        if not email:
            raise ValueError("Users must have an email address!")

        if not password:
            raise ValueError("Users must have a password!")

        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.project_owner = is_owner
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        """
        A method to create a staff user.
        """
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        """
        A method to create the super user
        """
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True,
            is_owner=True
        )
        return user


class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    """
    Custom user model for the project.
    Uses the email as the identifier intead of the default username.
    """
    email = models.EmailField(db_index=True, verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    project_owner = models.BooleanField(default=False)  # The owner of the project. Has super user permissions
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.first_name and self.last_name:
            full_name = '%s %s' % (self.first_name, self.last_name)
            return full_name.strip()

        elif self.first_name:
            full_name = '%s' % (self.first_name)
            return full_name.strip()

        elif self.last_name:
            full_name = '%s' % (self.last_name)
            return full_name.strip()

        else:
            return self.get_short_name()

    def get_short_name(self):
        # The user is identified by their email
        return self.email

    def has_perm(self, perm, obj=None):
        # Does the user have a specific permission?
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_owner(self):
        return self.project_owner
