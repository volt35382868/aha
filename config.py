from sample_config import Config
class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 29065853
    API_HASH = "777aac491624cce8ea86ec0a693a66de"
    # the name to display in your alive message
    ALIVE_NAME = "BiLaL"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgresql://myuser:mypassword@localhost:5432/mydatabase"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    STRING_SESSION = "1BJWap1sAUGeGgxO1oBLb6aWhgSZGmfZrDNQyfSsfjccdozvPNWjxqh-C0-QsOrlfBEkxDKcS-tiv0hsYgqW4_ACZrH6QAzI0GjSJlV5FleA9bmO8rE_uZFsLCJc9dyerBmzNwB7nvZ1kjHbBLMRI4ED5znb754bugAD5r6sI8g-j_BzhRkCy8e3ku3xNaEes0j4n5auVnlxHx7lY7iGMTRkwqZyCR18shuxvSIlnUWQHELNxqRnXpXjTEAwBPacN71gxHj8Glhr24zwwMwNYTiyaw9je8MS6xcGRfikoA25rKKgBRbQ4tbT0hbZC97y_isJ_sOGW3E_f5KSHgy0r_gABUeUUkWQ="
    # create a new bot in @botfather and fill the following vales with bottoken and username respectively
    TG_BOT_TOKEN = "7547847917:AAHUtlbaGSs6NOV1MQTZ0tKw4dLhKu4sB_c"
    # command handler
    COMMAND_HAND_LER = "."
    # sudo enter the id of sudo users userid's in that array
    SUDO_USERS = []
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
