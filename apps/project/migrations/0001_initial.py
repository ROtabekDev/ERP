# Generated by Django 4.2 on 2023-04-13 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('full_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Ism, familiyasi')),
                ('client_type', models.CharField(choices=[('physical_person', 'Jismoniy_shaxs'), ('legal_entity', 'Yuridik shaxs')], verbose_name='Mijoz turi')),
            ],
            options={
                'verbose_name': 'Mijoz',
                'verbose_name_plural': 'Mijozlar',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('title', models.CharField(max_length=150, verbose_name='Nomi')),
                ('slug', models.SlugField(max_length=150, verbose_name='Slugi')),
            ],
            options={
                'verbose_name': 'Tashkilot',
                'verbose_name_plural': 'Tashkilotlar',
            },
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('title', models.CharField(max_length=150, verbose_name='Nomi')),
                ('slug', models.SlugField(max_length=150, verbose_name='Slugi')),
            ],
            options={
                'verbose_name': 'Loyiha kategoriyasi',
                'verbose_name_plural': 'Loyiha kategoriyalari',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')),
                ('title', models.CharField(max_length=150, verbose_name='Nomi')),
                ('slug', models.SlugField(max_length=150, verbose_name='Slugi')),
                ('description', models.TextField(verbose_name='Tavsifi')),
                ('deadline', models.DateField(verbose_name='Tugatish vaqti')),
                ('status', models.CharField(choices=[('new', 'Yangi'), ('in_progress', 'Jarayonda'), ('finished', 'Tugatilgan')], default='new', max_length=20, verbose_name='Holati')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Narxi')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='project.client', verbose_name='Mijoz')),
                ('project_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='project.projectcategory', verbose_name='Kategoriyasi')),
            ],
            options={
                'verbose_name': 'Loyiha',
                'verbose_name_plural': 'Loyihalar',
            },
        ),
        migrations.AddField(
            model_name='client',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.organization', verbose_name='Tashkilot'),
        ),
    ]
