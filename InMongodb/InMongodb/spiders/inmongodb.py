import scrapy
class InputmongodbItem(scrapy.Item):
    tag = scrapy.Field()  # 标签字段
    cont = scrapy.Field()  # 名言内容
    pass