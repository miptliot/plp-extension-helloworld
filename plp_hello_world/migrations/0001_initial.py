# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plp', '0071_participant_is_graduate'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityInstructor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500, verbose_name='\u0418\u043c\u044f \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044f')),
                ('university', models.ManyToManyField(to='plp.University', verbose_name='\u0423\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c \u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442\u0430',
                'verbose_name_plural': '\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u0438 \u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442\u043e\u0432',
            },
        ),
    ]
