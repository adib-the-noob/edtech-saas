from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    def create_user(self, phone_number, full_name, password, **other_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """

        user = self.model(
            phone_number=phone_number,
            full_name=full_name,
            is_active=True,
            **other_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")

        superUser = self.model(phone_number=phone_number, **other_fields)
        superUser.set_password(password)
        superUser.save()
        return superUser


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(
        verbose_name="email address", max_length=255, unique=True, blank=True, null=True
    )
    profile_picture = models.ImageField(
        upload_to="profile_picture",
        blank=True,
        null=True,
    )

    is_verified = models.BooleanField(default=False)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "phone_number"

    def __str__(self):
        return f"{self.pk} - {self.full_name}"

    def save(self, *args, **kwargs):
        try:
            super(User, self).save(*args, **kwargs)
            old_instance = User.objects.get(pk=self.pk).profile_picture
            if old_instance != self.profile_picture:
                old_instance.delete(save=False)

        except:
            pass

class Otp(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otp')
    otp = models.IntegerField()
    has_used = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user.full_name} - {self.otp}"
    
