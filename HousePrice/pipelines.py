# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import copy

import pymysql
from scrapy import log
from twisted.enterprise import adbapi


class HousepricePipeline(object):
    def __init__(self):
        dbparms = dict(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='first',
            use_unicode=True,
        )
        self.post = adbapi.ConnectionPool('pymysql', **dbparms)

    def process_item(self, item, spider):
        houseitem = copy.deepcopy(item)
        query = self.post.runInteraction(self._conditional_insert, houseitem)
        return item

    def _conditional_insert(self, tb, item):
        print("11111111111111111111111111111111111111111111111111111111111111")
        sql = "insert into house(xiaoqu ,louceng,, price, avg_price) values (%s,%s,%s,%s)"
        print("2222222222222222222222222222222222222222222222222222222222222222222")
        parms = (item['xiaoqu'], item['louceng'], item['price'], item['avg_price'])
        print("3333333333333333333333333333333333333333333333333333333333333333")
        tb.execute(sql, parms)
        print("4444444444444444444444444444444444444444444444444444444444444444444")

    def handle_error(self, e):
        log.error(e)

    #
    # def process_item(self, item, spider):
    #     return item
