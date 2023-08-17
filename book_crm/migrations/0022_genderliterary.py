# Generated by Django 4.1.7 on 2023-08-16 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_crm", "0021_editorial"),
    ]

    operations = [
        migrations.CreateModel(
            name="GenderLiterary",
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
                ("name_gender", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name": "Name Gender",
                "verbose_name_plural": "Name Genders",
                "ordering": ["id"],
            },
        ),
    ]
