# note to me; stevie virtualenv local, steviebot server
import os, random, linecache
from dotenv import load_dotenv
load_dotenv('SECRETS.ENV')
import twitter

api = twitter.Api(consumer_key=os.environ.get('consumer_key'),
                  consumer_secret=os.environ.get('consumer_secret'),
                  access_token_key=os.environ.get('access_token'),
                  access_token_secret=os.environ.get('access_token_secret')
                 )

pathToCountCache = os.environ.get('path')
if !pathToCountCache:
    pathToCountCache = './'

totalLines = 0
with open(pathToCountCache + './cache.txt', 'r') as cache:
    totalLines = int(cache.read())

line = linecache.getline('./parsedlyrics.csv', random.randrange(0, totalLines))

if isinstance(line, str) == True and line != '':
    line = "\"" + line.strip('\n') + "\""

    #status = api.PostUpdate(line)
    print(line)
