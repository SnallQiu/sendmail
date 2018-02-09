from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib
import re
from httplib2 import socks
import socket
import requests
import json
from random import choice
import time
import datetime
import config
import msgtxt



def getHtmlText(url,**headers):
    r = requests.get(url, headers = headers,timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text


def format_attrs(s):
    name, attr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), attr))




def toaddress(x):                                                                    #想个方法随机抽40个发
    with open(config.toaddress, 'r') as ff:
        list_40 = []
        w = ff.readlines()
        y = int(len(w)/40)
        if x==0:
            x = choice(range(1,y))                                                      #随机选40个收件人
        for i in range(40 * (int(x) - 1), 40 * x):
            list_40.append(w[i].strip())

        try:
            for myadd in config.myaddress:                                              #发送检测邮箱
                list_40.append(myadd)
        except:
            pass
        return list_40


def from_addr():                                                                      # 将账号密码拿出来保存到list列表
    with open(config.fromaddress, 'rb')as f:
        w = f.readlines()
        # w = 'llq794@163.com----mvrz8302'
        list = []
        for i in w:
            a = re.findall('(.*\.com).*?([a-z].*)', i.decode('utf-8'))                #正则提取密码为a-z开头的发件箱
            list.append(a)

        return list


# 113.76.16.15:3217
# 180.104.214.113:2837
# 123.152.66.238:2682
# 171.125.14.163:6996

def changeip(list):
    cs = choice(list)
    ip, port = cs[0], cs[1]

    socket.socket = socks.socksocket
    socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, ip, port)
    return cs
    pass


def get_testip(x,badip):                                                                    #badip是一个已经用过的烂ip列表，如果再次提取的ip是已经用过的烂ip就重新提取
    flag = 1
    iplist = []
    try:
        print('尝试得到ip中...................')
        #芝麻代理api pcak为订单号
        #jsonip = getHtmlText(
            #'http://webapi.http.zhimacangku.com/getip?num={x}&type=2&pro=&city=0&yys=0&port=1&pack=9659&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='.format(
                #x=x))
        #jsonip = getHtmlText('http://api.xdaili.cn/xdaili-api//newExclusive/getIp?spiderId=dc42e156630441bc842e327e3239de8a&orderno=MF201712235216hAYJPw&returnType=2&count={x}&machineArea='.format(x = x))
        '''kuaidaiapi'''
        #jsonip = getHtmlText('http://dps.kuaidaili.com/api/getdps/?orderid=901400145784338&num={x}&format=json&sep=1'.format(x= x))
        jsonip = getHtmlText('http://api.xdaili.cn/xdaili-api//privateProxy/getDynamicIP/DD20181247334wV15mW/c6fa2fdc7db611e7bcaf7cd30abda612?returnType=2')
        ips = json.loads(jsonip)
        print(ips)
        '''快代理'''


        #for i in ips['RESULT']:
        try:
                #if i.split(':')[0] in badip:
                #   break
            iplist.append([ips['RESULT']['wanIp'],int(ips['RESULT']['proxyport'])])

        except Exception as e:
            print(str(e))
            pass
        if iplist == []:
            get_testip(x,badip)
            time.sleep(15)
        return iplist

        #快代理
        '''

        for i in ips['data']:
            try:
                iplist.append([i['ip'], int(i['port'])])
                print('已得到ip: %s' % i['ip'])
            except:
                pass
        if iplist == []:
            get_testip(x, badip)
        return iplist
        '''




    except:
        print('得到ip失败......重新获取中')
        time.sleep(15)

        get_testip(x,badip)

        pass



    pass
def gettext():                                                                            #再加几个内容，防止被发出去了收不到

    text = msgtxt.Text.gettext()
    return text


'''主函数在这里'''
def timem(func):
    def main2(n,s,*args):
        if time.strftime('%H%M',time.localtime(time.time()))<config.runtime:                       #控制时间 每天发到晚上23.30结束
            print(time.strftime('%H%M',time.localtime(time.time())))
            return func(n,s,*args)
    return main2


@timem
def main(n,s,badip):
    begin = datetime.datetime.now()
    input_ip = 1
    fromlist = from_addr()
    print('一共有%d个发件人'%(len(fromlist)))
    input_to = 0#int(input('一共有36w/40 = 9000个收件人片段，输入发到第几个片段，如果输入为0 则随机片段发送：'))
    flag = 1                                                                               #flag 代表ip可用性
    iplist = get_testip(input_ip,badip)
    for x in range(s, len(fromlist)-1):
        try:

            ipnow = changeip(iplist)
            for i in range(10):
                try:


                    if flag == 0:                                                          #如果flag = 0 换个新ip并把这个烂ip舍弃掉
                        try:
                            print('ip : %s 是烂ip，丢弃中...'%ipnow[0])
                            iplist.remove(ipnow)
                            if iplist == []:
                                break
                            ipnow = changeip(iplist)
                        except:
                            pass
                    flag = 0
                    print('当前ip：' + requests.get("http://icanhazip.com", timeout=30).text)#验证当前ip
                    smtp_server = 'smtp.163.com'
                    text = gettext()                                                       #得到邮件内容列表

                    msg = MIMEText(choice(text))                                           #从内容列表中随机选一个作为最终发出去的内容


                    msg['From'] = format_attrs('猴子家houzihome <%s>' % fromlist[x][0][0])
                    '''msg['To']只接受一个字符串！！！！！'''
                    '''
                    for x in emaillist:
                        emails.append(format_attrs('尊敬的用户 <%s>' % x))
                    '''
                    msg['To'] = ','.join(toaddress(input_to))
                    msg['Subject'] = Header('猴子家', 'utf-8').encode()
                    server = smtplib.SMTP(smtp_server, 25, timeout=10)
                    server.starttls()
                    server.set_debuglevel(1)
                    server.login(fromlist[x][0][0], fromlist[x][0][1].strip())
                    server.sendmail(fromlist[x][0][0], toaddress(input_to), msg.as_string())
                    server.quit()
                    n = n + 1
                    print('发信箱：%s 发送40封信成功！' % fromlist[x][0][0])
                    print('已发送%d封邮件，发送%d次' % (40 * n, n))
                    flag = 1                                                                #发送成功说明ip好用 并且邮箱好用一直发到第11个40封为止
                except Exception as e:
                    if 'UserReject' in str(e) or 'authentication failed' in str(e):         #如果显示邮箱问题或者登陆问题，说明ip好用
                        flag = 1
                        break                                                               #跳过这个不能用的email
                    print(str(e))
                    print('发送失败,已发送：%d 封邮件'%(n*40))
                    if ipnow[0] in str(e) and iplist == []:
                        return n,x,badip

                    if 'timed out' in str(e):                                 #跳过不能切换ip的ip
                        x=x-1
                        break
            if iplist == []:
                    break

        except:
            if iplist ==[] or iplist==None:

                break
            pass




    end = datetime.datetime.now()

    print('耗时：%s'%(end-begin))
    print('---------------分割线---------------')

    print('发邮件结束 一共发送%d封发到第%d个发件人'%(40*n,x))

    print('---------------分割线---------------')
    return n,x,badip




'''这里才是真正的主函数！！！'''

n = 0
x = int(input('请输入发件人文件中第几个发件人开始：')) - 1  # 输入1  s = 0
badip=[]

# 可以把已经发送过的发件箱写进文件或者数据库
while 1:
    n,x,badip = main(n,x,badip)
    socket.socket = socks.socksocket
    socks.setdefaultproxy()
