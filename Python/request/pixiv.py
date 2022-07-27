import requests
import json

http_address = '127.0.0.1:7788'
https_address = '127.0.0.1:7788'
url = 'https://www.pixiv.net/artworks/77995894'


proxies = {
    "http": http_address,
    "https": http_address
}
headers = {
    # 'Referer':'https://www.pixiv.net',
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Mobile Safari/537.36 Edg/101.0.1210.53',
    'Cookie':'first_visit_datetime_pc=2022-05-28+20:39:03; p_ab_id=7; p_ab_id_2=6; p_ab_d_id=651071587; yuid_b=GEZHlXQ; __cf_bm=cUOEgitB8SgMdu3cKma70xziRzYkfJyu.VYMetnzvsU-1653737952-0-AV+Zi8WOEs+oKwd5W449VdtVvKjrdbaLnmL6KwZVs8x//i7SDY2JDJjC0S0eX3okOZ9TKEj9/RRNZPPT5BcY6cuV8Vxf0rZ0TGCzEPHFiCAfsxB6dwUJzeY7R5CBOm1vJTw4mkD019OcayBftc77E88knE6kNGpsFLgRyUmfhd9QDmpkOmFx0JAl50RUc6PjAQ==; _fbp=fb.1.1653737955227.1953647081; PHPSESSID=61904428_BtN5O7bSHVG6X8ajT9a6D9mD8ysfL5FE; device_token=e8f0674f48ecfa1c4e919275156815fc; privacy_policy_agreement=3; c_type=22; privacy_policy_notification=0; a_type=0; b_type=1; QSI_S_ZN_5hF4My7Ad6VNNAi=r:10:2'
}
# res = requests.get('https://www.pixiv.net/',headers=headers,proxies=proxies)
# print(res.text)
# with open('./pixiv.html','w',encoding='utf-8') as f:
#     f.write(res.text)
# 获取画师id
def getAuthorAllPicId(id):
    # 传入参数
    url = 'https://www.pixiv.net/ajax/user/' + str(id) + '/profile/all'
    # 请求
    response = requests.get(url, headers=headers,proxies=proxies,verify = False)
    if response.status_code == 200:
        # 解析json数据
        resdict = json.loads(response.content)['body']['illusts']
        return [key for key in resdict]
    else:
        print('解析json失败')


headers['Referer'] = 'https://www.pixiv.net/artworks/{}'.format(getAuthorAllPicId(3036679))
# referer来源地址artworks/{}'.format(pic.id)
# 我们可以从上述链接中得到很多信息，比如标题，后缀名，保存时会方便一些
for i in range(count):
    turl = url.replace('_p0', '_p' + str(i))
    ttitle = title + '({})'.format(str(i))
    self.dlquene.put(Pic(ttitle, pic_id, turl, ext))

img = requests.get(url = url, headers=self.headers,proxies=proxies)
if img.status_code == 200:
    path = '.\\images\\' + helper.filenameRuler(title) + pic.ext
    with open(path, 'wb') as fp:
        try:
            fp.write(img.content)
        except Exception as e:
            print(e)
        fp.close()

