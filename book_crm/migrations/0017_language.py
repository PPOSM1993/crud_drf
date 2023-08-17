# Generated by Django 4.1.7 on 2023-08-16 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_crm", "0016_delete_binding_remove_book_category_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Language",
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
                    "language",
                    models.CharField(
                        blank=True, max_length=200, verbose_name="Language"
                    ),
                ),
            ],
            options={
                "verbose_name": "Language",
                "verbose_name_plural": "Languages",
                "ordering": ["id"],
            },
        ),
    ]
