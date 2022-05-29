# Generated by Django 4.0.4 on 2022-05-28 06:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CourseApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('image', models.ImageField(default=None, upload_to='courses/%Y/%m')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CourseApp.category')),
            ],
            options={
                'ordering': ['-id'],
                'unique_together': {('subject', 'category')},
            },
        ),
    ]
