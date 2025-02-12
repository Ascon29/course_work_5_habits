# Generated by Django 5.1.4 on 2025-01-09 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="associated_habit",
            field=models.ForeignKey(
                blank=True,
                help_text="укажите связанную привычку",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="habits.habit",
                verbose_name="связанная привычка",
            ),
        ),
    ]
