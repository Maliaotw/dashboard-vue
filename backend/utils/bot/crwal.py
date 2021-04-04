#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename : rss_to_db
# @Date     : 2018/7/24
# @Author   : Maliao
# @Link     : None

import logging
import feedparser
import pandas as pd
import re
import hashlib
from pandas.tseries.offsets import *

from utils.common import imgur, watermark
from web.app import models
from django.conf import settings
import os

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

image_path = os.path.join(settings.ROOT_DIR, 'files', 'image')


def crawl_rss():
    source_obj = models.Source.objects.filter(status=True)
    logger.info(source_obj)

    new_list = []

    for source in source_obj:
        # print(source.url)  # http://feeds.feedburner.com/engadget/cstb
        logger.info(source.url)
        logger.info(source.name)

        d = feedparser.parse(source.url)

        logger.info(d)

        # 判斷網址如果失效
        if d.entries:

            for post in d.entries:

                if not post.get('summary'):
                    continue

                if post.get('tags'):
                    t = [t['term'] for t in post.tags]
                else:
                    t = []

                # 正則解出縮圖URL
                thumbnail_obj = re.findall(r'((http(s?):)([/|.|\w|\s|-])*.(?:jpg|gif|png))', post.get('summary', ''))
                if thumbnail_obj:
                    thumbnail = thumbnail_obj[0][0]
                else:

                    name = source.name

                    # MD5
                    m = hashlib.md5()
                    m.update(name.encode("utf-8"))
                    h = m.hexdigest()
                    # print(h)

                    filename = os.path.join(image_path, "%s.jpg" % h)
                    # path = r"../statics/images/%s" % filename

                    # 檔案是否存在
                    if source.thumbnail:
                        thumbnail = source.thumbnail
                    else:
                        print(name, "創建檔案")
                        watermark.str2img(txt=name, path=filename)
                        thumbnail_link = imgur.push_imgur(filename)
                        source.thumbnail = thumbnail_link
                        source.save()

                        thumbnail = thumbnail_link

                data = {
                    'source': source,
                    'name': post.get('title'),
                    'url': post.get('feedburner_origlink') if post.get('feedburner_origlink') else post.link,
                    'publish': post.get('published', ''),
                    'content': post.get('summary', '') if post.get('summary', '') else '',
                    'tag': t,
                    'thumbnail': thumbnail,
                }
                new_list.append(data)


        else:
            pass  # 不返回資料

    return new_list


def insert_db(data):
    df = pd.DataFrame(data)

    df['publish'] = pd.to_datetime(df['publish'])
    df['publish'] = df['publish'] + DateOffset(hours=8)

    new_list = df.to_dict('records')
    logger.debug(new_list)

    for i in new_list:

        logger.debug(i)
        logger.debug(i['url'])

        tag_list = []
        tag_str = str(i['tag'])

        if i['tag']:
            for t in i['tag']:
                if models.Tag.objects.filter(name=t):
                    tag_obj = models.Tag.objects.filter(name=t)[0]
                    tag_list.append(tag_obj)
                else:
                    tag_obj = models.Tag.objects.create(name=t)
                    tag_list.append(tag_obj)

        if models.News.objects.filter(url=i['url']).filter(publish=i['publish']):
            # if not models.PushNews.objects.filter(url=i['url']):
            #     models.PushNews.objects.create(name=i['name'], url=i['url'], content=i['content'], publish=i['publish'],
            #                                    source=i['source'], tag=tag_str)
            pass

            # Existing_list.append(i)
        else:

            del i['tag']

            news_obj = models.News.objects.create(**i)
            # print(tag_list)
            for loop_tag in tag_list:
                news_obj.tag.add(loop_tag)
            news_obj.save()
            models.PushNews.objects.create(name=i['name'], url=i['url'], content=i['content'], publish=i['publish'],
                                           source=i['source'], tag=tag_str)


def crawl():
    data = crawl_rss()
    if data:
        insert_db(data)


if __name__ == '__main__':
    crawl()
