# Generated by Django 3.1.5 on 2021-01-25 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_contract'),
    ]

    operations = [
        migrations.AddField(
            model_name='upgraderequest',
            name='note_by_approver',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
