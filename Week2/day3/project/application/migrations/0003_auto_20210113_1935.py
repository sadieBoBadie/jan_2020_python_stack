# Generated by Django 2.2.4 on 2021-01-13 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
