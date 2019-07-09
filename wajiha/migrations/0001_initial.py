# Generated by Django 2.2.3 on 2019-07-08 14:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpportunityCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('start_at', models.DateField(null=True)),
                ('end_at', models.DateField(null=True)),
                ('website', models.URLField(null=True)),
                ('phone_number', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('age_min', models.IntegerField(null=True)),
                ('age_max', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='wajiha.OpportunityCategory')),
            ],
        ),
    ]