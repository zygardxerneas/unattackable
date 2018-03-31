#encoding:utf-8
import time

data=[]
f = open("access.log", "rb")    # 返回一个文件对象
line = f.readline()             # 调用文件的 readline()方法
while line:
    fline=str(line)

    list=fline.split(" - ")
    ip=list[0]

    st=list[1].find("[")
    ed=list[1].find("]")

    stime=list[1][st+1:ed]
    stime=stime.split(" ")[0]
    stime=stime.replace("Jan", "01")
    stime=stime.replace("Feb", "02")
    stime=stime.replace("Mar", "03")
    stime=stime.replace("Apr", "04")
    stime=stime.replace("May", "05")
    stime=stime.replace("Jun", "06")
    stime=stime.replace("July", "07")
    stime=stime.replace("Aug", "08")
    stime=stime.replace("Sept", "09")
    stime=stime.replace("Oct", "10")
    stime=stime.replace("Nov", "11")
    stime=stime.replace("Dec", "12")
    t=time.strptime(stime,'%d/%m/%Y:%H:%M:%S')


    st=list[1].find("\"")
    ed=list[1].find("\"",st+1,st+300)
    strll=list[1][st+1:ed]
    if strll.find(" ")!=-1:
        strlist=strll.split(" ")
        method=strlist[0]
        url=strlist[1]

        ed=list[1].rfind("\"")
        st=list[1].rfind("\"",0,ed-1);
        browser=list[1][st+1:ed]

        if url.find("jsp")!=-1 or url.find("html")!=-1 or url.find("action")!=-1:
            #添加到数组
            data.append(ip)

    line = f.readline()

f.close()