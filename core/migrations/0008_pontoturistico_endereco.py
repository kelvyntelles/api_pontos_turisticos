# Generated by Django 4.2 on 2023-04-17 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
        ('core', '0007_pontoturistico_avaliacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='endereco.endereco'),
            preserve_default=False,
        ),
    ]