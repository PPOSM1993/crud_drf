# Generated by Django 4.1.7 on 2023-08-16 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_crm", "0019_formatbook"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
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
                (
                    "name_author",
                    models.CharField(max_length=255, verbose_name="Name Author"),
                ),
                (
                    "about_author",
                    models.TextField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="About Author",
                    ),
                ),
            ],
            options={
                "verbose_name": "Author",
                "verbose_name_plural": "Authors",
                "ordering": ["id"],
            },
        ),
    ]
