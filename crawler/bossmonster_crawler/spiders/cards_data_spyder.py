import scrapy


class CardsDataSpider(scrapy.Spider):
    name = "cards_data"
    start_urls = [
        'http://bossmonster.wikia.com/wiki/List_of_Cards',
    ]

    def parse(self, response):
        card_tr_items = response.xpath('//table')[7].xpath('.//tr')
        for card_it in card_tr_items[1:]:
            tds = card_it.xpath('.//td')
            id = tds[0].xpath('.//text()').extract_first().strip()
            name = tds[1].xpath('.//a').xpath('./text()').extract_first()
            if name is None:
                name = tds[1].xpath('.//text()').extract_first().strip()
            # name = "".join(tds[1].xpath('.//text()').extract()).strip()
            # name = filter(lambda str: bool(str) and not str.isspace(),
            #         tds[1].xpath('.//text()').extract())[0]
            subtitle = tds[2].xpath('.//text()').extract_first().strip()
            stats = tds[3].xpath('.//text()').extract_first().strip()
            treasure = tds[4].xpath('.//text()').extract_first().strip()
            type = tds[5].xpath('.//a/text()').extract_first().strip()
            desc = '\n'.join(tds[6].xpath('.//text()').extract()).strip()
            min = tds[7].xpath('.//text()').extract_first().strip()
            amnt = tds[8].xpath('.//text()').extract_first().strip()
            link = None
            link = tds[1].xpath('.//a/@href').extract_first()
            if link is None:
                link = tds[6].xpath('.//a/@href').extract_first()
            item = {
                    'id':  id,
                    'name':  name.strip(),
                    'subtitle':  subtitle,
                    'stats':  stats,
                    'treasure':  treasure,
                    'type':  type,
                    'desc':  desc,
                    'min':  min,
                    'amnt':  amnt,
                    'link':  link,
                    'img_url': "",
            }
            if link is None:
                yield item
            request = scrapy.Request(response.urljoin(link), callback=self.parse_img_link)
            request.meta['item'] = item
            yield request

    def parse_img_link(self, response):
        img_selected = response.xpath('//img[starts-with(@class, "thumbimage")]')
        img_url = ""
        if len(img_selected) > 0:
            img_srcs = img_selected[0].xpath('@src').extract()
            if len(img_srcs) > 0:
                img_url = img_srcs[0]
        item = response.meta['item']
        item['img_url'] = img_url
        yield item
