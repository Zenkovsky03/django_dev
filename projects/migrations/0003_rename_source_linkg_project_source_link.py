# Generated by Django 4.2.6 on 2023-10-29 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_tag_project_vote_ratio_project_vote_total_review_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='source_linkg',
            new_name='source_link',
        ),
    ]
