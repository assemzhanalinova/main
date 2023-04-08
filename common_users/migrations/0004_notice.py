# Generated by Django 4.1.7 on 2023-04-03 23:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("common_users", "0003_commonuser_parent"),
    ]

    operations = [
        migrations.CreateModel(
            name="Notice",
            fields=[
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, db_index=True),
                ),
                ("updated", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(default=False)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="Title"),
                ),
                (
                    "text",
                    models.CharField(max_length=225, verbose_name="Text"),
                ),
                ("is_read", models.BooleanField(default=False)),
                (
                    "recipient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notices",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Notice",
                "verbose_name_plural": "Notices",
                "db_table": "notices",
            },
        ),
    ]