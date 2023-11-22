
from django.test import TestCase
from django.contrib.auth.models import User
from users.models import Profile
from users.signals import updateUser

class ProfileSignalTest(TestCase):
    def test_profile_creation_signal(self):
        # Create a new user
        user = User.objects.create(
            username='testuser', 
            email='test@example.com', 
            first_name='John')

        # Retrieve the profile associated with the user
        profile = Profile.objects.get(user=user)

        # Check if the profile was created successfully
        self.assertIsNotNone(profile)
        self.assertEqual(profile.user, user)
        self.assertEqual(profile.username, user.username)
        self.assertEqual(profile.email, user.email)
        self.assertEqual(profile.name, user.first_name)

    def test_profile_deletion_signal(self):
        # Create a new user
        user = User.objects.create(
            username='testuser',
            email='test@example.com', 
            first_name='John')

        # Retrieve the profile associated with the user
        profile = Profile.objects.get(user=user)

        # Delete the profile
        profile.delete()

        # Check if the user associated with the profile is deleted
        user_exists = User.objects.filter(username='testuser').exists()
        self.assertFalse(user_exists)



    def test_update_user_signal(self):
        # Create a new user
        user = User.objects.create(
            username='testuser', 
            email='test@example.com', 
            first_name='John')

        # Retrieve the profile associated with the user
        profile = Profile.objects.get(user=user)

        # Update the user information
        profile.name = 'Updated Name'
        profile.username = 'updatedusername'
        profile.email = 'updated@example.com'
        profile.save()

        # Refresh the user instance from the database
        updated_user = User.objects.get(pk=user.pk)

        # Check if the user fields have been updated
        self.assertEqual(updated_user.first_name, profile.name)
        self.assertEqual(updated_user.username, profile.username)
        self.assertEqual(updated_user.email, profile.email)

