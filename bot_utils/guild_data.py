from hata import Guild, ChannelText, Role

#Guild
NIHONGO_QUEST = Guild.precreate(709105396656111676)

#Channel
WELCOME_CHANNEL = ChannelText.precreate(809349050091569152)

#Roles
MUTED = Role.precreate(809443793413603409)

#To be choosen roles
FREE_ROLES = {
    'ANNOUNCEMENT':Role.precreate(809791647117475840),
    'JAPANESE':Role.precreate(716717701070061619),
    'N5':Role.precreate(716719435481874555),
    'N4':Role.precreate(716719433619472424),
    'N3':Role.precreate(716719423024791682),
    'N2':Role.precreate(716717997791772845),
    'N1':Role.precreate(716717949968449586)
    }

#Rules
SERVER_RULES = {
    "1":"Please follow [discord's term of use]()",
    "2":"Be Nice and have fun let's be an encouraging server.",
    "3":"Do not post anything illegal or any ip grabber links.",
    "4":"Please do not disclose your personal information to anyone.",
    "5":"This server is a SFW server. Please avoid posting NSFW content.",
    "6":"No spamming or anything if the mods told you to stop please stop.",
    "7":"Please respect others at all times. Harassment, dogpiling, etc. are not cool.",
    "8":"If someone is messaging you things you do not like please report it to the mods.",
    "9":"Please avoid potentionally offensive conversationm, such as politics, racism and religion.",
    "10":"Be humble. Our server is built up of people regardless of their level. If you notice someone is new please help them"
    }