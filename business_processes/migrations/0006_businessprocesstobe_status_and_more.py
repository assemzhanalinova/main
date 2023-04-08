# Generated by Django 4.1.7 on 2023-03-27 23:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "business_processes",
            "0005_rename_business_process_businessprocesstobe_business_process_as_is",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="businessprocesstobe",
            name="status",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (1, "Draft"),
                    (2, "Review"),
                    (3, "Approved"),
                    (4, "Canceled"),
                ],
                default=1,
                verbose_name="Status",
            ),
        ),
        migrations.AlterField(
            model_name="businessprocessasis",
            name="status",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "Draft"), (2, "Active"), (3, "Competed")],
                default=1,
                verbose_name="Status",
            ),
        ),
    ]
