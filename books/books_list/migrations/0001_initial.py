# Generated by Django 4.0.4 on 2022-04-21 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('publish_date', models.DateField()),
                ('add_to_site_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('appropriate', models.CharField(choices=[('-18', 'Under 18'), ('18-25', '18-25'), ('+25', 'adults')], max_length=200)),
                ('image', models.ImageField(upload_to='books_list/uploads/covers')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books_list.author')),
            ],
        ),
    ]
