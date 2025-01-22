import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7251156860:AAErl8y868jQS7c-r0sjMCkJdJDhNh07_mQ")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20607064"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "c0a09fd762681a66366cf84976f31a17")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://heroku:heroku@cluster0.wamwxpr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
