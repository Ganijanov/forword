from telethon.tl.types import Message
from telethon.sync import TelegramClient, events
from telethon.tl.types import InputMessagesFilterEmpty, InputMessagesFilterDocument
import datetime

# Установите свои значения api_id и api_hash
api_id = 20456561
api_hash = 'ed699ba471787e4ea7b5c08845a5842e'
bot_token = '6503671456:AAFmA-0h2PXeVIgt-wYtQqty-RGPa2m4USU'


# Установите ваш токен бота и идентификатор целевой группыx
target_group_id = 2137942298



# Define your keywords
keywords = ['Odam bor ', 'одам бор', 'pochta bor', 'почта бор', 'kiwi bor', 'kshi bor ', 'кши бор', ' ketamiz ', 'кетамиз', 'bagajli mashina kerak', 'mashina kerak', 'mawina kerak', 'mashina bormi', ' moshina kerak', ' moshina qerak', 'ketamz', 'kishi', 'kiwi', 'кши', 'почта', 'pochta', 'одам', 'Odam', 'avto keratk', 'авто кере', 'мошина кере', 'машина керак', 'ketamz', 'кетамз']  # Add your keywords here



client = TelegramClient('session_name', api_id, api_hash)
@client.on(events.NewMessage)
async def forward_message(event):
    message = event.message
    # Check if the message contains any of the keywords
    if any(keyword in message.text.lower() for keyword in keywords):
        # Prepare the forwarded message
        try:
            forwarded_message = f"👤 Отправитель: {message.sender.first_name}\n@{message.sender.username}\n📌 Группа: {message.chat.title}\n🔗 Ссылка на сообщение: https://t.me/c/{message.peer_id.channel_id}/{message.id}\n📝 Текст сообщения: {message.text}"
            try:
                await client.forward_messages(target_group_id, message)
                await client.send_message(target_group_id, forwarded_message)
            except:
                await client.send_message(target_group_id, forwarded_message)
        except:
            pass
        # Forward the message to the target group

# Start the Telegram client
with client:
    # Run the client until it's disconnected
    client.run_until_disconnected()

def send():
    client.send_message(target_group_id, 'Tolov esdan chiqmasin server tohtashiga 1 kun qoldi')


def main():
    today = datetime.date.today()
    if today.day == 10:
        send()


if '__name__' == '__main__':
    main()