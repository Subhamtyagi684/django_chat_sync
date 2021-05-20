from channels.consumer import SyncConsumer,AsyncConsumer
from asgiref.sync import async_to_sync

class EchoConsumer(SyncConsumer):

    def websocket_connect(self, event):
        self.room_name = "lobby"
        async_to_sync(self.channel_layer.group_add)(self.room_name,self.channel_name)
        self.send({
            "type": "websocket.accept",
        })
        print(f'[{self.channel_name}] -  you are connected')

    

    def websocket_receive(self, event):
        print(f"[{self.channel_name}] - Recieved message - {event['text']}")
        async_to_sync(self.channel_layer.group_send)(self.room_name,
            {
                'type': 'websocket.message',
                'text': event['text']
            }
        )
        
    def websocket_message(self,event):
        print(f"[{self.channel_name}] - Message sent - {event['text']}")
        self.send({
            "type": "websocket.send",
            "text": event["text"],
        })
        

    def websocket_disconnect(self,event):
        async_to_sync(self.channel_layer.group_discard)(self.room_name,self.channel_name)
        print('websocket is disconnected')