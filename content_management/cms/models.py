from django.db import models
# from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import Group,AbstractUser
from django.utils.translation import ugettext_lazy as _



class User(AbstractUser):
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, default=2)
    username = models.CharField(blank=True, null=True,max_length=10)
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','groups_id']
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.BigIntegerField(null=False)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True) 
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    pincode = models.IntegerField(null=False)


#This signal create Auth Token for users 
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs ):
    if created:
        Token.objects.create(user=instance)