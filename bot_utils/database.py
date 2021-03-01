from firebase import Firebase

from hata import Embed

from .tools import EXECUTOR
from .shared_data import BOT_LOGS
import config

class My_Database:
    
    FIREBASE = None
    DATABASE = None
#    STORAGE = None

#    NOT READY
#    @classmethod
#    async def connect_storage(cls):
#        '''Starts a connection to firebase'''
#        cls.STORAGE = cls.FIREBASE.storage()
    
    @classmethod
    async def connect_database(cls):
        '''Starts a connection to the database'''
        cls.DATABASE = cls.FIREBASE.database()
        print('Connected to database')
    
    @classmethod
    async def setup_firebase(cls, database_config):
        '''Starts a connection to firebase'''
        cls.FIREBASE = Firebase(database_config)
        print('Connected to firebase')
        
        if cls.DATABASE is None:
            await cls.connect_database()

#        NOT READY
#        if cls.STORAGE is None:
#            await cls.connect_storage()
#print(type(My_Database.FIREBASE))

async def store_guild_data(client, guild):
    """
    This function stores the guild data
    
    first it stores the prefixes if they do not exist
    second they stores the member data if the data does not exist
    """
    DATABASE = My_Database.DATABASE
    
    embed = Embed(title = "Database Status", description = 'Storing Every Data')
    message = await client.message_create(BOT_LOGS, embed)
    
    #For the prefix
    with client.keep_typing(BOT_LOGS):
        has_bot_data = bool(await EXECUTOR(client, DATABASE.child('MelonMintBots').get().val))
        if has_bot_data is None:
            
            bot_data = {
                config.MINT_ID:{'prefix':config.MINT_PREFIX},
                config.MELON_ID:{'prefix':config.MELON_PREFIX},
                config.MELON_MINT_ID:{'prefix':config.MELON_MINT_PREFIX}
            }
            
            await EXECUTOR(client, DATABASE.child('MelonMintBots').set(bot_data).update)
            value_msg = f"Set to {f'<@{id}> is set to {prefix}' for id, prefix in bot_data.items()}"
        else:
            value_msg = "Prefix Unchanged"
    
    await client.message_edit(message, embed.add_field(name = "Prefix Status", value = value_msg))
    
    #For Users
    with client.keep_typing(BOT_LOGS):
        new_count = 0
        update_count = 0
        
        guild_users = message.guild.users.copy().values()
        member_list = await EXECUTOR(client, DATABASE.child('members').shallow(). get().val)
        
        for user in guild_users:
            if user.is_bot:
                continue
            user_data = user.guild_profiles.get(guild)
                        
            if member_list is None or str(user.id) not in member_list: #just do it
                new_data = {
                    'joined_at':[str(user_data.joined_at)],
                    'left_at': [],
                    'name':[user.name],
                    'level':0,
                    'reputation':0,
                    'todo':[],
                    'roles': [x.id for x in user_data.roles] if user_data.roles else [] 
                    }
                new_count += 1
            
            else: #update stuff
                new_data = await EXECUTOR(client, DATABASE.child('members').child(str(user.id)).get().val)
                    
                new_data['joined_at'].append(str(user_data.joined_at))
                new_data['name'].append(user.name)
                
                if new_data.get('roles'):
                    new_data['roles'].extend([x.id for x in user_data.roles] if user_data.roles else [])
                else:
                    new_data['roles'] = [x.id for x in user_data.roles] if user_data.roles else []
                
                for value in ['joined_at','name','roles']:
                    list(set(new_data[value]))
                                
                update_count += 1
            print(f'Added {new_count}/{len(guild.users)}\nUpdated {update_count}/{len(guild.users)}')
            await EXECUTOR(client, DATABASE.child('members').child(str(user.id)).set(new_data).update)
        embed = embed.add_field(name = "Member Status", value = f'Added {new_count}/{len(guild.users)}\nUpdated {update_count}/{len(guild.users)}')
        await client.message_edit(message, embed)
        await client.message_create(message.channel, 'done')