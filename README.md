scrapy-redis-examples
==============

A scrapy project integrated with redis. we can use redis to do many things during scrapy work.  
**Rember dont use it to do anything illegal!**

####Usage
    apt-get update  
    sudo apt-get install redis-server  
    git clone ...  
    cd scrapy-redis-examples & scrapy crawl hrtencent  
Finally you can see result files in the storage folder

####New Features
1.Rembere the scrapy crawled status. Make sure every page we just craw once.  
2.Improve the scrapy performance. It works faster with redis. I rewrite some core module spider logic to the redis.  
3.Ouput scrapy results with distributed small files.Avoid losing all results during craw pages when been interrupted.



