from flask import Flask

app = Flask(__name__)
redisDB = Redis(host=os.getenv('HOST'), port=os.getenv('PORT'))

@app.route('/')
def welcomeToKodeKloud();
  redisDB.incr('visitorCount')
  visitCount = str(redisDB.get('visitorCount', 'utf-8')
  return "Welcome to KODEKLOUD!"

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
