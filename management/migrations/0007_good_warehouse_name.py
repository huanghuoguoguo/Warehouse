# Generated by Django 3.2.3 on 2021-05-23 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_alter_good_warehouse_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='warehouse_name',
            field=models.CharField(default=' ', max_length=10, verbose_name='仓库名称'),
            preserve_default=False,
        ),
    ]
