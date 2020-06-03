import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "bricksetspider"
    start_urls = ['https://brickset.com/sets/year-2016'] # variable name MUST BE `start_urls`; otherwise, it won't know the website.

    def parse(self, response):
        # [PRINT] for learning purpose
        # print(response) # "<200 https://brickset.com/sets/year-2016>"

        SET_SELECTOR = '.set' # refers to CSS class name (e.g. <article class='set'>...</article>)
        for brickset in response.css(SET_SELECTOR): 
            # [PRINT] for learning purpose            
            # print(brickset) # <Selector xpath="descendant-or-self::*[@class and contains(concat(' ', normalize-space(@class), ' '), ' set ')]" data='<article class="set">\n<a href="https:...'>

            NAME_SELECTOR = 'h1 ::text' # refers to the text wrapped inside of <h1>...</h1> tags (the <h1> can be anywhere inside of the <article class='set'>...</article>tag) 

            # refers to the number of pieces in XPath 
            # - '.' = current level (<article>);
            # - '//' = current or descendents in any level below ;
            # - '//dl[dt/text()=Pieces]' = <dl> tag that is inside of the current <article> tag, and "Pieces" is wrapped inside of <dt>...</dt> tags. 
            # - 'dd[2]' = the second `dd` tag
            PIECES_SELECTOR = './/dl[dt/text()=Pieces]/dd/a/text()' 
            MINIFIGS_SELECTOR = './/dl[dt/text()=Minifigs]/dd[2]/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'
            
            # print the extracted data
            yield {
                "name": brickset.css(NAME_SELECTOR).extract_first(),
                "pieces": brickset.xpath(PIECES_SELECTOR).extract_first(),
                "minifigs": brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                "image": brickset.css(IMAGE_SELECTOR).extract_first(),
            }
