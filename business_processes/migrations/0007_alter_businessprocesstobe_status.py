# Generated by Django 4.1.7 on 2023-03-28 13:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("business_processes", "0006_businessprocesstobe_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="businessprocesstobe",
            name="status",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (1, "Draft"),
                    (2, "Review"),
                    (3, "Approved"),
                    (4, "Not approved"),
                    (5, "Agreed"),
                    (6, "Not agreed"),
                ],
                default=1,
                verbose_name="Status",
            ),
        ),
    ]
