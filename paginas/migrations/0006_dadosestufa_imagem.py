# Generated by Django 3.2.7 on 2021-11-26 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0005_dadosestufa_referencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='dadosestufa',
            name='imagem',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
