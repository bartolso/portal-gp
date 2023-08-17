# Generated by Django 4.2.3 on 2023-07-18 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("drgs", "0001_initial"),
        ("mbds", "0001_initial"),
        ("persons", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="drg",
            name="mbd",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="drg_relation",
                to="mbds.mbd",
            ),
        ),
        migrations.AddField(
            model_name="drg",
            name="person",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="persons.person",
            ),
        ),
    ]