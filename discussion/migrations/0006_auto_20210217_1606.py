# Generated by Django 3.1.6 on 2021-02-17 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0005_qa_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qa',
            name='tags',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='discussion.qa'),
            preserve_default=False,
        ),
    ]
