# Generated by Django 5.0.6 on 2024-07-06 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_books_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(default='Books', upload_to='book/'),
            preserve_default=False,
        ),
    ]
