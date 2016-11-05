# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goods_num', models.IntegerField()),
            ],
            options={
                'db_table': 'Cart',
            },
        ),
        migrations.CreateModel(
            name='Goods_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goods_name', models.CharField(max_length=20)),
                ('goods_description', tinymce.models.HTMLField()),
                ('goods_price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('goods_stock', models.IntegerField()),
                ('goods_msg', tinymce.models.HTMLField()),
                ('goods_unit', models.CharField(max_length=20)),
                ('goods_pic_url', models.ImageField(upload_to=b'uploads/')),
                ('goods_detail_pic_url', models.ImageField(upload_to=b'uploads/')),
            ],
            options={
                'db_table': 'Goods_info',
            },
        ),
        migrations.CreateModel(
            name='Goods_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goods_list_name', models.CharField(max_length=20)),
                ('goods_list_class', models.CharField(max_length=20)),
                ('goods_list_pic', models.ImageField(upload_to=b'uploads/')),
            ],
            options={
                'db_table': 'Goods_list',
            },
        ),
        migrations.CreateModel(
            name='Ord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_num', models.IntegerField(default=0)),
                ('submit_date', models.DateTimeField()),
                ('total_price', models.DecimalField(max_digits=20, decimal_places=2)),
                ('isPay', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'Ord',
            },
        ),
        migrations.CreateModel(
            name='Order_detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('odetail_goods_num', models.IntegerField(default=0)),
                ('odetail_totalprice', models.IntegerField(default=0)),
                ('detail_num', models.ForeignKey(to='booktest.Ord')),
                ('odetail_goods_id', models.ForeignKey(to='booktest.Goods_info')),
            ],
            options={
                'db_table': 'Order_detail',
            },
        ),
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('receiver_address', tinymce.models.HTMLField()),
                ('receiver_name', models.CharField(max_length=20)),
                ('receiver_phone', models.CharField(max_length=20)),
                ('receiver_email', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Receiver',
            },
        ),
        migrations.CreateModel(
            name='User_db',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=20)),
                ('user_password', models.CharField(max_length=20)),
                ('user_phone', models.CharField(max_length=20)),
                ('user_email', models.CharField(max_length=20)),
                ('user_address', tinymce.models.HTMLField()),
            ],
            options={
                'db_table': 'User_db',
            },
        ),
        migrations.AddField(
            model_name='receiver',
            name='receiver_user_id',
            field=models.ForeignKey(to='booktest.User_db'),
        ),
        migrations.AddField(
            model_name='ord',
            name='order_user_id',
            field=models.ForeignKey(to='booktest.User_db'),
        ),
        migrations.AddField(
            model_name='goods_info',
            name='goods_list_id',
            field=models.ForeignKey(to='booktest.Goods_list'),
        ),
        migrations.AddField(
            model_name='cart',
            name='goods_id',
            field=models.ForeignKey(to='booktest.Goods_info'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user_id',
            field=models.ForeignKey(to='booktest.User_db'),
        ),
    ]
