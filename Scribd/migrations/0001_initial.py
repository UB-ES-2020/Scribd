# Generated by Django 3.1.2 on 2020-10-29 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ebook_number', models.CharField(default='', max_length=8, unique=True)),
                ('title', models.CharField(default='', max_length=50)),
                ('autor', models.CharField(default='', max_length=50)),
                ('description', models.TextField(default='')),
                ('is_promot', models.BooleanField(default='False')),
                ('size', models.IntegerField(default=0)),
                ('media_type', models.CharField(choices=[('pdf', 'pdf'), ('epub', 'epub')], default='', max_length=5)),
                ('featured_photo', models.ImageField(default='scribd/static/images/', upload_to='scribd/static/images/')),
                ('count_downloads', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Ebook',
                'verbose_name_plural': 'Ebooks',
            },
        ),
        migrations.CreateModel(
            name='EbookInsertDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('ebook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scribd.ebook')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=1000)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_registration', models.DateField(auto_now_add=True)),
                ('subscription', models.BooleanField()),
                ('type', models.CharField(choices=[('admin', 'admin'), ('provider', 'provider'), ('support', 'support'), ('free_trial', 'free_trial'), ('subscribed', 'subscribed')], max_length=15)),
            ],
            options={
                'verbose_name': 'User',
                'ordering': ['username'],
            },
        ),
        migrations.CreateModel(
            name='ViewedEbooks',
            fields=[
                ('id_vr', models.AutoField(primary_key=True, serialize=False)),
                ('ebook', models.ManyToManyField(through='Scribd.EbookInsertDate', to='Scribd.Ebook')),
            ],
        ),
        migrations.CreateModel(
            name='SubscribedUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_subs', models.DateField(auto_now_add=True)),
                ('free_trial', models.BooleanField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scribd.user')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value_stars', models.CharField(choices=[('One star', 1), ('Two stars', 2), ('Three stars', 3), ('Four stars', 4), ('Five stars', 5)], max_length=12)),
                ('comment', models.TextField()),
                ('ebook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scribd.ebook')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Scribd.user')),
            ],
        ),
        migrations.AddField(
            model_name='ebookinsertdate',
            name='viewed_ebooks',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scribd.viewedebooks'),
        ),
    ]
