# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from hooklinesinker.items import HooklinesinkerItem


class SportsmansSpider(scrapy.Spider):
    name = 'sportsmans'
    allowed_domains = ['storelocator.sportsmanswarehouse.com', 'sportsmanswarehouse.com']
    start_urls = [
        # Rancho Cordova
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=All&siteNo=233&siteStateProv=&taskQuery=Search',
        # Rocklin
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=30&taskID=list&keywords=All&siteNo=149&siteStateProv=&taskQuery=Search',
        # Chico
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=30&taskID=list&keywords=All&siteNo=232&siteStateProv=&taskQuery=Search',
        # Eureka
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=All&siteNo=184&siteStateProv=&taskQuery=Search',
        # Fairfield
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=All&siteStateProv=&siteNo=176&taskID=list&taskQuery=Search',
        # Fresno
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=All&siteStateProv=&siteNo=238&taskID=list&taskQuery=Search',
        # Rohnert Park
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=247&siteStateProv=&taskQuery=Search',
        # Stockton
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=186&siteStateProv=&taskQuery=Search',
        # Visalia
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=183&siteStateProv=&taskQuery=Search'
    ]

    def parse(self, response):
        # follow links to individual fishing sites
        for href in response.css('tbody tr td.textBold a::attr(href)').extract(): 
            yield response.follow(href, self.parse_site)

    def parse_site(self, response):
        """parse the necessary data from the reports"""

        # sets the scope as the table we are scraping data from within the page
        scope = response.xpath('//table[@id="mainTableAlt"]').extract_first()
        sel = Selector(text=scope)

        # yields our scraped values to HooklinesinkerItem
        yield HooklinesinkerItem(
            name = sel.css('td.titleResult::text').extract_first(),
            site = sel.xpath('//tr[3]/td[1]/text()').extract_first(),
            date = sel.xpath('//tr[3]/td[2]/text()').extract_first(),
            date_exp = sel.xpath('//tr[3]/td[3]/text()').extract_first(),
            type = sel.xpath('//tr[3]/td[4]/text()').extract_first(),
            rating = sel.xpath('//td/img/@title').extract_first(),
            report = sel.xpath('//tr[7]/td/p/text()').extract_first(),
            access = sel.xpath('//tr[9]/td/p/text()').extract_first(),
        )


