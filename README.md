# WebCrawler

### Prerequisite
- Python 3
- Anaconda
  - Scrapy (a python library for crawling)

### BrickSetSpider

This program is following a tutorial as a "Hello World" program into the world of web crawling.

#### How to Run?
- Terminal: `scrapy runspider BrickSetSpider.py`

#### Sample Output
```
2020-06-02 22:42:21 [scrapy.utils.log] INFO: Scrapy 2.1.0 started (bot: scrapybot)
2020-06-02 22:42:21 [scrapy.utils.log] INFO: Versions: lxml 4.3.4.0, libxml2 2.9.9, cssselect 1.1.0, parsel 1.6.0, w3lib 1.22.0, Twisted 20.3.0, Python 3.7.4 (default, Aug 13 2019, 15:17:50) - [Clang 4.0.1 (tags/RELEASE_401/final)], pyOpenSSL 19.0.0 (OpenSSL 1.1.1d  10 Sep 2019), cryptography 2.7, Platform Darwin-18.7.0-x86_64-i386-64bit
2020-06-02 22:42:21 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.selectreactor.SelectReactor
2020-06-02 22:42:21 [scrapy.crawler] INFO: Overridden settings:
{'SPIDER_LOADER_WARN_ONLY': True}
2020-06-02 22:42:21 [scrapy.extensions.telnet] INFO: Telnet Password: 1ef4f1b73dbd04f1
2020-06-02 22:42:21 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.logstats.LogStats']
2020-06-02 22:42:22 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2020-06-02 22:42:22 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2020-06-02 22:42:22 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2020-06-02 22:42:22 [scrapy.core.engine] INFO: Spider opened
2020-06-02 22:42:22 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2020-06-02 22:42:22 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2020-06-02 22:42:22 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://brickset.com/sets/year-2016> (referer: None)
2020-06-02 22:42:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': 'Brick Bank', 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10251-1.jpg?201510121127'}
2020-06-02 22:42:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': 'Volkswagen Beetle', 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10252-1.jpg?201606140214'}
2020-06-02 22:42:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': 'Big Ben', 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10253-1.jpg?201605190256'}
2020-06-02 22:42:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': 'Winter Holiday Train', 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10254-1.jpg?201608110306'}
2020-06-02 22:42:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': 'XL Creative Brick Box', 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10654-1.jpg?201609271134'}
2020-06-02 22:42:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': 'Creative Building Set', 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10702-1.jpg?201511230710'}
2020-06-02 22:42:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': 'Creative Building Basket', 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10705-1.jpg?201605201119'}
2020-06-02 22:42:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': 'Police Helicopter Chase', 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10720-1.jpg?201601050913'}
2020-06-02 22:42:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': 'Iron Man vs. Loki', 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10721-1.jpg?201601050913'}
2020-06-02 22:42:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': 'Snake Showdown', 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10722-1.jpg?201601050913'}
2020-06-02 22:42:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': "Ariel's Dolphin Carriage", 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10723-1.jpg?201601050913'}
2020-06-02 22:42:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': 'Batman & Superman vs. Lex Luthor', 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10724-1.jpg?201605201119'}
2020-06-02 22:42:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': 'Lost Temple', 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10725-1.jpg?201601050913'}
2020-06-02 22:42:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': "Stephanie's Horse Carriage", 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10726-1.jpg?201605201119'}
2020-06-02 22:42:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': "Emma's Ice Cream Truck", 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10727-1.jpg?201605201119'}
2020-06-02 22:42:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': "Mia's Vet Clinic", 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10728-1.jpg?201605201119'}
2020-06-02 22:42:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': "Cinderella's Carriage", 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10729-1.jpg?201601050913'}
2020-06-02 22:42:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': 'Baby Animals', 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10801-1.jpg?201511230710'}
2020-06-02 22:42:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': 'Savanna', 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10802-1.jpg?201511230710'}
2020-06-02 22:42:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': 'Arctic', 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10803-1.jpg?201511230710'}
2020-06-02 22:42:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': 'Jungle', 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10804-1.jpg?201511230710'}
2020-06-02 22:42:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': 'Around the World', 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10805-1.jpg?201601050913'}
2020-06-02 22:42:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': 'Horses', 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10806-1.jpg?201511230710'}
2020-06-02 22:42:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': 'Horse Trailer', 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10807-1.jpg?201511230710'}
2020-06-02 22:42:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://brickset.com/sets/year-2016>
{'name': 'Little Plane', 'pieces': None, 'minifigs': None, 'image': 'https://images.brickset.com/sets/small/10808-1.jpg?201511230710'}
2020-06-02 22:42:23 [scrapy.core.engine] INFO: Closing spider (finished)
2020-06-02 22:42:23 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 226,
 'downloader/request_count': 1,
 'downloader/request_method_count/GET': 1,
 'downloader/response_bytes': 15326,
 'downloader/response_count': 1,
 'downloader/response_status_count/200': 1,
 'elapsed_time_seconds': 1.104971,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2020, 6, 3, 3, 42, 23, 119894),
 'item_scraped_count': 25,
 'log_count/DEBUG': 26,
 'log_count/INFO': 10,
 'memusage/max': 54370304,
 'memusage/startup': 54370304,
 'response_received_count': 1,
 'scheduler/dequeued': 1,
 'scheduler/dequeued/memory': 1,
 'scheduler/enqueued': 1,
 'scheduler/enqueued/memory': 1,
 'start_time': datetime.datetime(2020, 6, 3, 3, 42, 22, 14923)}
2020-06-02 22:42:23 [scrapy.core.engine] INFO: Spider closed (finished)
```

### References
- [How To Crawl A Web Page with Scrapy and Python 3](https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3)
- [Wikipedia: XPath](https://en.wikipedia.org/wiki/XPath)