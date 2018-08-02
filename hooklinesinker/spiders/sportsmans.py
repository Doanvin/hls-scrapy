# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from hooklinesinker.items import HooklinesinkerItem


class SportsmansSpider(scrapy.Spider):
    name = 'sportsmans'
    allowed_domains = ['storelocator.sportsmanswarehouse.com', 'sportsmanswarehouse.com']
    start_urls = [
        'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=All&siteNo=233&siteStateProv=&taskQuery=Search',
        'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=30&taskID=list&keywords=All&siteNo=149&siteStateProv=&taskQuery=Search'
    ]

    def parse(self, response):
        # follow links to individual fishing sites
        for href in response.css('tbody tr td.textBold a::attr(href)').extract():
            yield response.follow(href, self.parse_site)

    def parse_site(self, response):
        """parse the necessary data from the reports"""

        # sets the scope as the table we are scraping data from within the page
        scope = response.xpath('//table[@id="mainTableAlt"]').extract()
        sel = Selector(text=scope)

        # saves our scraped values to an object/dict
        rep = {
            'name': sel.css('td.titleResult::text').extract_first(),
            'site': sel.xpath('//tr[3]/td[1]/text()').extract_first(),
            'date': sel.xpath('//tr[3]/td[2]/text()').extract_first(),
            'date_exp': sel.xpath('//tr[3]/td[3]/text()').extract_first(),
            'type': sel.xpath('//tr[3]/td[4]/text()').extract_first(),
            'rating': sel.xpath('//td/img/@title').extract_first(),
            'report': sel.xpath('//tr[7]/td/p/text()').extract_first(),
            'access': sel.xpath('//tr[9]/td/p/text()').extract_first(),
        }

        # yields our result using our Django Review model
        yield HooklinesinkerItem(
            name = rep['name'],
            site = rep['site'],
            date = rep['date'],
            date_exp = rep['date_exp'],
            type = rep['type'],
            rating = rep['rating'],
            report = rep['report'],
            access = rep['access'],
        )


