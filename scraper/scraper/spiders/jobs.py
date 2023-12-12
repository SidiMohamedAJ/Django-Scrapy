from scrapy import Spider
from urllib.parse import urljoin
from scraper.scraper.items import ScraperItem

class SpiderLinkedin(Spider):
    name = "scarper_jobs"
    start_urls = ['https://www.linkedin.com/jobs/search?keywords=Data%20Science%20Manager&location=United%20States&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0']


    def parse(self, response):

        items = ScraperItem()

        stage_names = response.xpath('//div[@class="base-search-card__info"]/h3/text()').extract()
        locations = response.xpath('//div/span[@class="job-search-card__location"]/text()').extract()
        links = response.xpath('//div[@class="base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card"]/a/@href').extract()

        for stage_name, location, link in zip(stage_names, locations, links):
            relative_url = link.strip()

            items['stage_name'] = stage_name.strip()
            items['location'] = location.strip()
            items['url'] = relative_url

            yield items

        # Follow pagination links if they exist
        next_page = response.xpath('//button[@class="infinite-scroller__show-more-button infinite-scroller__show-more-button--visible"]/@href').extract()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
