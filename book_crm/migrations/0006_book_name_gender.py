# Generated by Django 4.1.7 on 2023-08-11 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("book_crm", "0005_alter_book_name_book"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="name_gender",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="book_crm.gender_literary",
                verbose_name="Gender Literary",
            ),
        ),
    ]
