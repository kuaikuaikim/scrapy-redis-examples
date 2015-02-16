scrapy-redis-examples
==============

A scrapy project integrated with redis. we can use redis to do many things during scrapy work.  
**Rember dont use it to do anything illegal!**

####Usage
    sudo apt-get install scrapy-0.2x
    sudo apt-get install redis-server 
    sudo apt-get update  
    git clone ...
    
    #better use scrapy shell before craw
    scrapy shell http://specify_address/xxx.html
    
    cd scrapy-redis-examples/hrtencent & scrapy crawl hrtencent  
Finally you can see result files in the storage folder

####New Features
1.Rembere the scrapy crawled status. Make sure every page we just craw once.  
2.Improve the scrapy performance. It works faster with redis. I rewrite some core module spider logic to the redis.  
3.Ouput scrapy results with distributed small files.Avoid losing all results during craw pages when been interrupted.  
4.automatically downloading page images  

==============
一个scrapy集成redis的实例。我们可以用redis辅助scrapy很多功能模块，例如过滤，存储，性能。

####新特性
1.记住爬虫状态，确保每个页面只抓取一次。  
2.提高了scrapy爬虫性能，本人利用redis重写了scrapy的核心模块。   
3.爬虫结果分成多个小文件,防止程序中断丢失爬虫结果。  
4.自动下载页面图片  
