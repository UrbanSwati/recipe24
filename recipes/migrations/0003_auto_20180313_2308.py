# Generated by Django 2.0.3 on 2018-03-13 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(blank=True, default='default-image.jpg', upload_to=''),
        ),
    ]