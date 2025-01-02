BOT_NAME = "quotes_crawler"

SPIDER_MODULES = ["quotes_crawler.spiders"]
NEWSPIDER_MODULE = "quotes_crawler.spiders"

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    'quotes_crawler.pipelines.DatabasePipeline': 1,
}

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
