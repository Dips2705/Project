# Generated by Django 2.2.2 on 2019-07-29 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imageUrl',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
