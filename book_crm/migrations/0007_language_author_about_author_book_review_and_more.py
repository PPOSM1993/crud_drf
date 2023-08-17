# Generated by Django 4.1.7 on 2023-08-11 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_crm", "0006_book_name_gender"),
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
        ),
        migrations.AddField(
            model_name="author",
            name="about_author",
            field=models.CharField(
                blank=True, max_length=2000, null=True, verbose_name="About Author"
            ),
        ),
        migrations.AddField(
            model_name="book",
            name="review",
            field=models.CharField(max_length=255, null=True, verbose_name="Review"),
        ),
        migrations.AlterField(
            model_name="author",
            name="name_author",
            field=models.CharField(max_length=255, verbose_name="Name Author"),
        ),
    ]
