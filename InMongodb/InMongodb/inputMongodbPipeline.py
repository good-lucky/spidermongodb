import pymongo
class InputmongodbPipeline(object):
    def __init__(self):
        # 建立MongoDB数据库连接
        client = pymongo.MongoClient('127.0.0.1', 27017)
        # 连接所需数据库,ScrapyChina为数据库名
        db = client['spidertest']
        # 连接所用集合，也就是我们通常所说的表，mingyan为表名
        self.post = db['spidertest']

    # 重写process_item 方法
    def process_item(self, item, spider):
        postItem = dict(item)  # 把item转化成字典形式
        self.post.insert(postItem)  # 向数据库插入一条记录
        return item  # 会在控制台输出原item数据，可以选择不写