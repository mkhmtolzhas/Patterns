from ChatFactory import ChatFactory
from WhatsApp.WhatsAppFactory import WhatsAppFactory

def send_message(chat_factory: ChatFactory):
    return chat_factory.send_message(user_id="23B031118", message="I love more Amina")

if __name__ == "__main__":
    print(send_message(WhatsAppFactory()))