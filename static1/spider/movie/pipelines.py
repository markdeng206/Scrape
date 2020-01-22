# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import psycopg2
import simplejson as simplejson
from psycopg2._json import Json


class PgSQLPipeline():
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('PGSQL_HOST'),
            database=crawler.settings.get('PGSQL_DATABASE'),
            user=crawler.settings.get('PGSQL_USER'),
            password=crawler.settings.get('PGSQL_PASSWORD'),
            port=crawler.settings.get('PGSQL_PORT'),
        )

    def open_spider(self, spider):
        self.conn = psycopg2.connect(database=self.database,
                                     user=self.user,
                                     password=self.password,
                                     host=self.host,
                                     port=self.port)
        self.cursor = self.conn.cursor()
        sql = 'CREATE TABLE IF NOT EXISTS movie (' \
              'name varchar(50) NOT NULL, ' \
              'alias varchar(50), ' \
              'score float , ' \
              'rank integer, ' \
              'cover text, ' \
              'regions varchar(50)[], ' \
              'categories varchar(50)[], ' \
              'minute integer, ' \
              'published_at date, ' \
              'drama text, ' \
              'directors json, ' \
              'photos text [], ' \
              'actors json, ' \
              'PRIMARY KEY (name))'
        print('sql')
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()
        # self.cursor.c

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        sql = 'INSERT INTO movie (name, alias, score, rank, ' \
              'cover, regions, categories, minute, published_at, drama,' \
              'directors, actors, photos) values (%s, %s, %s,%s, %s,' \
              '%s, %s, %s, %s, %s, %s, %s, %s)'
        self.cursor.execute(sql, [
            item.get('name'),
            item.get('alias'),
            item.get('score'),
            item.get('rank'),
            item.get('cover'),
            item.get('regions'),
            item.get('categories'),
            item.get('minute'),
            item.get('published_at'),
            item.get('drama'),
            json.dumps(item.get('directors'), ensure_ascii=False),
            json.dumps(item.get('actors'), ensure_ascii=False),
            item.get('photos'),
        ])
        self.conn.commit()
        return item
