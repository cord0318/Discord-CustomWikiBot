BOT_TOKEN = "" # Bot Token
OWNER_ID = [761779146434805770] # List Type
PREFIX = "*"

from os import listdir

EXTENSION_LIST = []
for i in listdir("./src/extensions"):
    if i.endswith(".py"):
        EXTENSION_LIST.append("extensions." + i.replace(".py", ""))