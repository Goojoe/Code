#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
安装模块:
pip install requests lxml BeautifulSoup4 Pyemail
'''
# 导入requests(请求)模块
import requests
# bs4解析html
from bs4 import BeautifulSoup
# xpath解析器
from lxml import etree
# 获取当前时间
import time
# 请求头部信息
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.30",
    "Cookie":
    "ipb_pass_hash=f58d778df79a7eba02c4f2e14940ae31; ipb_member_id=5859832; sk=0j5al54oko50a6ex1ebtzaonq8w8; event=1654241066; ipb_session_id=ad207c1213f294aef0ce5e43ad82474b"
}
# 代理网络
proxies = {
    "http": "127.0.0.1:7788", 
    "https": "127.0.0.1:7788"
    }
# 指定请求URL
url = "https://e-hentai.org/hentaiathome.php"
# 请求url,赋值到html变量
html = requests.get(url=url, headers=headers)
# 设置编码
html.encoding = 'utf-8'
# 获取响应数据
# print(html.text)

# 使用Bs4解析网页
soup = BeautifulSoup(html.text, "lxml")
items = soup.find("table", class_="hct")
# 转换为字符串并保存
items = str(items)
# 保存文件以供接下来的etree.parse解析
with open("./content.html", "w", encoding="utf8") as f:
    f.write(items)
# 解析保存的文件
tree = etree.parse("./content.html")

# 解析客户端名,并赋值到client_id
client = tree.xpath("//a/text()")
# 从td筛选
ehentai_values = tree.xpath("//td/text()")
# year = str(time.localtime())
time_now = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
# 文案
li_name=["状态","服务器保存文件","信任度","质量","命中率","每日Hath"]
li_place=[1,4,9,10,11,12]
# 字典
port_43142={"服务器名称":str(client[0]),"时间":time_now}
port_43133={"服务器名称":str(client[1]),"时间":time_now}
# 遍历liplace,并增加字典
for i in range (len(li_place)):
    port_43142.update({li_name[i]:ehentai_values[li_place[i]]})
    port_43133.update({li_name[i]:ehentai_values[li_place[i]+14]})
#print(port_43142)
#print(port_43133)
# 邮件正文
mail_text=""
for k,v in port_43142.items():
    mail_text+=k+":"+str(v)+'\n'
mail_text+='----------' + '\n'
for k,v in port_43133.items():
    mail_text+=k+":"+str(v)+'\n'
print (mail_text)

