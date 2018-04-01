#encoding:utf-8
from datetime import datetime

class ipaddr:
    def __init__(self):
        self.iptime=""
        self.indexi=-1
        self.indexj=-1

data=[]     #数据
urls=[]
browsers=[]
ips={}
label=[]    #标签（0正常，1DDos，2爆破，3撞库
f = open("access.log", "rb")    # 返回一个文件对象
line = f.readline()             # 调用文件的 readline()方法

def findurls(url):
    for i in range(len(urls)):
        if (url==urls[i]):
            return i
    return -1

def trun_person(p,index,dt,num_url,num_browser):
    #时间
    str='{0:011b}'.format(dt)
    for i in range(index*28,index*28+11):
        p[i]=int(str[i-index*28],10)
    str = '{0:06b}'.format(num_url)
    for i in range(index*28+12,index*28+17):
        p[i]=int(str[i-index*28-12],10)
    str = '{0:011b}'.format(num_browser)
    for i in range(index * 28 + 18, index * 28 + 28):
        p[i]=int(str[i-index*28-18],10)

def tran_time(stime):
    stime = stime.replace("Jan", "01")
    stime = stime.replace("Feb", "02")
    stime = stime.replace("Mar", "03")
    stime = stime.replace("Apr", "04")
    stime = stime.replace("May", "05")
    stime = stime.replace("Jun", "06")
    stime = stime.replace("July", "07")
    stime = stime.replace("Aug", "08")
    stime = stime.replace("Sept", "09")
    stime = stime.replace("Oct", "10")
    stime = stime.replace("Nov", "11")
    stime = stime.replace("Dec", "12")
    t = datetime.strptime(stime, '%d/%m/%Y:%H:%M:%S')
    return t


def def_lebel(ip,time,browser):
    strtime=["28/Feb/2018:13:02:00","28/Feb/2018:13:16:57",
             "01/Mar/2018:21:18:11","01/Mar/2018:21:55:02",
             "07/Mar/2018:22:43:16","07/Mar/2018:22:45:35",
             "11/Mar/2018:20:44:02","11/Mar/2018:20:46:59",
             "02/Mar/2018:20:00:35","02/Mar/2018:21:17:31",
             "27/Feb/2018:22:23:35","27/Feb/2018:23:06:38",
             "11/Mar/2018:19:48:22","11/Mar/2018:19:48:51",
             "11/Mar/2018:23:25:26","11/Mar/2018:23:27:21",
             "12/Mar/2018:22:54:37","12/Mar/2018:23:06:53",
             "03/Mar/2018:00:35:55","03/Mar/2018:09:00:38",
             "03/Mar/2018:15:49:04","03/Mar/2018:18:46:24",
             "03/Mar/2018:20:00:58","03/Mar/2018:21:54:32",
             "11/Mar/2018:23:26:59","11/Mar/2018:23:52:42",
             "11/Mar/2018:23:56:32","12/Mar/2018:00:12:28"]
    ttime=[]
    for i in range(len(strtime)):
        ttime.append(tran_time(strtime[i]))
    if (ip=="49.77.173.26" and (time-ttime[0]).total_seconds()>0 and (time-ttime[1]).total_seconds()<0):
        return [0,1,0,0,0,0,0,0,0,0]
    if (ip=="49.77.173.26" and (time-ttime[2]).total_seconds()>0 and (time-ttime[3]).total_seconds()<0):
        return [0,1,0,0,0,0,0,0,0,0]
    if (ip=="185.29.9.195" and (time-ttime[4]).total_seconds()>0 and (time-ttime[5]).total_seconds()<0):
        return [0,1,0,0,0,0,0,0,0,0]
    if (ip=="121.237.98.247" and (time-ttime[6]).total_seconds()>0 and (time-ttime[7]).total_seconds()<0):
        return [0,1,0,0,0,0,0,0,0,0]
    if (ip=="223.3.163.195" and (time-ttime[8]).total_seconds()>0 and (time-ttime[9]).total_seconds()<0):
        return [0,1,0,0,0,0,0,0,0,0]
    if (ip=="223.3.170.60" and (time-ttime[10]).total_seconds()>0 and (time-ttime[11]).total_seconds()<0):
        return [0,1,0,0,0,0,0,0,0,0]
    if (ip=="223.3.185.19" and (time-ttime[12]).total_seconds()>0 and (time-ttime[13]).total_seconds()<0):
        return [0,1,0,0,0,0,0,0,0,0]
    if (ip=="223.3.185.19" and (time-ttime[14]).total_seconds()>0 and (time-ttime[15]).total_seconds()<0):
        return [0,1,0,0,0,0,0,0,0,0]
    if (ip=="122.96.40.148" and (time-ttime[16]).total_seconds()>0 and (time-ttime[17]).total_seconds()<0):
        return [0,1,0,0,0,0,0,0,0,0]
    if (ip=="223.3.163.195" and (time-ttime[18]).total_seconds()>0 and (time-ttime[19]).total_seconds()<0 and browser.find("Firefox/58.0")!=-1):
        return [0,0,1,0,0,0,0,0,0,0]
    if (ip=="223.3.111.21" and (time-ttime[20]).total_seconds()>0 and (time-ttime[21]).total_seconds()<0 and browser.find("Firefox/58.0")!=-1):
        return [0,0,0,1,0,0,0,0,0,0]
    if (ip=="223.3.111.21" and (time-ttime[22]).total_seconds()>0 and (time-ttime[23]).total_seconds()<0 and browser.find("Firefox/58.0")!=-1):
        return [0,0,0,1,0,0,0,0,0,0]
    if (ip=="223.3.185.19" and (time-ttime[24]).total_seconds()>0 and (time-ttime[25]).total_seconds()<0 and browser.find("Firefox/58.0")!=-1):
        return [0,0,0,1,0,0,0,0,0,0]
    if (ip=="223.3.173.50" and (time-ttime[26]).total_seconds()>0 and (time-ttime[27]).total_seconds()<0):
        return [0,0,0,1,0,0,0,0,0,0]
    return [1,0,0,0,0,0,0,0,0,0]

while line:
    fline=str(line)

    #IP
    list=fline.split(" - ")
    ip=list[0]

    #访问时间
    st=list[1].find("[")
    ed=list[1].find("]")
    stime=list[1][st+1:ed]
    stime=stime.split(" ")[0]
    t=tran_time(stime)
    #访问url
    st=list[1].find("\"")
    ed=list[1].find("\"",st+1,st+300)
    strll=list[1][st+1:ed]
    if strll.find(" ")!=-1:
        strlist=strll.split(" ")
        method=strlist[0]
        url=strlist[1]

        #浏览器
        ed=list[1].rfind("\"")
        st=list[1].rfind("\"",0,ed-1);
        browser=list[1][st+1:ed]

        if url.find("jsp")!=-1 or url.find("html")!=-1 or url.find("action")!=-1:
            #添加到数组
            flag=1
            for i in range(len(urls)):
                if (urls[i]==url):
                    flag=0
                    break
            if (flag): urls.append(url)

            if (ips.has_key(ip)):
                pid=ips[ip]
                dt=(t-pid.iptime).seconds
                if (dt<1800):
                    if (pid.indexj<28):
                        trun_person(data[pid.indexi],pid.indexj,dt,findurls(url),hash(browser)%1007)
                        tlabel=def_lebel(ip,t,browser)
                        if (tlabel!=label[pid.indexi] and label[pid.indexi][0]==1):
                            label[pid.indexi]=tlabel
                    else:
                        person = [0 for i in range(784)]
                        trun_person(person, 0, 0, findurls(url), hash(browser) % 1007)
                        pid = ipaddr()
                        pid.iptime = t
                        pid.indexi = len(ips)
                        pid.indexj = 1
                        ips[ip] = pid
                        data.append(person)
                        label.append(def_lebel(ip, t, browser))
                else:
                    person = [0 for i in range(784)]
                    trun_person(person, 0, 0, findurls(url), hash(browser) % 1007)
                    pid = ipaddr()
                    pid.iptime = t
                    pid.indexi = len(ips)
                    pid.indexj = 1
                    ips[ip] = pid
                    data.append(person)
                    label.append(def_lebel(ip,t,browser))
            else:
                person=[0 for i in range(784)]
                trun_person(person,0,0,findurls(url),hash(browser)%1007)
                pid=ipaddr()
                pid.iptime=t
                pid.indexi=len(ips)
                pid.indexj=1
                ips[ip]=pid
                data.append(person)
                label.append(def_lebel(ip, t, browser))


    line = f.readline()

f.close()