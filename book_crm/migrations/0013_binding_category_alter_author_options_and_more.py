# Generated by Django 4.1.7 on 2023-08-11 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("book_crm", "0012_book_language_book_size"),
    ]

    operations = [
        migrations.CreateModel(
            name="Binding",
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
                ("binding", models.CharField(max_length=200, verbose_name="Binding")),
            ],
            options={
                "verbose_name": "Binding",
                "verbose_name_plural": "Bindings",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Category",
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
                    "category",
                    models.CharField(
                        blank=True, max_length=200, verbose_name="Category"
                    ),
                ),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
                "ordering": ["id"],
            },
        ),
        migrations.AlterModelOptions(
            name="author",
            options={
                "ordering": ["id"],
                "verbose_name": "Author",
                "verbose_name_plural": "Authors",
            },
        ),
        migrations.AlterModelOptions(
            name="formatbook",
            options={
                "ordering": ["id"],
                "verbose_name": "Format",
                "verbose_name_plural": "Formats",
            },
        ),
        migrations.AlterModelOptions(
            name="genderliterary",
            options={
                "ordering": ["id"],
                "verbose_name": "Name Gender",
                "verbose_name_plural": "Name Genders",
            },
        ),
        migrations.AlterModelOptions(
            name="language",
            options={
                "ordering": ["id"],
                "verbose_name": "Language",
                "verbose_name_plural": "Languages",
            },
        ),
        migrations.AlterField(
            model_name="book",
            name="name_gender",
            field=models.ForeignKey(
                default=12,
                on_delete=django.db.models.deletion.PROTECT,
                to="book_crm.genderliterary",
                verbose_name="Gender Literary",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="book",
            name="size",
            field=models.CharField(default=11, max_length=7, verbose_name="Size Book"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="book",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="book_crm.category",
                verbose_name="Language",
            ),
        ),
    ]
