# Generated by Django 3.1.5 on 2021-01-25 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('status', models.CharField(choices=[('S', 'Standard'), ('P', 'Premium')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='UpgradeRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('N', 'New'), ('A', 'Accepted'), ('R', 'Rejected')], max_length=2)),
            ],
        ),
    ]
