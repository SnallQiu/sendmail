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


def getHtmlText(url,**headers):
    # print(url)
    # pro = {'http': 'http://144.0.48.126:8080'}
    r = requests.get(url, headers = headers,timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text


def format_attrs(s):
    name, attr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), attr))




def toaddress(num):                                                                    #想个方法随机抽40个发
    with open('收信人2.txt', 'r') as ff:
        #x = x-2050
        w = ff.readlines()
        y = int(len(w)/40)
        for s in range(num):
            list_40 = []
            x = choice(range(1, y))  # 随机选40个收件人
            for i in range(5 * (int(x) - 1), 5 * x):
                list_40.append(w[i].strip())
            list_40.append('305460936@qq.com')
            yield list_40
        #list_40.append('17854212463@163.com')
        #list_40.append('513359686@qq.com')                                         #如果要测试邮箱发送率 这边添加一个自己的qq收件箱
        #list_40.append('870407139@qq.com')




def from_addr():  # 将账号密码拿出来保存到list列表
    with open('/Users/zangxiaojie/PycharmProjects/sendemail/fromadd2.txt', 'rb')as f:
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
    #print(cs)
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
        jsonip = getHtmlText('http://dps.kuaidaili.com/api/getdps/?orderid=901400145784338&num={x}&format=json&sep=1'.format(x= x))


        ips = json.loads(jsonip)
        print(ips)
        '''快代理'''


        for i in ips['data']['proxy_list']:
            try:
                #if i.split(':')[0] in badip:
                #   break
                iplist.append([i.split(':')[0],int(i.split(':')[1])])

            except Exception as e:
                print(str(e))
                pass
        #print('得到%d个ip'%(len(iplist)))
        if iplist == []:
            get_testip(x,badip)
        return iplist
        #if len(iplist) > 0:
        #else:
            #get_testip(x,badip)


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
        time.sleep(5)

        get_testip(x,badip)

        pass



    pass
def gettext():                                                                            #再加几个内容，防止被发出去了收不到

    text = [#"房产类app猴子家是一个新房，短租，二手房的买卖平台，\n"
                            #+ "这里有丰富的房产资讯，一手的新房，温馨的二手房，还可以电话直联房东哦。\n"
                             "这是一款二次元租房神器。这里是齐天大圣的家。买房就上猴子家。\n"
                            # + "猴子家下载链接：https://itunes.apple.com/cn/app/%E7%8C%B4%E5%AD%90%E5%AE%B6-%E6%96%B0%E6%88%BF-%E7%9F%AD%E7%A7%9F-%E4%BA%8C%E6%89%8B%E6%88%BF%E7%9A%84%E4%B9%B0%E5%8D%96%E5%B9%B3%E5%8F%B0/id1121556351?mt=8 <br> "
                            + "请关注公众号houzihome，会有惊喜哦！\n "
                            + "看大圣归来，能否再创辉煌！！！",                                #逗号分隔

                            #'相遇，在不经意间｡能邂逅你，是我之幸｡\n'
                            '我因你成长， 为你追问世事，\n'
                            + '而你，却再不问寻天长地久｡\n'
                            #+ '我因你改变，变成你喜欢的模样，\n'
                            + '而你，却再也不敲击我的心门｡\n'
                            + '我把时光与情意写成文字寄予你，\n'
                            #+ '而你， 却从未展信｡\n'
                            + '也许，不打扰，即是温柔｡\n'
                            + '所以停笔，将信笺收起。\n'
                            #+ '但愿，再转身以后，还会相遇...\n'
                            + '我是猴子家，让和你一起成长。',
                            #'我是houzihome hhhhhh 2018快乐！',
                            #'测试hzhome，2018年快乐！',
                            #'python 爱好者祝你2018快快来',
                            '姑娘，还在为和男朋友吵架而闷闷不乐？买个房子吧，让我们做你最终的安慰。\n'
                            +'姑娘，爱像烟火，怎么热烈缤纷怎么来，而绚烂过后往往是满地碎屑，买个房子吧，让我们握住你的手，给你一生的安全感。\n'
                            #+'姑娘，清水煮岁月，不悲不喜，做个远离尘世，安安静静地女子，是毕生的愿望，买个房子吧，他会是你最好的依靠。\n'
                            +'买房就上猴子家。'
                            ]
    #text = ['来自山东青岛的信','是我是我就是我小哪吒！']
    return text


'''主函数在这里'''
def timem(func):
    def main2(n,s,*args):
        if time.strftime('%H%M',time.localtime(time.time()))<'2330':                       #控制时间 每天发到晚上23.30结束
            print(time.strftime('%H%M',time.localtime(time.time())))
            return func(n,s,*args)
    return main2


@timem
def main(n,s,badip):
    begin = datetime.datetime.now()
    input_ip = 1
    fromlist = from_addr()
    print('一共有%d个发件人'%(len(fromlist)))
    #s = int(input('请输入发件人文件中第几个发件人开始：'))-1                                    #输入1  s = 0
    input_to = 1#int(input('一共有36w/40 = 9000个收件人片段，输入发到第几个片段，如果输入为0 则随机片段发送：'))
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
                            #badip.append(ipnow[0])
                            iplist.remove(ipnow)
                            #print(iplist)
                            if iplist == []:
                                break
                            ipnow = changeip(iplist)
                            #while ipnow in badip:
                                #ipnow = changeip(iplist)
                        except:
                            pass
                    flag = 0
                    print('当前ip：' + requests.get("http://icanhazip.com", timeout=30).text)#验证当前ip
                    smtp_server = 'smtp.163.com'
                    text = gettext()                                                       #得到邮件内容列表

                    msg = MIMEText(choice(text))                                           #从内容列表中随机选一个作为最终发出去的内容

                    # msg = MIMEText('houzihome')

                    msg['From'] = format_attrs('猴子家houzihome <%s>' % fromlist[x][0][0])
                    '''msg['To']只接受一个字符串！！！！！'''
                    # masto = ''
                    # emails = []
                    '''
                    for x in emaillist:
                        emails.append(format_attrs('尊敬的用户 <%s>' % x))
                    '''
                    # msg['To'] = ','.join((format_attrs('管理员 <%s>'%to_addr1),format_attrs(' <%s>'%to_addr2))
                    #msg['To'] = ','.join(toaddress(input_to))
                    msg['Subject'] = Header('齐天大圣的问候', 'utf-8').encode()
                    server = smtplib.SMTP(smtp_server, 25, timeout=10)
                    server.starttls()
                    server.set_debuglevel(1)
                    server.login(fromlist[x][0][0], fromlist[x][0][1].strip())
                    for i in toaddress(8):
                        msg['To'] = ','.join(i)
                        server.sendmail(fromlist[x][0][0], i, msg.as_string())
                        print('发送5封成功！')
                    server.quit()
                    # email_hassend.append(fromlist[x][0][0])
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
                        #break

                    if 'timed out' in str(e):                                 #跳过不能切换ip的ip
                        break
            if iplist == []:
                    break

        except Exception as e:
            #print(str(e))
            if iplist ==None or iplist ==[]:
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
#time = time.strftime('%H%M',time.localtime(time.time()))
#print(time)
while 1:
    n,x,badip = main(n,x,badip)
    socket.socket = socks.socksocket
    socks.setdefaultproxy()
    #print('这些烂ip们：',badip)#把http ip弄回成主机ip
