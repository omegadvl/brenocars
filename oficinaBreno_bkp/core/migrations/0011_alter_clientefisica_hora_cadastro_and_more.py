# Generated by Django 4.0.6 on 2023-04-20 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_clientejuridica_hora_cadastro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientefisica',
            name='Hora_Cadastro',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='clientejuridica',
            name='Hora_Cadastro',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='Hora_Cadastro',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='Hora_Cadastro',
            field=models.TimeField(auto_now_add=True),
        ),
    ]