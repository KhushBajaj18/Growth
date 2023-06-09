import discord

# Enter your Discord bot token below
TOKEN = "MTExNTY5MjA1NzIwNjQ2NDYwMg.Gbdff6.F_BEx5THuyUhtm5qt52O-MOQ1GXlf0Ikson6C4"

# Create a Discord client
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    # Once the client is logged in, get the guild object for the specified guild ID
    guild_id = "1115695112383631411"
    guild = client.get_guild(int(guild_id))
    if guild is None:
        print("The guild does not exist.")
        await client.close()
        return

    # Get the total member count for the guild
    member_count = guild.member_count

    # Print the total member count
    print(f"The total member count for the server is {member_count}")

    # Close the Discord client
    await client.close()

# Run the client
client.run(TOKEN)
