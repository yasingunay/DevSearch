# Generated by Django 4.2.7 on 2023-11-20 13:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_profile_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_image",
            field=models.ImageField(
                blank=True,
                default="static/images/profiles/user-default.png",
                null=True,
                upload_to="profiles/",
            ),
        ),
    ]
