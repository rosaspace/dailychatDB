# Generated by Django 4.1.7 on 2024-10-02 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('beginner', '初级'), ('intermediate', '中级'), ('advanced', '高级')], max_length=20)),
                ('audio_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Dialogue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.TextField()),
                ('chinese', models.TextField()),
                ('order', models.IntegerField()),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dialogues', to='simplechat.conversation')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
