import requests
import time

def background(spider_name, url):
    time.sleep(4)
    target = 'http://scrapyrt:9080/crawl.json?spider_name='+spider_name+'&'+'url='+url
    return requests.get(target).json()

    #return 'http://scrapyrt:9080/crawl.json?spider_name='+spider_name+'&'+'url='+url