# Generated by Django 4.1.7 on 2023-03-14 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0003_alter_flight_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
