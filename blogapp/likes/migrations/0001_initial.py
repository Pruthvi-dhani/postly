# Generated by Django 5.2 on 2025-04-15 15:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        ('posts', '0001_initial'),
        ('user', '0003_alter_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.comments')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('user', 'comment'), name='commentlikes_user_id_comment_id_unique_constraint')],
            },
        ),
        migrations.CreateModel(
            name='PostLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.posts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('user', 'post'), name='postlikes_user_id_post_id_unique_constraint')],
            },
        ),
    ]
