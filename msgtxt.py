texts = [                     "猴子家app是一个新房，短租，二手房的买卖平台，\n"
                            +"这里有丰富的房产资讯，一手的新房，温馨的二手房，还可以电话直联房东哦。\n"
                            +"这是一款二次元租房神器。这里是齐天大圣的家。买房就上猴子家。\n"
                            # + "猴子家下载链接：https://itunes.apple.com/cn/app/%E7%8C%B4%E5%AD%90%E5%AE%B6-%E6%96%B0%E6%88%BF-%E7%9F%AD%E7%A7%9F-%E4%BA%8C%E6%89%8B%E6%88%BF%E7%9A%84%E4%B9%B0%E5%8D%96%E5%B9%B3%E5%8F%B0/id1121556351?mt=8 <br> "
                            + "请关注公众号houzihome，会有惊喜哦！\n "
                            + "看大圣归来，能否再创辉煌！！！",                                #逗号分隔

                            '相遇，在不经意间｡能邂逅你，是我之幸｡\n'
                            +'我因你成长， 为你追问世事，\n'
                            + '而你，却再不问寻天长地久｡\n'
                            + '我因你改变，变成你喜欢的模样，\n'
                            + '而你，却再也不敲击我的心门｡\n'
                            + '我把时光与情意写成文字寄予你，\n'
                            + '而你， 却从未展信｡\n'
                            + '也许，不打扰，即是温柔｡\n'
                            + '所以停笔，将信笺收起。\n'
                            + '但愿，再转身以后，还会相遇...\n'
                            + '我是猴子家，让和你一起成长。',

                            '姑娘，还在为和男朋友吵架而闷闷不乐？买个房子吧，让我们做你最终的安慰。\n'
                            +'姑娘，爱像烟火，怎么热烈缤纷怎么来，而绚烂过后往往是满地碎屑，买个房子吧，让我们握住你的手，给你一生的安全感。\n'
                            +'姑娘，清水煮岁月，不悲不喜，做个远离尘世，安安静静地女子，是毕生的愿望，买个房子吧，他会是你最好的依靠。\n'
                            +'买房就上猴子家。',

                            '怎么确定男生追你是喜欢你还是套路？\n'
                            +'什么是爱情？\n'
                            +'\n'
                            +'没有你\n'
                            +'故事只有两行\n'
                            + "请关注公众号houzihome，会有惊喜哦！\n ",

                            '我爹常说，买房的人有三个阶段：见自己，见天地，见众生。\n'
                            +'我见过自己，也算见过天地，可惜见不到众生。这条路我没走完，希望你能把它走下去。\n'
                            +'买房就上猴子家\n'
                            +'请关注微信公众号：houzihome',

                             '我一直在寻找，有你的世界在哪里。'

                           

 
                            #+'itunes.apple.com/cn/app/%E7%8C%B4%E5%AD%90%E5%AE%B6-%E6%96%B0%E6%88%BF-%E7%9F%AD%E7%A7%9F-%E4%BA%8C%E6%89%8B%E6%88%BF%E7%9A%84%E4%B9%B0%E5%8D%96%E5%B9%B3%E5%8F%B0/id1121556351?mt=8'
                           
                            ]
import time
def gettext(txt):
    now = time.strftime('%m%d', time.localtime(time.time()))
    if int(now) % 2 == 0:
        msg_txt = txt[:3]
    else:
        msg_txt = txt[3:]
    return msg_txt

text = gettext(texts)