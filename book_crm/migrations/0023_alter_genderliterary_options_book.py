# Generated by Django 4.1.7 on 2023-08-16 18:51

from django.db import migrations, models
import django.db.models.deletion
import isbn_field.fields
import isbn_field.validators


class Migration(migrations.Migration):

    dependencies = [
        ("book_crm", "0022_genderliterary"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="genderliterary",
            options={
                "ordering": ["id"],
                "verbose_name": "Name Gender Literary",
                "verbose_name_plural": "Name Genders Literary",
            },
        ),
        migrations.CreateModel(
            name="Book",
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
                    "isbn",
                    isbn_field.fields.ISBNField(
                        max_length=28,
                        validators=[isbn_field.validators.ISBNValidator],
                        verbose_name="ISBN",
                    ),
                ),
                (
                    "name_Book",
                    models.CharField(
                        max_length=255, null=True, verbose_name="Name Book"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="book_crm.category",
                        verbose_name="Category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Book",
                "verbose_name_plural": "Books",
                "ordering": ["id"],
            },
        ),
    ]
