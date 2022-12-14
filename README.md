# Scrapyq

### Project goal:

Containerized, distributed asyc request handling daemon for scrapy spiders. This project combines `scrapyrt` with `redis` and aims to add periodic scheduling to scraping tasks.

1. Expose `scrapy` project to an endpoint using `scrapyrt` - ![#c5f015](https://via.placeholder.com/15/c5f015/c5f015.png) Complete
2. Create an external handler to handle scraping requests - ![#c5f015](https://via.placeholder.com/15/c5f015/c5f015.png) Complete
3. Queue async requests using `redis` and `rq` - ![#c5f015](https://via.placeholder.com/15/c5f015/c5f015.png) Complete
4. Replace `rq` with `celery` - ![#f03c15](https://via.placeholder.com/15/f03c15/f03c15.png) Pending
5. Add `mongodb` backend to dump outputs - ![#f03c15](https://via.placeholder.com/15/f03c15/f03c15.png) Pending
6. Add scheduler using `celery` - ![#f03c15](https://via.placeholder.com/15/f03c15/f03c15.png) Pending

### Architecture diagram:
![plot](./utils/Architecture.png)

### Stack: 
`docker`, `python3.9`, `scrapy`, `scrapyrt`, `flask`, `redis`, `rq`


### To build and run docker containers:
```
cd scrapyq
docker-compose build --no-cache
docker-compose up
```

Add your custom scrapy spiders to `scrapyq/project/project/spiders/` similar to `example.py`.

To test API, import the POSTMAN collection `utils/scrapyq.postman_collection.json`

**1. Start scraping:** 

```
http://127.0.0.1:8001/start?spider_name=example&url=https://www.example.com/

> Task queued 550de549-600f-4a9a-ae4d-4da15382d8c9, 0 number of tasks left in queue
```
Run this request multiple times via POSTMAN to queue requests in redis. 

Change the spider_name and url for custom spiders and different targets.

**2. Fetch status/result:**

```
http://127.0.0.1:8001/result?job_id=550de549-600f-4a9a-ae4d-4da15382d8c9

> [{'header': 'Example Domain', 'paragraphs': 'This domain is for use in illustrative examples in documents. You may use
this\n domain in literature without prior coordination or asking for permission.'}]
```
Replace the job_id with the ones that are recieved from the first API call(s).
