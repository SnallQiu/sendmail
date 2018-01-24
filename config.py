import msgtxt
import time
'''温馨提示：使用前上快代理设置 https://www.kuaidaili.com/usercenter/dpsipwhitelist/  主机ip白名单'''

'''在这里进行常规设置'''

'''设置收发邮箱文件'''
toaddress = '收信人2.txt'
fromaddress = 'fromadd3.txt'

'''设置检查收到邮箱，可以添加自己的邮箱'''
myaddress = ['305460936@qq.com']

'''设置一天脚本跑的时长'''
'''2330代表一值跑到23.30停止，若不间断运行，可设置runtime='2400' '''
runtime = '2530'

'''设置信封文本内容'''

msg_txt = msgtxt.text