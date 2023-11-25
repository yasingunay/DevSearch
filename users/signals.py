from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings



@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    """
    This function will be called after a YourModel instance is saved.

    Args:
        sender: The model class.
        instance: The actual instance being saved.
        created: A boolean; True if a new record was created.
    """
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

        subject = "Welcome to the DevSearch"
        message = "We are glad you are here!"

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
            # fail_silently: If set to True, errors during the email-sending process will be logged but not raised as exceptions. 
            # If set to False (the default), exceptions will be raised if there are errors.
        )


# post_save.connect(profileUpdated, sender=Profile)


def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.username = profile.username
        if profile.email and profile.name:
            user.first_name = profile.name
            user.email = profile.email
        user.save()


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    if user is not None:
        user.delete()


post_delete.connect(deleteUser, sender=Profile)
post_save.connect(updateUser, sender=Profile)
