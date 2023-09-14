# Generated by Django 4.2.5 on 2023-09-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_alter_reservation_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='adults',
            field=models.CharField(choices=[(1, '1'), (2, '2'), (3, '3')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='children',
            field=models.CharField(choices=[(1, '1'), (2, '2'), (3, '3')], max_length=3, null=True),
        ),
    ]
