# Generated by Django 4.1.4 on 2023-01-07 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.IntegerField(choices=[(0, 'GRAMM'), (1, 'MILLILITR'), (2, 'DONA')]),
        ),
    ]
