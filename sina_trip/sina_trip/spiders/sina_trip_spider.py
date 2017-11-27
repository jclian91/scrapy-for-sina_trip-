import scrapy
from scrapy.spiders import Spider  
from scrapy.selector import Selector  
from sina_trip.items import SinaTripItem  
  
  
class sinaTripSpider(Spider):  
    name = "sinaTripSpider"    #name of Spider  
    start_urls = ["http://travel.sina.com.cn/"]  #start url 
    
    def parse(self, response):   #parse function
        item = SinaTripItem()
        sel = Selector(response)
        sites = sel.xpath("//img/@src").extract()   #extract url of pictures
        for site in sites: 
            item['url'] = ['http:'+site]
            yield item
