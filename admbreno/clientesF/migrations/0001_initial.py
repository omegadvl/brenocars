# Generated by Django 4.1 on 2023-04-07 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("sobrenome", models.CharField(max_length=100)),
                ("profissao", models.CharField(max_length=100)),
                ("cep", models.CharField(max_length=8)),
                ("endereco", models.CharField(max_length=200)),
                ("cidade", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("data_nascimento", models.DateField()),
                ("cpf", models.CharField(max_length=11)),
                ("telefone", models.CharField(max_length=15)),
                ("celular", models.CharField(max_length=15)),
                ("estado", models.CharField(max_length=100)),
                ("uf", models.CharField(max_length=2)),
            ],
        ),
    ]