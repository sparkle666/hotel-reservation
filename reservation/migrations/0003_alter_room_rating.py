# Generated by Django 4.2.4 on 2023-09-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_alter_room_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='rating',
            field=models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=2),
        ),
    ]