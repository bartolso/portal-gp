# Generated by Django 4.2.3 on 2023-08-09 08:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("drgs", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="drg",
            name="locked",
            field=models.BooleanField(default=False),
        ),
    ]
