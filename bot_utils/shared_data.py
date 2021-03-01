from hata import Guild, ChannelText, ChannelVoice, Role

import config

#Bots
RAN_FROM = config.RAN_FROM
SEND_LOG = False

MINT_PREFIX = config.MINT_PREFIX
MELON_PREFIX = config.MELON_PREFIX
MELON_MINT_PREFIX = config.MELON_MINT_PREFIX

INVITE = 'https://discord.com/api/oauth2/authorize?client_id={BOT_ID}&permissions=2147483639&scope=bot'
SLASH = 'https://discord.com/oauth2/authorize?client_id={BOT_ID}&scope=applications.commands+bot'

#Colors
BLUE = 0x1489B0
RED = 0xBC2E25
GREEN = None

#Guild
NIHONGO_QUEST = Guild.precreate(709105396656111676)

#Channel
MEMBER_COUNT = ChannelVoice.precreate(809262218763304960)

ANNOUNCEMENT_CHANNEL = ChannelText.precreate(717045980981362799)
WELCOME_N_RULES_CHANNEL = ChannelText.precreate(811966741659648050)
ROLES_CHANNEL = ChannelText.precreate(809264280759042069)
NAVIGATION_CHANNEL = ChannelText.precreate(809281727184240682)
SUGGESTION_CHANNEL = ChannelText.precreate(809262950971473930)
SERVER_CHANNEL = ChannelText.precreate(763204369221943337)

INTRO_CHANNEL = ChannelText.precreate(717214286988050443)
OFF_TOPIC_CHANNEL = ChannelText.precreate(717211320881250336)
GENERAL_CHANNEL = ChannelText.precreate(809349050091569152)
BOT_CMDS_CHANNEL = ChannelText.precreate(809269896554348604)


#Bot related channels
BOT_LOGS = ChannelText.precreate(811036715992612864)
DM_BOT_SUPPORT = ChannelText.precreate(811036609809612830)

#Roles
MOD_ROLE = Role.precreate(716309172756414464)
MUTED_ROLE = Role.precreate(809443793413603409)
ALPHA_ROLE = Role.precreate(745297481310404640)

#To be choosen roles
FREE_ROLES = {
    'ANNOUNCEMENT':Role.precreate(809791647117475840),
    'BUMPERS':Role.precreate(813834732600164383),
    'JAPANESE':Role.precreate(716717701070061619),
    'N5':Role.precreate(716719435481874555),
    'N4':Role.precreate(716719433619472424),
    'N3':Role.precreate(716719423024791682),
    'N2':Role.precreate(716717997791772845),
    'N1':Role.precreate(716717949968449586),
    'MELIONS':Role.precreate(813954482580226048),
    'POLLS':Role.precreate(813834065366876161),
    'UNIMPORTANT':Role.precreate(813977455119171594),
    'HE':Role.precreate(813836231275184128),
    'SHE':Role.precreate(813836433264607303),
    }

#Rules
SERVER_RULES = {
    "1":"Please follow [discord's term of use](https://discord.com/terms)",
    "2":"Be Nice and have fun let's be an encouraging server.",
    "3":"Do not post anything illegal or any ip grabber links.",
    "4":"Please do not disclose your personal information to anyone.",
    "5":"This server is a SFW server. Please avoid posting NSFW content.",
    "6":"No spamming or anything if the mods told you to stop please stop.",
    "7":"Please respect others at all times. Harassment, dogpiling, etc. are not cool.",
    "8":"If someone is messaging you things you do not like please report it to the mods.",
    "9":"Please avoid potentionally offensive conversation, such as politics, racism and religion.",
    "10":("Be humble. Our server is built up of people regardless of their level."
        "If you notice someone is new please help them"),
    "11":"Please use the correct the channel according to their topic"
    }

#Nihongo Quest Links
LINKS = {
    'WEBSITE':'https://nihongoquest.com',
    'TIKTOK':'https://www.tiktok.com/@nihongo.quest.dev',
    'FACEBOOK':'https://facebook.com/NihongoQuest/',
    'TWITTER':'https://twitter.com/bailey_eng',
    'INSTAGRAM':'https://www.instagram.com/nihongoquestgame/',
    'ITCH':'https://itch.io',
    'DISCORD':'https://discord.gg/B5WXZdj',
    }
