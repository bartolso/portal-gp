# Generated by Django 4.2.3 on 2023-08-09 08:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gps", "0002_alter_gp_gpv_alter_gp_message"),
    ]

    operations = [
        migrations.AddField(
            model_name="gp",
            name="locked",
            field=models.BooleanField(default=False),
        ),
    ]