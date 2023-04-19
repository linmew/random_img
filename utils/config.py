from typing import List

from pydantic import BaseModel


#class ChatConfig(BaseModel):
     #ecy_lmt: int = 5
     #ys_lmt: int = 5

def get_message_id(event):
    if event.message_type == 'private':
        return event.user_id
    elif event.message_type == 'group':
        return event.group_id
    elif event.message_type == 'guild':
        return event.channel_id

#config_manager = ChatConfig()
