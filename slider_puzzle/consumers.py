from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class SliderPuzzleConsumer(WebsocketConsumer):
    def connect(self):
        game_id = self.scope['url_route']['kwargs']['game_id']
        self.accept()

        async_to_sync(self.channel_layer.group_add)(game_id, self.channel_name)

    def disconnect(self, close_code):
        game_id = self.scope['url_route']['kwargs']['game_id']
        async_to_sync(self.channel_layer.group_discard)(game_id, self.channel_name)

    def receive(self, text_data=None, bytes_data=None):
        game_id = self.scope['url_route']['kwargs']['game_id']
        async_to_sync(self.channel_layer.group_send)(
            game_id,
            {
                "type": "group_forward",
                "text": text_data,
            },
        )

    # receive from room then forward to everyone in group
    def group_forward(self, event):
        self.send(text_data=event['text'])