# 导入requests(请求)模块
import requests
# bs4解析html
from bs4 import BeautifulSoup
# xpath解析器
from lxml import etree
# 获取当前时间
import time

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

def requests_text(url,):
