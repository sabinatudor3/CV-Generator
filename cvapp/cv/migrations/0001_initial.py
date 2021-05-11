# Generated by Django 3.1.5 on 2021-05-10 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('data', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cv.data')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('', 'Choose..'), ('1', 'Template 1')], max_length=1)),
                ('data', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cv.data')),
            ],
        ),
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(max_length=300)),
                ('tech1', models.CharField(max_length=50)),
                ('tech2', models.CharField(blank=True, max_length=50, null=True)),
                ('tech3', models.CharField(blank=True, max_length=50, null=True)),
                ('data', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cv.data')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills1', models.CharField(choices=[('1', 'Communication'), ('2', 'Teamwork'), ('3', 'Innovation'), ('4', 'Leadership'), ('5', 'Motivation')], max_length=1)),
                ('skills2', models.CharField(choices=[('1', 'Problem-solving'), ('2', 'Organisation'), ('3', 'Perseverance'), ('4', 'Ability to work under pressure'), ('5', 'Adaptability')], max_length=1)),
                ('skills3', models.CharField(choices=[('1', 'Work Ethic'), ('2', 'Flexibility'), ('3', 'Time Management'), ('4', 'Critical Thinking'), ('5', 'Creativity')], max_length=1)),
                ('data', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cv.data')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language1', models.CharField(max_length=50)),
                ('language2', models.CharField(blank=True, max_length=50, null=True)),
                ('language3', models.CharField(blank=True, max_length=50, null=True)),
                ('data', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cv.data')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=50)),
                ('studies', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('data', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cv.data')),
            ],
        ),
    ]
