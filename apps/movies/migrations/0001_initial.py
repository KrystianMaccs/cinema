# Generated by Django 4.0 on 2023-04-12 14:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('protagonists', models.CharField(max_length=120)),
                ('poster', models.ImageField(upload_to='')),
                ('start_date', models.DateField()),
                ('status', models.CharField(choices=[('CU', 'Coming up'), ('ST', 'Starting'), ('RN', 'Running'), ('FN', 'Finished')], default='CU', max_length=2)),
                ('ranking', models.IntegerField(choices=[(1, 'Poor'), (2, 'Fair'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=0, help_text='1=Poor, 2=Fair, 3=Good, 4=Very Good, Excellent', verbose_name='Rating')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
