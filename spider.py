# -*- coding: utf-8 -*-                                                                                                                                                                         #关注微信公众号“和你学Python”可获取更多资源

#导入requests库
import requests

#导入lxml库的etree
from lxml import etree 

#把练习用网址赋值给变量url
url = 'http://lab.scrapyd.cn/page/{}/'

#创建一个空列表
data = []

#获取一页的数据
def get_data(response):
    #将返回的网页代码通过etree创建一个HTML对象
    tree = etree.HTML(response.text)
    
    #获取所有词条节点
    div_list = tree.xpath('//div[@class="quote post"]')

    #遍历div获取该页的内容
    for div in div_list:
        #创建一个空字典
        dic = {}
        
        #获取作者
        dic['author'] = div.xpath('.//small[@class="author"]')[0].text
        
        #获取标签
        tags = []
        for tag in div.xpath('.//a[@class="tag"]'):
            tags.append(tag.text)
        dic['tags'] = tags
        
        #获取文本
        dic['text'] = div.xpath('.//span[@class="text"]')[0].text

        #把字典添加入列表
        data.append(dic)

#定义保存的函数
def save(lst):
    #以写入方式打开一个文件
    with open(r'C:\Users\Administrator\Desktop\data.txt', 'w') as file:
        #把列表里的字典输入到文件里
        for dic in lst:
            for key, value in dic.items():
                file.write(key + '：' + str(value) + ' ')
            file.write('\n')
    print('文件已保存')
    
if __name__ == '__main__':
    #获取所有页面的数据
    for i in range(1, 7):
        get_data(requests.get(url.format(i)))
        print('第{}页数据已获取'.format(i))
        
    #把存有所有数据的data写入文件
    save(data)










#关注微信公众号“和你学Python”可获取更多资源
