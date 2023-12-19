# Generated by Django 4.2.4 on 2023-11-16 10:03

from django.db import migrations, models
import django.db.models.deletion
import main_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(validators=[main_app.validators.validate_menu_categories])),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.restaurant')),
            ],
        ),
    ]
