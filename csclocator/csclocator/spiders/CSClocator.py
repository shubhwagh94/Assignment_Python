import scrapy


class CsclocatorSpider(scrapy.Spider):
    name = 'CSClocator'
    allowed_domains = ['CSClocator.com']
    start_urls = ['https://www.csclocator.com/csc/maharashtra/nagpur/nagpur']

    def parse(self, response):
        all_div_CSClocator = response.css('div.col-lg-12')
        name = all_div_CSClocator.css('td:nth-child(1)::text').extract()
        address = all_div_CSClocator.css('td:nth-child(2)::text').extract()
        phone_No = all_div_CSClocator.css('.table-striped a ::text').extract()
        yield {
            'name' : name,
            'address' : address,
            'phone_No' : phone_No
        }