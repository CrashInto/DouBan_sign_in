
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re

login_url = 'https://www.douban.com/accounts/login'
home_url = 'https://www.douban.com'
username = input('输入账号：')
password = input('输入密码：')
data = {
    'form_email': username,
    'form_password': password,
    'redir': 'https://www.douban.com',
    'login': '登录'
}
s = requests.session()
response = s.get(login_url).text
soup = BeautifulSoup(response,'lxml')
captcha_image_link = soup.select('#captcha_image')[0]['src']
id_patt = re.compile('<input type="hidden" name="captcha-id" value="(.*?)".*?>',re.S)
captcha_image_id = re.search(id_patt,response).group(1)

if captcha_image_link:
    print('请等待验证码加载...')
    browser = webdriver.Chrome()
    browser.get(captcha_image_link)
    captcha = input('输入验证码：')
    data['captcha-solution'] = captcha
    data['captcha-id'] = captcha_image_id
    login = s.post(login_url,data = data)
    browser.close()
    result = s.get(home_url)
    # print(result.text)
    login_soup = BeautifulSoup(result.text,'lxml')
    capture = login_soup.select('.bn-more')
    print('当前登陆账号为：'+capture[0].get_text())
