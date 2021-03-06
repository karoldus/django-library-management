# Generated by Django 3.2.5 on 2021-08-31 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production_year', models.IntegerField()),
                ('avalible', models.BooleanField(default=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.booktype')),
            ],
        ),
    ]
