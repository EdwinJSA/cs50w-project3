# Generated by Django 2.1.4 on 2018-12-17 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20181216_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order2',
            name='amount',
        ),
        migrations.AddField(
            model_name='order2',
            name='category',
            field=models.CharField(max_length=64, null=True),
        ),
    ]