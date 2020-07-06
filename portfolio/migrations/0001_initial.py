# Generated by Django 3.0.8 on 2020-07-06 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('about_image', models.ImageField(upload_to='about')),
                ('about_title_help', models.CharField(max_length=400)),
                ('about_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CaseWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='case')),
                ('read_more', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_logo', models.ImageField(upload_to='brand')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('profession', models.CharField(max_length=400)),
                ('name', models.CharField(max_length=400)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=400)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('submit_email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('privacy', models.TextField()),
                ('term', models.TextField()),
                ('copy_right', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='FQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=400)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home')),
                ('title', models.CharField(max_length=400)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Live_work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('subtitle', models.CharField(max_length=400)),
                ('video_link', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('subtitle', models.CharField(max_length=400)),
                ('about_image', models.ImageField(upload_to='service')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='brand')),
                ('title', models.CharField(max_length=400)),
                ('comments', models.CharField(max_length=400)),
                ('read_more', models.URLField(max_length=500)),
                ('admin_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]