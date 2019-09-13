# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# Extracted data --> Item containers  --> Storing as json / csv files
# Extracted data --> Item containers  --> Pipeline --> SQL/Mongo database

class QuotetutorialPipeline(object):
    def process_item(self, item, spider):

        print("Pipeline :" + item['title'][0])
        return item
