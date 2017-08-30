# bot.py
# The main bot
# Misha Larionov

# Import dependencies
# PyCharm complains that PEP8 hates one-liner imports
import time
import cfg
import sqlite3

# More dependencies (need to be installed)
import asyncio
import discord

# Initialize the Discord client
client = discord.Client()

# Start the sqlite database
db = sqlite3.connect('database.sqlite')
cursor = db.cursor()

# Test purposes only // TODO: Remove
cursor.execute('''
DROP TABLE test
''')
# End testing code

cursor.execute('''
CREATE TABLE IF NOT EXISTS test (
  team_id integer PRIMARY KEY UNIQUE,
  team_owner integer NOT NULL,
  team_member_1 integer,
  team_member_2 integer,
  team_member_3 integer
);
''')

# cursor.execute('''
# INSERT INTO test VALUES (
#   1,
#   500,
#   501,
#   502,
#   NULL
# );
# ''')
#
# db.commit()

# cursor.execute('''
# SELECT team_owner, team_members FROM test WHERE team_id = 1;''')
#
# data = cursor.fetchall()
#
# for item in data:
#     print(item)


# This function fires whenever a message is sent in a channel where the bot can view messages
@client.event
@asyncio.coroutine
def on_message(message):

    # This line is purely for debug output and not really required
    print(time.strftime("%Y-%m-%d %H:%M:%S") + ": " + message.author.name + " says: " + message.content)

    # Make sure the author isn't a bot (Avoids two bots creating a feedback loop)
    if message.author.bot:
        return

    # Make variables so I can type less
    content = message.content
    author = message.author

    # Command handling goes here


# This function fires when the client first connects to Discord
@client.event
@asyncio.coroutine
def on_ready():
    print(time.strftime("%Y-%m-%d %H:%M:%S") + ': Connected to Discord')

# Run the client once all the setup is finished
client.run(cfg.TOKEN)

# db.close()
