# Generated by Django 3.1.7 on 2021-02-24 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=255)),
                ('meaning', models.TextField()),
                ('synonym', models.TextField(blank=True, null=True)),
                ('antonym', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
