# Generated by Django 4.1.5 on 2023-01-22 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('short_description', models.TextField()),
                ('published_date', models.DateField()),
                ('image', models.ImageField(upload_to='blog/')),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
    ]
