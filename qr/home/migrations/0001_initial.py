# Generated by Django 4.0.4 on 2022-05-04 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lname', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=222)),
                ('fname', models.TextField(null=True)),
                ('date', models.DateField()),
            ],
        ),
    ]
