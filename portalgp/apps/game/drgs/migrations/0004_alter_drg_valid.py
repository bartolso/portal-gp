# Generated by Django 4.2.3 on 2023-08-09 09:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("drgs", "0003_drg_locked"),
    ]

    operations = [
        migrations.AlterField(
            model_name="drg",
            name="valid",
            field=models.CharField(default="Sin revisar", max_length=20),
        ),
    ]