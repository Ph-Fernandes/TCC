# Generated by Django 4.0.4 on 2022-07-26 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mit_bal', models.IntegerField()),
                ('sex', models.PositiveSmallIntegerField()),
                ('education', models.PositiveSmallIntegerField()),
                ('marriage', models.PositiveSmallIntegerField()),
                ('age', models.PositiveSmallIntegerField()),
                ('pay_1', models.SmallIntegerField()),
                ('pay_2', models.SmallIntegerField()),
                ('pay_3', models.SmallIntegerField()),
                ('pay_4', models.SmallIntegerField()),
                ('pay_5', models.SmallIntegerField()),
                ('pay_6', models.SmallIntegerField()),
                ('bill_amt_1', models.IntegerField()),
                ('bill_amt_2', models.IntegerField()),
                ('bill_amt_3', models.IntegerField()),
                ('bill_amt_4', models.IntegerField()),
                ('bill_amt_5', models.IntegerField()),
                ('bill_amt_6', models.IntegerField()),
                ('pay_amt_1', models.IntegerField()),
                ('pay_amt_2', models.IntegerField()),
                ('pay_amt_3', models.IntegerField()),
                ('pay_amt_4', models.IntegerField()),
                ('pay_amt_5', models.IntegerField()),
                ('pay_amt_6', models.IntegerField()),
                ('payment', models.BinaryField()),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
    ]