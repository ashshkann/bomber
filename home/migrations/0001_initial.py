# Generated by Django 3.2.6 on 2021-08-22 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about_site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_text', models.TextField()),
                ('about_title_text1', models.CharField(max_length=50)),
                ('about_shourt_text1', models.TextField()),
                ('about_title_text2', models.CharField(max_length=50)),
                ('about_shourt_text2', models.TextField()),
                ('about_title_text3', models.CharField(max_length=50)),
                ('about_shourt_text3', models.TextField()),
                ('about_title_text4', models.CharField(max_length=50)),
                ('about_shourt_text4', models.TextField()),
                ('about_title_text5', models.CharField(max_length=50)),
                ('about_shourt_text5', models.TextField()),
                ('bout_title_text6', models.CharField(max_length=50)),
                ('about_shourt_text6', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='header_site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_logo', models.CharField(max_length=20)),
                ('title_text', models.TextField()),
                ('title_about', models.TextField()),
                ('title_background_image', models.ImageField(upload_to='')),
                ('title_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
