import urllib.request
import urllib.parse
import time
import http.cookiejar

webUrl = "https://www.zhihu.com/login/email"  # 不能写https://www.zhihu.com/#signin因为不支持重定向

webheader = {
    # 'Accept': 'text/html, application/xhtml+xml, */*',
    # 'Accept-Language': 'zh-CN',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
    # 'User-Agent': 'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    # 'DNT': '1',
    # 'Connection': 'Keep-Alive'
}

postData = {
    'email': '794858207@qq.com',
    'captcha_type': 'cn',
    'password': 'lm1994',
    '_xsrf': '',
    'captcha': ''
}
localStorePath = "写你想保存的验证码图片的地址"

if __name__ == '__main__':
    # 声明一个CookieJar对象实例来保存cookie
    cookie = http.cookiejar.CookieJar()
    # 创建opener
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)  # 建立opener对象，并添加头信息
    urllib.request.install_opener(opener)

    captcha_url = 'https://www.zhihu.com/captcha.gif?r=%d&type=login&lang=cn' % (time.time() * 1000)
    # captcha_url = 'http://www.zhihu.com/captcha.gif?r=%d&type=login' % (time.time() * 1000)#这样获得的是“字母+数字验证码”

    # 这个获取验证码图片的方法是不行的！
    # urllib.request.urlretrieve(captcha_url, localStorePath + 'myCaptcha.gif')

    # 用urlopen函数保存验证图片
    req = urllib.request.Request(url=captcha_url, headers=webheader)
    content = urllib.request.urlopen(req)
    # content = opener.open(req)
    captcha_name = 'myNewCaptcha.gif'
    content = content.read()
    with open(captcha_name, 'wb') as f:
        f.write(content)

    postData['captcha'] = input('请输入验证码')
    # postData['_xsrf'] = get_xsrf()
    postData['_xsrf'] = 'fa5ae712244bd4287e371801052003fc'
    print(postData['_xsrf'])

    # 用urlopen函数传送数据给服务器实现登录
    postData_encoded = urllib.parse.urlencode(postData).encode('utf-8')
    req = urllib.request.Request(url=webUrl, data=postData_encoded, headers=webheader)
    webPage = urllib.request.urlopen(req)
    # webPage = opener.open(req)
    data = webPage.read().decode('utf-8')

    print(data)
    with open("D:/知乎服务器反馈的内容.txt", mode='w', encoding='utf-8') as dataFile:
        dataFile.write(data)
