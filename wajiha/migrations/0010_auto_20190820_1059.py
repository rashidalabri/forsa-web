# Generated by Django 2.2.4 on 2019-08-20 06:59

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wajiha', '0009_auto_20190818_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
