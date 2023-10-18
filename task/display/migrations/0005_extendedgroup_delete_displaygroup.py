# Generated by Django 4.2.6 on 2023-10-18 15:12

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('display', '0004_displaygroup_delete_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.group')),
                ('description', models.CharField(max_length=255)),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.DeleteModel(
            name='DisplayGroup',
        ),
    ]
