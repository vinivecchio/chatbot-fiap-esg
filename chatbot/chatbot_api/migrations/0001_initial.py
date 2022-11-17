# Generated by Django 3.2.15 on 2022-09-29 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('valor', models.CharField(max_length=1)),
                ('descricao', models.TextField()),
                ('acao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('titulo', models.TextField()),
                ('respostas', models.ManyToManyField(to='chatbot_api.Resposta')),
            ],
        ),
    ]
