import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Get bot token from environment variable (Render settings)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("⚠️ TELEGRAM_BOT_TOKEN is not set in Render environment variables.")

# Start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("👋 Hello! Send me a movie name and I'll fetch the link.")

# Handle movie name text
def handle_message(update: Update, context: CallbackContext):
    movie_name = update.message.text
    # TODO: Replace with scraping later
    fake_link = f"https://example.com/download/{movie_name.replace(' ', '_')}"
    update.message.reply_text(f"🎬 You searched for: {movie_name}\n🔗 Link: {fake_link}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    print("✅ Bot started...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
