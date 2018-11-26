# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
class TesteItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Imagem = scrapy.Field()
    Nome = scrapy.Field()
    Price = scrapy.Field()
    Desconto = scrapy.Field()
    Vendedor = scrapy.Field()
    ItensVendidos = scrapy.Field()
    InfoAdicional = scrapy.Field()
    pass


class MLSpider(Spider):
    name = 'mlivre'
    start_urls = ['https://celulares.mercadolivre.com.br/celular']

    def parse(self, response):
        resposta = response.xpath('//ol/div')
        print(resposta)
        items = []
        for elemento in resposta:

            item = TesteItem()
            item['Imagem'] = ' '.join(elemento.xpath('//div[contains(@class, "image-content")]/a/@href').extract())
            item['Nome'] = ' '.join(elemento.xpath("//div/h2/a/span/text() " ).extract())
            item['Price'] = ' '.join(elemento.xpath("//div/div/span[@class='price__fraction']/text()" ).extract())
            item['Desconto'] = ' '.join(elemento.xpath("//div[contains(@class, 'item__discount')]/text()").extract())
            item['Vendedor'] = ' '.join(elemento.xpath("//div[contains(@class,'item__brand')]//span/text()").extract())
            item['ItensVendidos'] = ' '.join(elemento.xpath("//div[contains(@class,'item__condition')]/text()").extract())
            item['InfoAdicional'] = ' '.join(elemento.xpath("//p[contains(@class, 'stack-item-info')]/text()").extract())
            yield item
            items.append(item)
            
        pass
        print(items)

