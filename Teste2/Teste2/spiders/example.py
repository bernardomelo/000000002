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
    start_urls = ['https://lista.mercadolivre.com.br/geladeira']

    def parse(self, response):
        resposta = response.xpath('//ol/li')
        items = []
        for elemento in resposta:

         
            Imagem = ' '.join(elemento.xpath('.//div[contains(@class, "image-content")]/a/@href').extract())
            Nome = ' '.join(elemento.xpath(".//div/h2/a/span/text() " ).extract())
            Price = ' '.join(elemento.xpath(".//div/div/span[@class='price__fraction']/text()" ).extract())
            Desconto = ' '.join(elemento.xpath(".//div[contains(@class, 'item__discount')]/text()").extract())
            Vendedor = ' '.join(elemento.xpath(".//div[contains(@class,'item__brand')]//span/text()").extract())
            ItensVendidos = ' '.join(elemento.xpath(".//div[contains(@class,'item__condition')]/text()").extract())
            InfoAdicional = ' '.join(elemento.xpath(".//p[contains(@class, 'stack-item-info')]/text()").extract())
            items.append(Imagem)
            items.append(Nome)
            items.append(Price)
            items.append(Desconto)
            items.append(Vendedor)
            items.append(ItensVendidos)
            items.append(InfoAdicional)

            
        pass
        while len(items) > 1:
            print('Imagem: ', items[0])
            print('Nome: ', items[1])
            print('Price: ', items[2])
            print('Desconto: ', items[3])
            print('Vendedor: ', items[4])
            print('ItensVendidos: ', items[5])
            print('InfoAdicional: ', items[6])
            print('\n')
            items.pop(0)
            items.pop(0)
            items.pop(0)
            items.pop(0)
            items.pop(0)
            items.pop(0)
            items.pop(0)
            pass


