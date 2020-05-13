# -*- coding: utf-8 -*-
# Generated by Django 3.0.4 on 2020-03-16 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LetterData",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=500)),
                ("street_address", models.CharField(max_length=500)),
                ("district", models.CharField(max_length=500)),
                ("pin", models.CharField(blank=True, max_length=10, null=True)),
                ("province", models.CharField(max_length=500)),
                ("contact_person", models.CharField(max_length=200)),
                ("contact_number", models.IntegerField()),
                ("letter_subject", models.CharField(max_length=500)),
                ("letter_date", models.DateField(auto_now_add=True)),
                ("site", models.CharField(max_length=500)),
                ("date", models.DateField()),
                ("time", models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name="StaffInTeam",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                )
            ],
        ),
        migrations.CreateModel(
            name="TeamName",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("team_name", models.CharField(max_length=500)),
            ],
        ),
    ]