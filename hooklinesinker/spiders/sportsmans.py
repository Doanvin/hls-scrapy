# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from hooklinesinker.items import HooklinesinkerItem


class SportsmansSpider(scrapy.Spider):
    name = 'sportsmans'
    allowed_domains = ['storelocator.sportsmanswarehouse.com', 'sportsmanswarehouse.com']
    start_urls = [
        # # ALASKA
        # # Anchorage
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=121&siteStateProv=&taskQuery=Search',
        # # Firbanks
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=145&siteStateProv=&taskQuery=Search',
        # # Juneau
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=248&taskID=list&taskQuery=Search',
        # # Soldotna
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=212&siteStateProv=&taskQuery=Search',
        # # Wasilla
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=159&siteStateProv=&taskQuery=Search',
        # # ARIZONA
        # # Avondale
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=252&siteStateProv=&taskQuery=Search',
        # # Flagstaff
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=239&siteStateProv=&taskQuery=Search',
        # # Mesa
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=30&taskID=list&keywords=&siteNo=139&siteStateProv=&taskQuery=Search',
        # # Pheonix
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=117&taskID=list&taskQuery=Search',
        # # Prescott
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=253&taskID=list&taskQuery=Search',
        # # Show Low
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=253&taskID=list&taskQuery=Search',
        # # Tuscon
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=132&siteStateProv=&taskQuery=Search',
        # # Yuma
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=181&siteStateProv=&taskQuery=Search',
        # # CALIFORNIA
        # # Rancho Cordova
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=All&siteNo=233&siteStateProv=&taskQuery=Search',
        # # Rocklin
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=30&taskID=list&keywords=All&siteNo=149&siteStateProv=&taskQuery=Search',
        # # Chico
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=30&taskID=list&keywords=All&siteNo=232&siteStateProv=&taskQuery=Search',
        # # Eureka
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=All&siteNo=184&siteStateProv=&taskQuery=Search',
        # # Fairfield
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=All&siteStateProv=&siteNo=176&taskID=list&taskQuery=Search',
        # # Fresno
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=All&siteStateProv=&siteNo=238&taskID=list&taskQuery=Search',
        # # Rohnert Park
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=247&siteStateProv=&taskQuery=Search',
        # # Stockton
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=186&siteStateProv=&taskQuery=Search',
        # # Visalia
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=183&siteStateProv=&taskQuery=Search',
        # # COLORADO
        # # Colorado Springs
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=138&siteStateProv=&taskQuery=Search',
        # # Grand Junction
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=108&siteStateProv=&taskQuery=Search',
        # # Loveland
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=106&taskID=list&taskQuery=Search',
        # # Pueblo
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=182&taskID=list&taskQuery=Search',
        # # Sheridan
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=243&taskID=list&taskQuery=Search',
        # # Thornton
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=30&taskID=list&keywords=&siteNo=119&siteStateProv=&taskQuery=Search',
        # # IOWA
        # # Ankeny
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=120&taskID=list&taskQuery=Search',
        # # IDAHO
        # # Idaho Falls
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=105&taskID=list&taskQuery=Search',
        # # Lewiston
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=226&siteStateProv=&taskQuery=Search',
        # # Nampa
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=224&siteStateProv=&taskQuery=Search',
        # # Pocatello
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=236&siteStateProv=&taskQuery=Search',
        # # KENTUKY
        # # Lexington
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=163&taskID=list&taskQuery=Search',
        # # LOUISIANA
        # # Slidell
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=250&taskID=list&taskQuery=Search',
        # # MONTANA
        # # Bozeman
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=203&siteStateProv=&taskQuery=Search',
        # # Missoula
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=30&taskID=list&keywords=&siteNo=201&siteStateProv=&taskQuery=Search',
        # # NORTH CAROLINA
        # # Wilmington
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=177&taskID=list&taskQuery=Search',
        # # NEWMEXICO
        # # Albuquerque
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=40&taskID=list&keywords=&siteNo=126&siteStateProv=&taskQuery=Search',
        # # Las Cruces
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=251&siteStateProv=&taskQuery=Search',
        # # NEVADA
        # # Carson City
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=229&taskID=list&taskQuery=Search',
        # # Las Vegas
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=222&siteStateProv=&taskQuery=Search',
        # # Reno
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=123&siteStateProv=&taskQuery=Search',
        # # OREGON
        # # Albany
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=245&taskID=list&taskQuery=Search',
        # # Bend
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=30&taskID=list&keywords=&siteNo=206&siteStateProv=&taskQuery=Search',
        # # Hillsboro
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=230&siteStateProv=&taskQuery=Search',
        # # Klamoth Falls
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=241&taskID=list&taskQuery=Search',
        # # Medford
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=158&siteStateProv=&taskQuery=Search',
        # # Portland
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=204&taskID=list&taskQuery=Search',
        # # Roseburg
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=249&taskID=list&taskQuery=Search',
        # # Salem
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=205&taskID=list&taskQuery=Search',
        # # TENNESSEE
        # # Chatanooga
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=152&taskID=list&taskQuery=Search',
        # # UTAH
        # # Cedar City
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=178&taskID=list&taskQuery=Search',
        # # Heber City
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=240&siteStateProv=&taskQuery=Search',
        # # Logan
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=228&taskID=list&taskQuery=Search',
        # # Provo
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=102&taskID=list&taskQuery=Search',
        # # Riverdale
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=103&siteStateProv=&taskQuery=Search',
        # # South Jordan
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=30&taskID=list&keywords=&siteNo=246&siteStateProv=&taskQuery=Search',
        # # St. George
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=148&siteStateProv=&taskQuery=Search',
        # # Vernal
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=234&siteStateProv=&taskQuery=Search',
        # # VIRGINIA
        # # Roanoke
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=223&siteStateProv=&taskQuery=Search',
        # # WASHINGTON
        # # Everett
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=185&siteStateProv=&taskQuery=Search',
        # # Ferderal Way
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=40&taskID=list&keywords=&siteNo=210&siteStateProv=&taskQuery=Search',
        # # Kelso
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=235&siteStateProv=&taskQuery=Search',
        # # Kennewick
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=207&taskID=list&taskQuery=Search',
        # # Moses Lake
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=179&taskID=list&taskQuery=Search',
        # # Puyallup
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=213&siteStateProv=&taskQuery=Search',
        # # Silverdale
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=209&taskID=list&taskQuery=Search',
        # # Spokane Valley
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=30&taskID=list&keywords=&siteNo=188&siteStateProv=&taskQuery=Search',
        # # Vancouver
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=30&taskID=list&keywords=&siteNo=208&siteStateProv=&taskQuery=Search',
        # # Wenatchee
        # # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=231&siteStateProv=&taskQuery=Search',
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=180&taskID=list&taskQuery=Search',
        # # WYOMING
        # # Casper
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/?keywords=&siteStateProv=&siteNo=137&taskID=list&taskQuery=Search',
        # # Gillete
        # 'https://storelocator.sportsmanswarehouse.com/fishing_report/index.cfm?appID=100&taskPageID=&pageNo=1&maxRows=20&taskID=list&keywords=&siteNo=255&siteStateProv=&taskQuery=Search'
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
            gps = sel.xpath('//tr[5]/td[2]/text()').extract_first(),
            report = sel.xpath('//tr[7]/td/p/text()').extract_first(),
            access = sel.xpath('//tr[9]/td/p/text()').extract_first(),
        )


