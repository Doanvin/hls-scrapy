# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2


class HooklinesinkerPipeline(object):
    def open_spider(self, spider):
        hostname = 'localhost'
        username = '' # your username
        password = '' # your password
        database = 'reports' # your database
        port = 5432
        try:
            self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port)
        except psycopg2.Error as e:
            print(e.pgerror)
            
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute("insert into reports(name, site, date, date_exp, type, rating, report, access) values(%s,%s,%s,%s,%s,%s,%s,%s)",(item['name'],item['site'],item['date'],item['date_exp'],item['type'],item['rating'],item['report'],item['access']))
        self.connection.commit()
        return item