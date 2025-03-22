from Chat import Chat
from threading import Lock
from abc import ABCMeta


class WhatsAppMeta(ABCMeta):
    _instances = {}

    _lock: Lock = Lock()


    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class WhatsApp(Chat, metaclass=WhatsAppMeta):
    def send_message(
            self, 
            user_id, 
            message
        ) -> dict:
        return {
            user_id,
            message
        }