from flask import Flask, request
from models import background

import redis
from rq import Queue

app = Flask(__name__)

r = redis.Redis(host='redis-server', port=6379)
q = Queue(connection=r)

@app.route('/start')
def start():
    spider_name  = request.args.get('spider_name', None) #PARAMETER 1: spider_name
    url  = request.args.get('url', None)                 #PARAMETER 2: url
    
    job = q.enqueue(background, args=(spider_name, url))
    return f"Task queued {job.id}, {len(q)} number of tasks left in queue"
    
    #target = background(spider_name, url)
    #return requests.get(target).json()

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0',port=8001)