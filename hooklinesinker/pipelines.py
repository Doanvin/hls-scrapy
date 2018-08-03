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
        database = '' # your database
        port = 5432
        try:
            self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port)
            self.cur = self.connection.cursor()
        except psycopg2.Error as e:
            print(e.pgerror)

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        item = self.normalize_data(item)
        in_db = self.checkDuplicates(item)
        if not in_db:
            self.cur.execute("insert into reports(name, site, date, date_exp, type, rating, gps, report, access) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);",(item['name'],item['site'],item['date'],item['date_exp'],item['type'],item['rating'],item['gps'],item['report'],item['access']))
            self.connection.commit()
            return item
        elif in_db:
            return item
        else:
            print('Error checking for item in database')
            return item

    def normalize_data(self, item):
        # change site
        if item['site'] == 'Rancho Cordo...':
            item['site'] = 'Rancho Cordova'
        if item['site'] == 'Grand Juncti...':
            item['site'] = 'Grand Junction'
        if item['site'] == 'Colorado Spr...':
            item['site'] = 'Colorado Springs'
        if item['site'] == 'KLamath Fall...':
            item['site'] = 'Klamath Falls'
        if item['site'] == 'Spokane Vall...':
            item['site'] = 'Spokane Valley'

        # relplace None type with empty string
        if item['report'] == None:
            item['report'] = ''
        if item['access'] == None:
            item['access'] = ''

        # replace /n with space in report and access
        if "\n" in item['report']:
            item['report'] = item['report'].replace("\n", " ")
        if "\n" in item['access']:
            item['access'] = item['access'].replace("\n", " ")

        # replace \xa0 with ''
        if "\xa0" in item['report']:
            item['report'] = item['report'].replace("\xa0", "")
        if "\xa0" in item['access']:
            item['access'] = item['access'].replace("\xa0", "")

        # change rating from None to 0 and '# stars' to '#'
        if item['rating'] == None:
            item['rating'] = 0
        elif item['rating'] == 'Star None':
            item['rating'] =  0
        elif len(item['rating']) > 5:
            item['rating'] = item['rating'][0]

        # change date_exp from empty None to empty string
        if item['date_exp'] == None:
            item['date_exp'] = ''
        return item

    def checkDuplicates(self, item):
        """Check database for duplicate entries"""
        # escape apostrophes before sql select query
        item = self.checkApostrophes(item)

        self.cur.execute("select name,site,date from reports where name = '{}' and site = '{}' and date = '{}';".format(item['name'], item['site'], item['date']))
        rows = self.cur.fetchall()

        if rows != None and len(rows) > 0:
            # no duplicates
            print('FOUND DUPLICATE IN DATABASE :(')
            return True
        
        elif len(rows) == 0:
            # found duplicate
            print('NOT A DUPLICATE ENTRY!!!')
            return False

        else:
            print('Error in checkdb! len(rows) not > 0 and len(rows) not == 0.')
            return True

    def checkApostrophes(self, item):
        """Check for apostrophes and escape them before sql select query"""
        if "'" in item['name']:
            item['name'] = item['name'].replace("'", "''")
        if "'" in item['site']:
            item['site'] = item['site'].replace("'", "''")
        return item