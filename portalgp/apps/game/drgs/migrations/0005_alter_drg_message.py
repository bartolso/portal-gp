# Generated by Django 4.2.3 on 2023-08-09 09:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("drgs", "0004_alter_drg_valid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="drg",
            name="message",
            field=models.CharField(max_length=20),
        ),
    ]