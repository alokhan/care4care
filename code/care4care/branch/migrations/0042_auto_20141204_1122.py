# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0041_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='creator',
            field=models.ForeignKey(verbose_name='Branch administrators', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='branch',
            name='location',
            field=models.CharField(blank=True, null=True, verbose_name='Address', max_length=256),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='branch',
            name='members',
            field=models.ManyToManyField(through='branch.BranchMembers', verbose_name="Branch's members", to=settings.AUTH_USER_MODEL, null=True, blank=True, related_name='members'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(verbose_name="Branch's name", max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='branchmembers',
            name='joined',
            field=models.DateTimeField(verbose_name='Listing date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(verbose_name='Comment'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='object_id',
            field=models.PositiveIntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='branch',
            field=models.ForeignKey(verbose_name='Branch', to='branch.Branch', related_name='demand_branch'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(verbose_name='Type of help', max_length=21, choices=[('1', 'Visit home'), ('2', 'Companionship'), ('3', 'Transport by car'), ('4', 'Shopping'), ('5', 'House sitting'), ('6', 'Manual jobs'), ('7', 'Gardening'), ('8', 'Pet sitting'), ('9', 'Personal care'), ('a', 'Administrative'), ('b', 'Other ...')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='closed',
            field=models.BooleanField(default=False, verbose_name='Assigned volunteer'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='donor',
            field=models.ForeignKey(verbose_name='Sender', to=settings.AUTH_USER_MODEL, null=True, blank=True, related_name='demand_donor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='estimated_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Estimetad time (in minutes)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='km',
            field=models.IntegerField(blank=True, null=True, verbose_name='Trip distance'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='location',
            field=models.CharField(blank=True, null=True, verbose_name='Address', max_length=256),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='real_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Real time (int minutes)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='receive_help_from_who',
            field=models.IntegerField(default=5, verbose_name='Who can see and respond to demand/offer', choices=[(5, 'All'), (3, 'Verified member'), (6, 'My favorite members')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='receiver',
            field=models.ForeignKey(verbose_name='Receiver', to=settings.AUTH_USER_MODEL, null=True, blank=True, related_name='demand_receiver'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='success',
            field=models.NullBooleanField(verbose_name='Succeded', default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='time',
            field=multiselectfield.db.fields.MultiSelectField(help_text='Select the hours that suit you', verbose_name='Busy time', max_length=17, choices=[(1, 'Early morning (8h-10h)'), (2, 'Late morning (10h-12h)'), (3, 'Noon (12h-13h)'), (4, 'Early afternoon (13h-16h)'), (5, 'Late afternoon (16h-19h)'), (6, 'Supper (19h-20h)'), (7, 'Early evening (20h-22h) '), (8, 'Late evening (22h-00h)'), (9, 'Night (00h-8h)')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='title',
            field=models.CharField(null=True, verbose_name='Title', max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandproposition',
            name='accepted',
            field=models.BooleanField(default=False, verbose_name='Proposition accepted'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandproposition',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Additional comments'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandproposition',
            name='created',
            field=models.DateTimeField(auto_now=True, verbose_name='Creation date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandproposition',
            name='km',
            field=models.IntegerField(blank=True, null=True, verbose_name='Trip distance'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandproposition',
            name='time',
            field=multiselectfield.db.fields.MultiSelectField(help_text='Select the hours that suit you', verbose_name='Hour chosen', max_length=17, choices=[(1, 'Early morning (8h-10h)'), (2, 'Late morning (10h-12h)'), (3, 'Noon (12h-13h)'), (4, 'Early afternoon (13h-16h)'), (5, 'Late afternoon (16h-19h)'), (6, 'Supper (19h-20h)'), (7, 'Early evening (20h-22h) '), (8, 'Late evening (22h-00h)'), (9, 'Night (00h-8h)')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='branch',
            field=models.ForeignKey(verbose_name='Branch', to='branch.Branch', related_name='offer_branch'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(verbose_name='Type of help', max_length=21, choices=[('1', 'Visit home'), ('2', 'Companionship'), ('3', 'Transport by car'), ('4', 'Shopping'), ('5', 'House sitting'), ('6', 'Manual jobs'), ('7', 'Gardening'), ('8', 'Pet sitting'), ('9', 'Personal care'), ('a', 'Administrative'), ('b', 'Other ...')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='donor',
            field=models.ForeignKey(verbose_name='Sender', to=settings.AUTH_USER_MODEL, null=True, blank=True, related_name='offer_donor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='receive_help_from_who',
            field=models.IntegerField(default=5, verbose_name='Who can see and respond to demand/offer', choices=[(5, 'All'), (3, 'Verified member'), (6, 'My favorite members')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='receiver',
            field=models.ForeignKey(verbose_name='Receiver', to=settings.AUTH_USER_MODEL, null=True, blank=True, related_name='offer_receiver'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='time',
            field=multiselectfield.db.fields.MultiSelectField(help_text='Select the hours that suit you', verbose_name='Busy time', max_length=17, choices=[(1, 'Early morning (8h-10h)'), (2, 'Late morning (10h-12h)'), (3, 'Noon (12h-13h)'), (4, 'Early afternoon (13h-16h)'), (5, 'Late afternoon (16h-19h)'), (6, 'Supper (19h-20h)'), (7, 'Early evening (20h-22h) '), (8, 'Late evening (22h-00h)'), (9, 'Night (00h-8h)')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='successdemand',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Comments'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='successdemand',
            name='created',
            field=models.DateTimeField(auto_now=True, verbose_name='Creation date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='successdemand',
            name='time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Time spent (in minutes)'),
            preserve_default=True,
        ),
    ]
