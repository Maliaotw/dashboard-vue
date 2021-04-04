
import logging
import telegram
import re
from time import sleep
from datetime import timedelta

from django.conf import settings
from web.app import models


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def push():


    # 選擇發送bot
    telegram_obj = telegram.bot.Bot(token=settings.TELEGRAM_BOT_TOKEN)

    # # 選擇發送MailUser
    # email_admin = models.EmailMaster.objects.filter(user=conf.EMAILUSER['user'])
    #
    # if email_admin:
    #     email_admin = email_admin.first()
    # else:
    #     email_admin = models.EmailMaster.objects.create(**conf.EMAILUSER)
    #
    #

    # 有綁定的使用者
    activate_user = models.Telegram.objects.filter(status=True)

    logger.info(activate_user)

    push_news = models.PushNews.objects.all()

    for news in push_news:

        logger.info(news)

        # Source 訂閱者
        logger.info(news.source.userprofile_set.all())

        # 有綁定的訂閱者
        sub_user = news.source.userprofile_set.all()
        tg_sub_user = sub_user.filter(telegram__in=activate_user)


        logger.info(sub_user)


        h8 = timedelta(hours=8)
        txt = ["標題:\n%s" % news.name,
               "發佈時間:%s" % (news.publish+h8).strftime("%Y-%m-%d %H:%M:%S"),
               "標籤:%s" % [],
               "來源:%s" % news.source,
               "內文:\n%s" % re.sub(r'</?\w+[^>]*>', '', news.content[0:150]),
               "連結:\n%s" % news.url
               ]

        tg_text = "\n".join(txt)

        etxt = ["標題:\n%s" % news.name,
               "發佈時間:%s" % (news.publish+h8).strftime("%Y-%m-%d %H:%M:%S"),
               "標籤:%s" % [],
               "來源:%s" % news.source,
               "內文:\n%s" % news.content,
               "連結:\n%s" % news.url
               ]

        email_text = "\n".join(etxt)

        # 給各路訂閱者發送TG
        logger.info(tg_sub_user)
        for user in tg_sub_user:
            userid = user.telegram.chat_id
            logger.info(userid)
            # bot = telegram.Bot(token=tg_admin.token)
            telegram_obj.sendMessage(chat_id=userid, text=tg_text)
            sleep(30)

        # 訂閱者電子郵件
        logger.info(sub_user)
        toaddrs = list(filter(None, [user.user.email for user in sub_user]))
        logger.info(toaddrs)

        # if toaddrs:
        #     smtp = smtphelper(host=email_admin.host, port=email_admin.port, user=email_admin.user, pwd=email_admin.passwd)
        #     smtp.smtp_sendhtml(news.name,email_text,toaddrs=toaddrs)



        # 刪除這筆資料
        news.delete()
