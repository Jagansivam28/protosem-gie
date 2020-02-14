# Generated by Django 2.2.7 on 2019-12-02 12:11

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('cohort', models.CharField(blank=True, default='19.2', max_length=10, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Software_platforms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.IntegerField(blank=True, choices=[(1, 'Stage 1'), (2, 'Stage 2'), (3, 'Stage 3')], default=0, null=True)),
                ('eagle_pcb', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('psim_multi_sim', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('lab_view', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('matlab', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('tableau', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('tibco_spotfire', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('average_score', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sp', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.IntegerField(blank=True, choices=[(1, 'Stage 1'), (2, 'Stage 2'), (3, 'Stage 3')], default=0, null=True)),
                ('Linux_mac_packaging', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('cloud_platform', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('web_application_development', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('mobile_application_development', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('application_architecture_design', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('average_score', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='S', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Programming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.IntegerField(blank=True, choices=[(1, 'Stage 1'), (2, 'Stage 2'), (3, 'Stage 3')], default=0, null=True)),
                ('defining_problem', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('computer_science_fundamentals', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('programming_techniques', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('programming_languages', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('average_score', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='P', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product_design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.IntegerField(blank=True, choices=[(1, 'Stage 1'), (2, 'Stage 2'), (3, 'Stage 3')], default=0, null=True)),
                ('rapid_prototyping', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('principles_of_industrial_design', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('ui_ux_Design', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('cad', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('analysis_of_mechanical_design', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('average_score', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pd', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Intellectual_Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.IntegerField(blank=True, choices=[(1, 'Stage 1'), (2, 'Stage 2'), (3, 'Stage 3')], default=0, null=True)),
                ('ip_exploration', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('patent_drafting', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('average_score', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ip', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Innovation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.IntegerField(blank=True, choices=[(1, 'Stage 1'), (2, 'Stage 2'), (3, 'Stage 3')], default=0, null=True)),
                ('problem_validation', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('customer_development', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('testing_value_proposition', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('solution_alternatives_exploration', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('pitch', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('grant_proposal_writing', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('milestones_planning_reporting', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('average_score', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='I', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hardware_iot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.IntegerField(blank=True, choices=[(1, 'Stage 1'), (2, 'Stage 2'), (3, 'Stage 3')], default=0, null=True)),
                ('electronics_circuit_design', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('pcb_designing', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('embedded_hardware_platform', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('sensors_actuators', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('modules_integrations', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('system_interfaces_implementation', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('data_acquisition_techniques', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('basic_of_networking', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('power_design_for_circuits', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('average_score', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Hd', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.IntegerField(blank=True, choices=[(1, 'Stage 1'), (2, 'Stage 2'), (3, 'Stage 3')], default=0, null=True)),
                ('data_modelling_evaluation', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('probablity_statistics', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('applied_math_algorithms', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('applied_machine_learning', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('distributed_computing', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('edge_computing', models.IntegerField(blank=True, choices=[(10, 'LEANER'), (20, 'THINKER'), (30, 'HACKER'), (40, 'ENGINEER'), (50, 'EXPERT')], default=0, null=True)),
                ('average_score', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ai', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]