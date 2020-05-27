# Generated by Django 3.0.6 on 2020-05-27 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_billingprofile_customer_id'),
        ('orders', '0005_auto_20200526_0458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_id', models.CharField(blank=True, max_length=120, null=True)),
                ('brand', models.CharField(blank=True, max_length=120, null=True)),
                ('country', models.CharField(blank=True, max_length=120, null=True)),
                ('exp_month', models.IntegerField(blank=True, null=True)),
                ('exp_year', models.IntegerField(blank=True, null=True)),
                ('last4', models.CharField(blank=True, max_length=4, null=True)),
                ('billing_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='billing.BillingProfile')),
            ],
        ),
    ]
