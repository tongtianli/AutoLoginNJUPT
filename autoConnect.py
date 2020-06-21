import requests
import re
from urllib import parse
import datetime

def log(text : str):
    strTime = datetime.datetime.now().strftime("%m.%d %H:%M:%S")
    with open('log.txt','a+') as f:
        f.write(strTime + ' : ' + text + '\n')

hd = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36"}

BASEURL = 'http://10.10.244.11:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=10.10.244.11&iTermType=1&wlanuserip={}&wlanacip={}&wlanacname={}&mac=00-00-00-00-00-00&ip={}&enAdvert=0&queryACIP=0&loginMethod=1'

response = requests.get('http://baidu.com/', headers=hd)
if len(re.findall('百度一下',response.text)) != 0:
    log('已连接网络，停止执行联网操作')
    exit(1)
print(response.text)
htmlUrlText = re.findall('<a href=".*">',response.text)[0]
url = htmlUrlText.split('"')[1]
params = parse.parse_qs( parse.urlparse( url ).query )
logginUrl = BASEURL.format(params['wlanuserip'][0],params['wlanacip'][0],params['wlanacname'][0],params['wlanuserip'][0])

with open('config.txt','r') as f:
    config = f.readlines()
provider = config[0].split(':')[-1].replace('\n','')
username = config[1].split(':')[-1].replace('\n','')
password = config[2].split(':')[-1].replace('\n','')
print(provider,username,password)
if provider == '移动':
    username =username + '@cmcc'
elif provider == '电信':
    username =username + '@njxy'
elif provider == '校园网':
    pass
else:
    log('运营商选择错误，请输入电信/移动/校园网，不需要空格')
    exit(1)
data = {'DDDDD':username,'upass':password,'R1':0,'R2':0,'R3':0,'R6':0,'para':00,'0MKKey':123456}
response = requests.post(logginUrl,data)
print(response.text)
if len(re.findall('成功',response.text)) != 0:
    log('登陆成功')
else:
    log('登陆失败')