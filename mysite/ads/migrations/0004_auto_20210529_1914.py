# Generated by Django 3.1.1 on 2021-05-29 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0003_auto_20201208_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='content_type',
            field=models.CharField(blank=True, help_text='The MIMType of the file', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='picture',
            field=models.BinaryField(blank=True, editable=True, null=True),
        ),
        migrations.CreateModel(
            name='Fav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.ad')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('ad', 'user')},
            },
        ),
        migrations.AddField(
            model_name='ad',
            name='favorites',
            field=models.ManyToManyField(related_name='favorite_ads', through='ads.Fav', to=settings.AUTH_USER_MODEL),
        ),
    ]
