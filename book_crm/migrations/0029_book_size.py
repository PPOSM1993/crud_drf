# Generated by Django 4.1.7 on 2023-08-16 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_crm", "0028_book_name_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="size",
            field=models.CharField(default=27, max_length=7, verbose_name="Size Book"),
            preserve_default=False,
        ),
    ]