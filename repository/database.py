from databases import Database

from config.config import config

database = Database(config.DATABASE_URL)
