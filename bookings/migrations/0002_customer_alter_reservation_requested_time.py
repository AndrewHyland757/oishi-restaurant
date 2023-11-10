# Generated by Django 4.2.7 on 2023-11-10 07:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bookings", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.IntegerField()),
                ("password", models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name="reservation",
            name="requested_time",
            field=models.CharField(
                choices=[
                    ("12:00", "12:00"),
                    ("12:30", "12:30"),
                    ("01:00", "01:00"),
                    ("01:30", "01:30"),
                    ("02:00", "02:00"),
                    ("02:30", "02:30"),
                    ("03:00", "03:00"),
                    ("18:00", "18:00"),
                    ("18:30", "18:30"),
                    ("19:00", "19:00"),
                    ("20:30", "20:30"),
                    ("21:00", "21:00"),
                ],
                default="12:00",
                max_length=10,
            ),
        ),
    ]