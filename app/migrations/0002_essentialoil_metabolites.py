# Generated by Django 2.2.6 on 2019-10-22 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='essentialoil',
            name='metabolites',
            field=models.ManyToManyField(through='app.Through', to='app.Metabolite'),
        ),
    ]