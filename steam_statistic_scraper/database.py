from peewee import *
from configparse import Config
databasetype = Config.get('database','type')


if databasetype == "SQLite":
	database = SqliteDatabase(Config.get('database','path'))
elif databasetype == "Mysql":
	databasename = Config.get('database', 'dbname')
	databaseuser = Config.get('database', 'user')
	database = MySQLDatabase(databasename,user=databaseuser)
elif databasetype == "Postgresql":
	database = PostgresqlDatabase()

def db_connect():
	database.connect()
def db_close():
	if not database.is_closed():
		database.close()
def create_tables():
	db_connect()
	database.create_tables([UserLoggedIn,GameUser], safe=True)
	db_close()

class BaseModel(Model):
	class Meta:
		database = database


class UserLoggedIn(BaseModel):
	time = DateTimeField(primary_key=True)
	userloggedin = IntegerField(null=False)


class GameUser(BaseModel):
	time = DateTimeField(null=False)
	currentuserloggedin = IntegerField(null=False)
	dayhighuserloggedin = IntegerField(null=False)
	gamename = CharField(null=False)

create_tables()
