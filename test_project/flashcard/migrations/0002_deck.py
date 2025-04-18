# Generated by Django 4.2.9 on 2025-04-17 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flashcard", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Deck",
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
                ("name", models.CharField(max_length=100)),
                ("cards", models.ManyToManyField(to="flashcard.card")),
            ],
        ),
    ]
