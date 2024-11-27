# Generated by Django 5.1.3 on 2024-11-26 22:00

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('mileage', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(max_length=255)),
                ('is_available', models.BooleanField(default=True)),
                ('thumbnail_image', models.ImageField(blank=True, null=True, upload_to='car_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarFilter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year_min', models.IntegerField()),
                ('year_max', models.IntegerField()),
                ('price_min', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_max', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Dealership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='car_images/')),
                ('is_primary', models.BooleanField(default=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='zoomz.car')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='dealership',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='zoomz.dealership'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_user_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_criteria', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoomz.user')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('review_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zoomz.car')),
                ('dealership', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zoomz.dealership')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoomz.user')),
            ],
        ),
        migrations.CreateModel(
            name='ContactInquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoomz.car')),
                ('dealership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoomz.dealership')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoomz.user')),
            ],
        ),
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='zoomz.user')),
            ],
        ),
    ]