# Generated by Django 3.2.4 on 2021-06-14 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobile',
            field=models.CharField(max_length=10, null=True),
        ),
    ]