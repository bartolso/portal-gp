# Generated by Django 4.2.3 on 2023-08-15 09:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wimport", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="importrecord",
            name="gp_amount",
            field=models.IntegerField(),
        ),
    ]