# Generated by Django 5.2.3 on 2025-07-20 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0005_doc_slots_doctors_slot_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="doctors",
            name="slot_id",
        ),
        migrations.AddField(
            model_name="doc_slots",
            name="doc_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="homepage.doctors",
            ),
        ),
    ]
