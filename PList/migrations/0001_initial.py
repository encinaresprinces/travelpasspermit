# Generated by Django 3.1.6 on 2021-06-24 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barangay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zbarangay', models.CharField(default='', max_length=50)),
                ('municipal', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('swabresult', models.TextField(default='', max_length=50)),
                ('identificationCards', models.FileField(upload_to='documents/')),
                ('transportation', models.TextField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TravelerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tname', models.TextField(default='', max_length=50)),
                ('birthday', models.CharField(default='', max_length=10)),
                ('gender', models.TextField(default='', max_length=10)),
                ('address', models.CharField(default='', max_length=50)),
                ('cnumber', models.IntegerField(default='')),
                ('email', models.CharField(default='', max_length=50)),
                ('barangay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PList.barangay')),
            ],
        ),
        migrations.CreateModel(
            name='Trequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departuredate', models.DateField(default='', max_length=12)),
                ('returndate', models.DateField(default='', max_length=12)),
                ('destinationtravel', models.CharField(default='', max_length=50)),
                ('travelprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PList.travelerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rstatus', models.TextField(default='', max_length=50)),
                ('remarks', models.TextField(default='', max_length=50)),
                ('requirements', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PList.requirements')),
            ],
        ),
        migrations.AddField(
            model_name='requirements',
            name='travelprofile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PList.travelerprofile'),
        ),
    ]
