# Generated by Django 5.1.3 on 2025-02-01 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0004_postoffre'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidat',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
