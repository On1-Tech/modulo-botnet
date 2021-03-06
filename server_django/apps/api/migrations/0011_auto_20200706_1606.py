# Generated by Django 3.0.7 on 2020-07-06 08:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20200706_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('session_id', models.IntegerField()),
                ('output', models.TextField(default='', max_length=100000)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outputs', to='api.Agent')),
            ],
        ),
        migrations.DeleteModel(
            name='Output_session',
        ),
    ]
