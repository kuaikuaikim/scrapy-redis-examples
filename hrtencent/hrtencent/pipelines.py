# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals


import json
import codecs
import os

class JsonWithEncodingPipeline(object):

    def __init__(self):
    	self.f_num = 1;
    	self.file_name = self.get_file_name()
        self.file = codecs.open(self.file_name, 'w', encoding='utf-8')

    def process_item(self, item, spider):
    	if os.path.getsize(self.file_name) > 10485760:
    		self.file.close()
    		self.f_num = self.f_num + 1
    		self.file_name = self.get_file_name()
    		self.file = codecs.open(self.file_name, 'w', encoding='utf-8')

        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
    
    def get_file_name(self):
    	return 'storage/'+'data_utf8_' + str(self.f_num) + '.json'

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item