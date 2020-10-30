# Generated by Django 2.0.6 on 2020-10-29 13:02

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('author_name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
            ],
            options={
                'verbose_name': '作者',
                'verbose_name_plural': '作者',
                'db_table': 'drf_author',
            },
        ),
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('phone', models.CharField(max_length=11)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='app.Author')),
            ],
            options={
                'verbose_name': '作者详情',
                'verbose_name_plural': '作者详情',
                'db_table': 'drf_author_detail',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('book_name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('pic', models.ImageField(default='img/1.jpg', upload_to='img')),
                ('authors', models.ManyToManyField(db_constraint=False, related_name='books', to='app.Author')),
            ],
            options={
                'verbose_name': '图书',
                'verbose_name_plural': '图书',
                'db_table': 'drf_book',
            },
        ),
        migrations.CreateModel(
            name='Press',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('press_name', models.CharField(max_length=20)),
                ('pic', models.ImageField(default='img/1,jpg', upload_to='img')),
                ('address', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': '出版社',
                'verbose_name_plural': '出版社',
                'db_table': 'drf_press',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='publish',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='app.Press'),
        ),
    ]
