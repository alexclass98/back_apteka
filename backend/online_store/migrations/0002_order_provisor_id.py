# Generated by Django 4.2 on 2023-04-09 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='provisor_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
