# Generated by Django 2.2.3 on 2019-07-10 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wajiha', '0007_auto_20190709_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='image',
            field=models.ImageField(default='media/default.jpg', upload_to=''),
            preserve_default=False,
        ),
    ]
