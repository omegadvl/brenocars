# Generated by Django 4.0.6 on 2023-04-20 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_clientejuridica_uf_alter_fornecedor_uf'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientefisica',
            name='Hora_Cadastro',
            field=models.TimeField(auto_now=True),
        ),
    ]
