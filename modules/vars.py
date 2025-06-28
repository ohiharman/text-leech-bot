import os

API_ID    = os.environ.get("API_ID", "27680167")
API_HASH  = os.environ.get("API_HASH", "90b8bad42e6210d0e1e04a858e045f55")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8090621972:AAE3Kj9FdD7KXBz8r_M2aa8ZRaKnLG_QfJ0") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
