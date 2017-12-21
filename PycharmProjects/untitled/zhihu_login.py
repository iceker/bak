import requests

agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
header = {
    "HOST":"www.zhihu.com",
    "Referer": "https://www.zhizhu.com",
    'User-Agent': agent
}

session = requests.session()
post_url = "https://www.zhihu.com/api/v3/oauth/sign_in"
post_data = {
    "client_id":"c3cef7c66a1843f8b3a9e6a1e3160e20",
    "grant_type":"password",
    "username": "794858207@qq.com",
    "password": "lm1994",
    "timestamp":"1505459447271",
    "source":"com.zhihu.web",
    "signature":"bb0a35e91417c2a190745d5f650704da0cf390ab"
}
response_text = session.post(post_url, data=post_data, headers=header)
print(response_text.text)
