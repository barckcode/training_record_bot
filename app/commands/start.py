from telegram.update import Update
from telegram.ext import CommandHandler, CallbackContext


# Command
def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    context.bot.send_message(
        chat_id=chat_id,
        text=f"🤖 Bienvenido {update.effective_chat.first_name} \n\n🤖 Soy TrainingRecord, el bot que te ayudará a llevar un registro de tus entrenamientos.\n🧐 Si necesitas saber de qué soy capaz visita a esta página web: (Próximamente estará disponible)",
    )


    message = context.bot.send_message(
        chat_id=chat_id,
        text=f"😜 Este es tú ID: {update.effective_chat.id} \n\n🦾 Lo necesitarás poder recibir los registros de tus entrenamientos. No te preocupes voy a crear un pin de este mensaje en el chat para que lo tengas siempre a mano.",
    )


    context.bot.pin_chat_message(
        chat_id=chat_id,
        message_id=message.message_id
    )


start_command = CommandHandler('start', start)
