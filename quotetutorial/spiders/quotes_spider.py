import scrapy
from ..items import QuotetutorialItem

# web scraping quotes, authors, tags
class QuoteSpider(scrapy.Spider):
	name = 'quotes'
	page_number = 2
	start_urls = ['https://www.amazon.in/Whirlpool-Semi-Automatic-Superb-Atom-70S/product-reviews/B071Z6MSY6/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber=1']

	def parse(self,response):

		items = QuotetutorialItem()

		all_reviews = response.css('div#cm_cr-review_list')
		for reviews in all_reviews: 
			date = reviews.css('#cm_cr-review_list span.review-date::text').extract()
			items['date'] = date

			yield items

		next_page = 'https://www.amazon.in/Whirlpool-Semi-Automatic-Superb-Atom-70S/product-reviews/B071Z6MSY6/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber='+ str(QuoteSpider.page_number)+'' #we only need attribute

		if QuoteSpider.page_number <= 35:
			QuoteSpider.page_number += 1
			yield response.follow(next_page, callback=self.parse)

