# Generated by Django 4.2.7 on 2023-11-25 19:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0007_message"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profile",
            options={"ordering": ["created"]},
        ),
    ]
