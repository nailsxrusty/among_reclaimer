import random
import discord

list_a = ["Captain", "1st Salvage Turret", "Box Handler", "2nd Salvage Turret", "Manned Turret",
          "1st Remote Turret Gunner", "2nd Remote Turret Gunner", "Pilot", "Co-Pilot"]

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
	print("The bot is ready!")

@client.event
async def on_message(message):
	print(f"Received message from {message.author}: {message.content}")
	if message.content.startswith("!ping"):
		if message.channel.permissions_for(message.guild.me).send_messages:
			await message.channel.send("Pong!")
		else:
			await message.author.send("Pong!")

	if message.content.startswith("!assign_positions"):
		if message.channel.permissions_for(message.guild.me).send_messages:
			users = []
			for mention in message.mentions:
				user = message.guild.get_member(mention.id)
				if user is not None:
					users.append(user)
				else:
					await message.channel.send(f"User with ID {mention.id} not found in this server.")
			if users:
				infiltrator = random.choice(users)
				for i, user in enumerate(users):
					msg = "Your position on the ship is: " + list_a[i]
					if user == infiltrator:
						msg += "\nYou ARE the infiltrator!"
					try:
						await user.send(msg)
					except discord.Forbidden:
						await message.channel.send(f"Could not send DM to {user}. They may have DMs disabled.")
			else:
				await message.channel.send("No users found to assign positions to.")
		else:
			await message.channel.send("I do not have permission to send messages in this channel.")

client.run("INSERT TOKEN HERE")
