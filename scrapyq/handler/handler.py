from multiprocessing import connection
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


def results(jobid):
    return str(q.fetch_job(jobid))

@app.route('/result')
def get_result():
    job_id  = request.args.get('job_id', None)
    job = q.fetch_job(job_id)

    if job.is_finished:
        ret = job.return_value['items']
    elif job.is_queued:
        ret = {'status':'in-queue'}
    elif job.is_started:
        ret = {'status':'waiting'}
    elif job.is_failed:
        ret = {'status': 'failed'}
    return str(ret)


if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0',port=8001)