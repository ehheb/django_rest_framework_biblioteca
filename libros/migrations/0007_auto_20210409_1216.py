# Generated by Django 2.2 on 2021-04-09 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0006_auto_20210409_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='editorial',
            field=models.ForeignKey(on_delete=True, related_name='libros', to='editoriales.Editorial'),
        ),
    ]