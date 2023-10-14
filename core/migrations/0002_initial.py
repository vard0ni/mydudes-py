# Generated by Django 3.2.18 on 2023-10-14 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='replycomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pagepost',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='page_post_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pagepost',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.page'),
        ),
        migrations.AddField(
            model_name='pagepost',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='page',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='page_followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='page',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notification',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='noti_comment', to='core.comment'),
        ),
        migrations.AddField(
            model_name='notification',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='noti_post', to='core.post'),
        ),
        migrations.AddField(
            model_name='notification',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='noti_sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='noti_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='grouppost',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.group'),
        ),
        migrations.AddField(
            model_name='grouppost',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='group_post_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='grouppost',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groupchatmessage',
            name='groupchat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_chat', to='core.groupchat'),
        ),
        migrations.AddField(
            model_name='groupchatmessage',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_chat_message_sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groupchat',
            name='host',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_host', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groupchat',
            name='members',
            field=models.ManyToManyField(related_name='group_chat_members', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='memebers',
            field=models.ManyToManyField(blank=True, related_name='memebers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gallery',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.post'),
        ),
        migrations.AddField(
            model_name='friendrequest',
            name='receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request_receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='friendrequest',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request_sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='friend',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='friend',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='comment_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='reciever',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reciever', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chat_user', to=settings.AUTH_USER_MODEL),
        ),
    ]