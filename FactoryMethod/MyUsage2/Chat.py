from abc import ABC, abstractmethod

class Chat(ABC):
    @abstractmethod
    def send_message(self, user_id: str, message: str) -> dict:
        pass
    