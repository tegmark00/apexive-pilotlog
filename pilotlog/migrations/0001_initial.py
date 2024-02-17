# Generated by Django 5.0.2 on 2024-02-17 15:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('record_modified', models.DateTimeField()),
                ('aircraft_code', models.UUIDField(primary_key=True, serialize=False)),
                ('fin', models.CharField(max_length=10)),
                ('sea', models.BooleanField()),
                ('tmg', models.BooleanField()),
                ('efis', models.BooleanField()),
                ('eng_group', models.IntegerField(blank=True, null=True)),
                ('eng_type', models.IntegerField(blank=True, null=True)),
                ('fnpt', models.IntegerField()),
                ('make', models.CharField(max_length=50)),
                ('run2', models.BooleanField()),
                ('aircraft_class', models.IntegerField(db_column='class')),
                ('model', models.CharField(max_length=50)),
                ('power', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('active', models.BooleanField()),
                ('kg5700', models.IntegerField()),
                ('rating', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('complex', models.BooleanField()),
                ('cond_log', models.IntegerField()),
                ('fav_list', models.BooleanField()),
                ('category', models.IntegerField()),
                ('high_perf', models.BooleanField()),
                ('sub_model', models.CharField(max_length=50)),
                ('aerobatic', models.BooleanField()),
                ('ref_search', models.CharField(max_length=50)),
                ('reference', models.CharField(max_length=50)),
                ('tail_wheel', models.BooleanField()),
                ('default_app', models.IntegerField()),
                ('default_log', models.IntegerField()),
                ('default_ops', models.IntegerField()),
                ('device_code', models.IntegerField()),
                ('default_launch', models.IntegerField()),
            ],
            options={
                'db_table': 'aircraft',
            },
        ),
        migrations.CreateModel(
            name='AirField',
            fields=[
                ('record_modified', models.DateTimeField()),
                ('af_code', models.UUIDField(primary_key=True, serialize=False)),
                ('af_cat', models.IntegerField()),
                ('afiata', models.CharField(max_length=10)),
                ('aficao', models.CharField(max_length=10)),
                ('af_name', models.CharField(max_length=100)),
                ('affaa', models.CharField(blank=True, max_length=10, null=True)),
                ('user_edit', models.BooleanField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('notes', models.CharField(blank=True, max_length=100, null=True)),
                ('tz_code', models.CharField(max_length=10)),
                ('latitude', models.FloatField()),
                ('show_list', models.BooleanField()),
                ('af_country', models.CharField(max_length=50)),
                ('longitude', models.FloatField()),
                ('notes_user', models.CharField(max_length=100)),
                ('region_user', models.CharField(max_length=100)),
                ('elevation_ft', models.IntegerField()),
            ],
            options={
                'db_table': 'airfield',
            },
        ),
        migrations.CreateModel(
            name='ImagePic',
            fields=[
                ('record_modified', models.DateTimeField()),
                ('img_code', models.UUIDField(primary_key=True, serialize=False)),
                ('file_ext', models.CharField(max_length=10)),
                ('file_name', models.CharField(max_length=100)),
                ('link_code', models.UUIDField()),
                ('img_upload', models.BooleanField()),
                ('img_download', models.BooleanField()),
            ],
            options={
                'db_table': 'image_pic',
            },
        ),
        migrations.CreateModel(
            name='LimitRules',
            fields=[
                ('record_modified', models.DateTimeField()),
                ('limit_code', models.UUIDField(primary_key=True, serialize=False)),
                ('l_to', models.DateField()),
                ('l_from', models.DateField()),
                ('l_type', models.IntegerField()),
                ('l_zone', models.IntegerField()),
                ('l_minutes', models.IntegerField()),
                ('l_period_code', models.IntegerField()),
            ],
            options={
                'db_table': 'limit_rules',
            },
        ),
        migrations.CreateModel(
            name='MyQuery',
            fields=[
                ('record_modified', models.DateTimeField()),
                ('mq_code', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('quick_view', models.BooleanField()),
                ('short_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'my_query',
            },
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('record_modified', models.DateTimeField()),
                ('pilot_code', models.UUIDField(primary_key=True, serialize=False)),
                ('notes', models.CharField(max_length=100)),
                ('active', models.BooleanField()),
                ('company', models.CharField(max_length=100)),
                ('fav_list', models.BooleanField()),
                ('user_api', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=100)),
                ('linkedin', models.CharField(max_length=100)),
                ('pilot_ref', models.CharField(max_length=100)),
                ('pilot_name', models.CharField(max_length=100)),
                ('pilot_email', models.CharField(max_length=100)),
                ('pilot_phone', models.CharField(max_length=100)),
                ('certificate', models.CharField(max_length=100)),
                ('phone_search', models.CharField(max_length=100)),
                ('pilot_search', models.CharField(max_length=100)),
                ('roster_alias', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'pilot',
            },
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('record_modified', models.DateTimeField()),
                ('q_code', models.UUIDField(primary_key=True, serialize=False)),
                ('ref_extra', models.IntegerField()),
                ('ref_model', models.CharField(max_length=100)),
                ('validity', models.IntegerField()),
                ('date_valid', models.DateField(blank=True, null=True)),
                ('q_type_code', models.IntegerField()),
                ('date_issued', models.DateField(blank=True, null=True)),
                ('minimum_qty', models.IntegerField()),
                ('notify_days', models.IntegerField()),
                ('ref_air_field', models.UUIDField()),
                ('minimum_period', models.IntegerField()),
                ('notify_comment', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'qualification',
            },
        ),
        migrations.CreateModel(
            name='SettingConfig',
            fields=[
                ('record_modified', models.DateTimeField()),
                ('config_code', models.IntegerField(primary_key=True, serialize=False)),
                ('data', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('group', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'setting_config',
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('record_modified', models.DateTimeField()),
                ('flight_code', models.UUIDField(primary_key=True, serialize=False)),
                ('pf', models.BooleanField()),
                ('pax', models.IntegerField()),
                ('fuel', models.IntegerField()),
                ('de_ice', models.BooleanField()),
                ('route', models.CharField(max_length=100)),
                ('to_day', models.IntegerField()),
                ('min_u1', models.IntegerField()),
                ('min_u2', models.IntegerField()),
                ('min_u3', models.IntegerField()),
                ('min_u4', models.IntegerField()),
                ('min_xc', models.IntegerField()),
                ('arr_rwy', models.CharField(max_length=10)),
                ('dep_rwy', models.CharField(max_length=10)),
                ('ldg_day', models.IntegerField()),
                ('lift_sw', models.IntegerField()),
                ('p1_code', models.UUIDField()),
                ('p2_code', models.UUIDField()),
                ('p3_code', models.UUIDField()),
                ('p4_code', models.UUIDField()),
                ('report', models.CharField(max_length=100)),
                ('tag_ops', models.CharField(max_length=100)),
                ('to_edit', models.BooleanField()),
                ('min_air', models.IntegerField()),
                ('min_ifr', models.IntegerField()),
                ('min_pic', models.IntegerField()),
                ('min_rel', models.IntegerField()),
                ('min_sfr', models.IntegerField()),
                ('arr_code', models.UUIDField()),
                ('date_utc', models.DateField()),
                ('dep_code', models.UUIDField()),
                ('hobbs_in', models.IntegerField()),
                ('holding', models.IntegerField()),
                ('pairing', models.CharField(max_length=100)),
                ('remarks', models.CharField(max_length=100)),
                ('sign_box', models.IntegerField()),
                ('to_night', models.IntegerField()),
                ('user_num', models.IntegerField()),
                ('min_dual', models.IntegerField()),
                ('min_exam', models.IntegerField()),
                ('crew_list', models.CharField(max_length=100)),
                ('date_base', models.DateField(blank=True, null=True)),
                ('fuel_used', models.IntegerField()),
                ('hobbs_out', models.IntegerField()),
                ('ldg_night', models.IntegerField()),
                ('next_page', models.BooleanField()),
                ('tag_delay', models.CharField(max_length=100)),
                ('training', models.CharField(max_length=100)),
                ('user_bool', models.BooleanField()),
                ('user_text', models.CharField(max_length=100)),
                ('min_inst', models.IntegerField()),
                ('min_night', models.IntegerField()),
                ('min_picus', models.IntegerField()),
                ('min_total', models.IntegerField()),
                ('arr_offset', models.IntegerField()),
                ('date_local', models.DateTimeField(blank=True, null=True)),
                ('dep_offset', models.IntegerField()),
                ('tag_launch', models.CharField(max_length=100)),
                ('tag_lesson', models.CharField(max_length=100)),
                ('to_time_utc', models.IntegerField()),
                ('arr_time_utc', models.IntegerField()),
                ('base_offset', models.IntegerField()),
                ('cargo', models.IntegerField(blank=True, null=True)),
                ('dep_time_utc', models.IntegerField(blank=True, null=True)),
                ('ldg_time_utc', models.IntegerField()),
                ('fuel_planned', models.IntegerField()),
                ('next_summary', models.BooleanField()),
                ('tag_approach', models.CharField(max_length=100)),
                ('arr_time_sched', models.IntegerField()),
                ('dep_time_sched', models.IntegerField()),
                ('flight_number', models.CharField(max_length=10)),
                ('flight_search', models.CharField(max_length=100)),
                ('aircraft', models.ForeignKey(blank=True, db_column='aircraft_code', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pilotlog.aircraft')),
            ],
            options={
                'db_table': 'flight',
            },
        ),
        migrations.CreateModel(
            name='MyQueryBuild',
            fields=[
                ('record_modified', models.DateTimeField()),
                ('mqb_code', models.UUIDField(primary_key=True, serialize=False)),
                ('build_1', models.CharField(max_length=100)),
                ('build_2', models.IntegerField()),
                ('build_3', models.IntegerField()),
                ('build_4', models.CharField(max_length=100)),
                ('mq', models.ForeignKey(db_column='mq_code', on_delete=django.db.models.deletion.CASCADE, to='pilotlog.myquery')),
            ],
            options={
                'db_table': 'my_query_build',
            },
        ),
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.CharField(max_length=32)),
                ('user_id', models.PositiveBigIntegerField()),
                ('platform', models.PositiveIntegerField()),
                ('modified', models.DateTimeField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log_entries', to='contenttypes.contenttype')),
            ],
            options={
                'db_table': 'log_entry',
                'unique_together': {('content_type', 'guid')},
            },
        ),
    ]
