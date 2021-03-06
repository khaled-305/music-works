# Generated by Django 4.0.4 on 2022-05-02 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, help_text='music work title', max_length=100, null=True, unique=True)),
                ('contributors', models.CharField(blank=True, help_text='contributors of a music work', max_length=250, null=True, unique=True)),
                ('iswc', models.CharField(blank=True, help_text='music work iswc', max_length=200, null=True, unique=True)),
            ],
        ),
    ]
