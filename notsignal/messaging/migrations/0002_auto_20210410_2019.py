# Generated by Django 3.1.8 on 2021-04-10 20:19

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=django_cryptography.fields.encrypt(models.TextField(verbose_name='Content')),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.CharField(max_length=1000, verbose_name='Username'),
        ),
    ]
