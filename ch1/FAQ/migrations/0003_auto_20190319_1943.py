# Generated by Django 2.0.13 on 2019-03-19 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FAQ', '0002_auto_20190315_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qna',
            name='text',
            field=models.TextField(),
        ),
    ]
