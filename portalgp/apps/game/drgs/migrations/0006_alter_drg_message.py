# Generated by Django 4.2.3 on 2023-08-09 09:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("drgs", "0005_alter_drg_message"),
    ]

    operations = [
        migrations.AlterField(
            model_name="drg",
            name="message",
            field=models.CharField(max_length=200),
        ),
    ]
