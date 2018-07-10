'''
模拟登陆脚本
1.requests登录
2.携带cookie参数
'''

import requests
from bs4 import BeautifulSoup

url = 'http://example.webscraping.com/places/default/user/login'

data = {
	'email' : '1299193255@qq.com',
	'password' : 'Sdz6lffqxFW9MMLIt5fY',
}

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}

s = requests.Session()

def get_login_html():
	response = s.get(url)
	bs = BeautifulSoup(response.text, 'lxml')
	inputs = bs.select('#web2py_user_form input')
	print(response.url,'\n')
	data = {}
	for vo in inputs:
		if vo.get('name'):
			data[vo.get('name')] = vo.get('value')
	return (data, s.cookies)

def do_login_action(data,cookies):
	s.get(url, cookies = cookies)
	response = s.post(url, data = data)
	print(response.url,'\n')

def main():
	data, cookies = get_login_html()
	data['email'] = '1299193255@qq.com'
	data['password'] = 'Sdz6lffqxFW9MMLIt5fY'
	do_login_action(data, cookies)


if __name__ == '__main__':
	main()