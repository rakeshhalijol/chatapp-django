from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .models import Detial
from django.contrib.auth.models import User
from channels.db import database_sync_to_async

import json

class DetialConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("connected")
        await self.accept()

    async def receive_json(self, content, **kwargs):
        data = content
        print(type(data))


        if data["command"] == "open":
            await self.channel_layer.group_add(
                data["roomname"],
                self.channel_name
            )
            print("User added")

        elif data["command"] == 'send':
            msg = data["message"]
            print(type(self.scope["user"]))
            print("hello before")
            # user = await database_sync_to_async(User.objects.filter)(username = self.scope["user"])

            # print(f"user is {user}")
            get_user = await database_sync_to_async(User.objects.get)(username = data["user"])
            print(get_user,type(get_user))
            create = Detial(user = get_user,msg = msg)
            await database_sync_to_async(create.save)()
            await self.channel_layer.group_send(data["roomname"],{
                "type":"chat.message",
                "msg":data["message"],
                "user":data["user"]
            })


    async def disconnect(self, code):
        print("disconnected")

    async def chat_message(self,event):
        await self.send_json({
            'user':event["user"],
            'message':event["msg"]
        })
