# Generated by Django 2.0 on 2018-10-17 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodicTransfer',
            fields=[
                ('transfer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='banking.Transfer')),
                ('name', models.CharField(max_length=200)),
            ],
            bases=('banking.transfer',),
        ),
    ]
