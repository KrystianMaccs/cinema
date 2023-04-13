# Generated by Django 4.0 on 2023-04-12 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='movie',
            name='protagonists',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('CU', 'Coming up'), ('ST', 'Starting'), ('RN', 'Running'), ('FN', 'Finished')], default='CU', max_length=250),
        ),
    ]
