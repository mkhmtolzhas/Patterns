from abc import ABC, abstractmethod
from Chat import Chat

class ChatFactory(ABC):
    @abstractmethod
    def create_chat(self) -> Chat:
        pass

    def send_message(self, user_id: str, message: str) -> dict:
        return self.create_chat().send_message(user_id=user_id, message=message)

    