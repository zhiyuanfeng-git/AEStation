# Generated by Django 5.0.4 on 2024-04-17 07:17

import accounts.models.manager
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_usermodel_is_staff'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usermodel',
            managers=[
                ('objects', accounts.models.manager.UserModelManager()),
            ],
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
