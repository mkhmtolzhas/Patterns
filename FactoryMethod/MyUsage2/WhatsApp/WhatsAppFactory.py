from ChatFactory import ChatFactory
from Chat import Chat
from WhatsApp.WhatsApp import WhatsApp

class WhatsAppFactory(ChatFactory):
    def create_chat(self) -> Chat:
        return WhatsApp()
        