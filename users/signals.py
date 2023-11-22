from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from.models import Profile


@receiver(post_save, sender = User)
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
        print("Signal: User created. Creating profile...")
        profile = Profile.objects.create(
            user= user,
            username = user.username,
            email = user.email,
            name = user.first_name,
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
    user.delete()


post_delete.connect(deleteUser, sender=Profile)
post_save.connect(updateUser, sender=Profile)

