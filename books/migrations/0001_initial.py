# Generated by Django 4.2.1 on 2023-09-27 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Name', max_length=100)),
                ('surname', models.CharField(default='surname', max_length=100)),
                ('personal_thoughts', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title', max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('genre', models.CharField(default='Genre', max_length=100)),
                ('release_date', models.DateTimeField()),
                ('personal_thoughts', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author')),
            ],
        ),
    ]
