from redit import Redis

redisDB = Redis(host=os.getenv('HOST'), port=os.getenv('PORT'))

redistDB.set('visitorCount', 0)
