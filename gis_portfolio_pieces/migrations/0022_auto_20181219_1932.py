# Generated by Django 2.1.4 on 2018-12-19 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gis_portfolio_pieces', '0021_auto_20181219_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='portitem',
            name='intro_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portitem',
            name='weight',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portitempiece',
            name='external_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portitempiece',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
