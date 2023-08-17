# Generated by Django 4.2.3 on 2023-07-18 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("drgs", "0001_initial"),
        ("persons", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MBD",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("message", models.CharField(max_length=1000, null=True)),
                ("valid", models.CharField(max_length=2)),
                ("comment", models.CharField(max_length=1000, null=True)),
                (
                    "drg",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="mbd_relation",
                        to="drgs.drg",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="persons.person",
                    ),
                ),
            ],
        ),
    ]
