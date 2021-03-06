# Generated by Django 2.0.5 on 2018-06-13 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='문제세트명')),
            ],
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='part',
            name='Set',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='voca.TestSet'),
            preserve_default=False,
        ),
    ]
