# Generated by Django 4.1 on 2022-11-10 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("first_app", "0006_plain"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog_Site",
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
                ("image", models.ImageField(upload_to="upload/images")),
                ("content", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
        ),
    ]
