# 官方网站：http://www.kucps.com
import threading
import logging
import os
import sys
import configparser
# make the example runnable without the need to install
from os.path import abspath, dirname
sys.path.insert(0, abspath(dirname(abspath(__file__)) + '/..'))
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(os.path.split(rootPath)[0])
print(sys.path)

# CTP行情库
from CTPMarket import *
# CTP交易库
# 导入时间库
import time
from threading import Thread

# MyCTPMarket类继承自CTPMarket类
class MyCTPMarket(CTPMarket):
    global list_INE,list_CFFEX,list_SHFE,list_DCE,list_CZCE
    global dict_exchange, dict_instrument
    def __init__(self):
        super().__init__()

    def UpdateMainType(self, instrumentMain, instrumentName, exchange, jump):
        global tempdate
        returnvalue = 0
        savedate = time.strftime("%Y%m%d", time.localtime())
        tvs = (int(float(savedate) * 0.000001)) * 1000000
        tempdate = int((float(savedate) - float(tvs)) * 0.01)
        tj = 0
        for j in range(12):
            if exchange == 'INE':
                returnvalue = mounthyear4(tempdate, j)
                update_instrument(instrumentMain + str(returnvalue), instrumentName, exchange, jump)
                globalvar.md.SubscribeMarketData(instrumentMain + str(returnvalue))
                if j==0:
                    if len(instrumentMain) > 0:
                        globalvar.set_list_INE(instrumentMain+','+instrumentName+','+exchange)
                globalvar.dict_exchange[instrumentMain + str(returnvalue)] = exchange+',能源所'
                globalvar.dict_instrument[instrumentMain + str(returnvalue)] = instrumentMain+','+instrumentName+','+exchange
            elif exchange == 'CFFEX':
                returnvalue = mounthyear4(tempdate, j)
                update_instrument(instrumentMain + str(returnvalue), instrumentName, exchange, jump)
                globalvar.md.SubscribeMarketData(instrumentMain + str(returnvalue))
                if j==0:
                    if len(instrumentMain) > 0:
                        globalvar.set_list_CFFEX(instrumentMain+','+instrumentName+','+exchange)
                globalvar.dict_exchange[instrumentMain + str(returnvalue)] = exchange+',中金所'
                globalvar.dict_instrument[instrumentMain + str(returnvalue)] = instrumentMain+','+instrumentName+','+exchange
            elif exchange == 'SHFE':
                returnvalue = mounthyear4(tempdate, j)
                update_instrument(instrumentMain + str(returnvalue), instrumentName, exchange, jump)
                globalvar.md.SubscribeMarketData(instrumentMain + str(returnvalue))
                if j==0:
                    if len(instrumentMain) > 0:
                        globalvar.set_list_SHFE(instrumentMain+','+instrumentName+','+exchange)
                globalvar.dict_exchange[instrumentMain + str(returnvalue)] = exchange+',上期所'
                globalvar.dict_instrument[instrumentMain + str(returnvalue)] = instrumentMain+','+instrumentName+','+exchange
            elif exchange == 'DCE':
                returnvalue = mounthyear4(tempdate, j)
                update_instrument(instrumentMain + str(returnvalue), instrumentName, exchange, jump)
                globalvar.md.SubscribeMarketData(instrumentMain + str(returnvalue))
                if j==0:
                    if len(instrumentMain) > 0:
                        globalvar.set_list_DCE(instrumentMain+','+instrumentName+','+exchange)
                globalvar.dict_exchange[instrumentMain + str(returnvalue)] = exchange+',大商所'
                globalvar.dict_instrument[instrumentMain + str(returnvalue)] = instrumentMain+','+instrumentName+','+exchange
            elif exchange == 'CZCE':
                returnvalue = mounthyear3(tempdate, j)
                update_instrument(instrumentMain + str(returnvalue), instrumentName, exchange, jump)
                globalvar.md.SubscribeMarketData(instrumentMain + str(returnvalue))
                if j==0:
                    if len(instrumentMain) > 0:
                        globalvar.set_list_CZCE(instrumentMain+','+instrumentName+','+exchange)
                globalvar.dict_exchange[instrumentMain + str(returnvalue)] = exchange+',郑商所'
                globalvar.dict_instrument[instrumentMain + str(returnvalue)] = instrumentMain+','+instrumentName+','+exchange
        return returnvalue

    def mackinstrumentID(self):
        instrumentidlist = []
        with open('InstrumentID.ini', 'r') as f:
            for line in f:
                instrumentIDarr = line.strip('\n').split(',')
                instrumentidlist.append(list(line.strip('\n').split(',')))
                self.UpdateMainType(instrumentIDarr[1], instrumentIDarr[2], instrumentIDarr[3], instrumentIDarr[4])

        #globalvar.printlist()
        #print("输出list: " + globalvar.list_INE[-1])
        #ui.callback_md_combox()

    def updatehistorystockagain(self,instrument,historystocklist2):
        tempinstrument=instrument
        if  tempinstrument.strip('0123456789')==instrument:
            return
        reagain=0
        if instrument in historystocklist2:
            for i in range(len(historystocklist2)):
                print(historystocklist2 )
                if str(historystocklist2[i])==instrument:
                    historystocklist2.pop(i)
                    reagain=1
                    break
        if reagain==1:
            self.updatehistorystockagain(instrument,historystocklist2)
        else:
            historystocklist2.insert(0,instrument)
            hstr=''
            for i in range(len(historystocklist2)):
                if i < len(historystocklist2) - 1:
                    hstr = hstr + historystocklist2[i] + ','
                else:
                    hstr = hstr + historystocklist2[i]
            with open("historystock.ini", "w") as f:
                f.write(hstr)


    def updatehistorystock(self,instrument):
        tempinstrument=instrument
        if  tempinstrument.strip('0123456789')==instrument:
            return
        reagain=0
        with open('historystock.ini', 'r') as f:
            for line in f:
                historystocklist = line.strip('\n').split(',')
                if instrument in historystocklist:
                    for i in range(len(historystocklist)):
                        if str(historystocklist[i])==instrument:
                            historystocklist.pop(i)
                            reagain=1
                            break
        if reagain==1:
            self.updatehistorystockagain(instrument,historystocklist)
        else:
            historystocklist.insert(0,instrument)
            hstr=''
            for i in range(len(historystocklist)):
                if i<len(historystocklist)-1:
                    hstr=hstr+historystocklist[i]+','
                else:
                    hstr = hstr + historystocklist[i]
            with open("historystock.ini", "w") as f:
                f.write(hstr)



    def ReqUserLogin(self):
        pass
    '''
    #重载
    def KlineM1 (self):
        print("wdg")
        super().KlineM1()
    '''


    def OnRtnDepthMarketData(self, tickdata):
        print("OnRtnDepthMarketData")
        print(str(tickdata[0].InstrumentID, encoding="utf-8")+' , ' +str(tickdata[0].UpdateTime)+' , ' +
              str(tickdata[0].UpdateMillisec)+' , ' +str(tickdata[0].LastPrice) )

    # 合约订阅回调
    def OnRspSubMarketData(self, a):
        print(u'订阅合约成功OnRspSubMarketData'+a.contents.InstrumentID)
        log_todaymd('订阅合约成功OnRspSubMarketData'+a.contents.InstrumentID)

    # 合约订阅回调
    def OnRspUnSubMarketData(self, a):
        print(u'反订阅合约成功OnRspUnSubMarketData'+a.contents.InstrumentID)
        log_todaymd('反订阅合约成功OnRspUnSubMarketData'+a.contents.InstrumentID)

    # 登录回调
    def OnRspUserLogin(self, a):
        # print(a.contents.a1, a.contents.a2)
        print(u'行情登录成功OnRspUserLogin')
        log_todaymd('行情登录成功OnRspUserLogin')
        self.SubscribeMarketData('rb2205')
        #self.mackinstrumentID()
        # 订阅品种zn1610，接收Tick数据,不根据Tick生成其他周期价格数据,但可根据AddPeriod函数添加周期价格数据的设置

    # 退出登录回调
    def OnRspUserLogout(self, a):
        # print(a.contents.a1, a.contents.a2)
        print(u'行情登出成功OnRspUserLogout')
        log_todaymd('行情登出成功OnRspUserLogout')

    # 建立连接回调
    def OnFrontConnected(self):
        print("连接行情服务器成功OnFrontConnected")
        log_todaymd('连接行情服务器成功OnFrontConnected')

    # 断开连接回调
    def OnFrontDisconnected(self, a):
        print("断开与行情服务器连接OnFrontDisconnected")
        log_todaymd('断开与行情服务器连接OnFrontDisconnected')

    def SubscribeMarketData(self, a):
        return CTPMarket().SubscribeMarketData(a)

    def InitMD(self):
        return CTPMarket().InitMD()

    def OpenLog(self):
        return CTPMarket().OpenLog()

    def CloseLog(self):
        return CTPMarket().CloseLog()

    def ReqUserLogin(self):
        return CTPMarket().ReqUserLogin()

    def ReqUserLogout(self):
        return CTPMarket().ReqUserLogout()

class RegTdThreadOnFrontConnected(Thread):
    def __init__(self, name, td):
        super().__init__()
        self.name = name
        self.td = td
    def run(self):
        self.td.VNRegOnFrontConnected()

class RegTdThreadOnFrontDisconnected(Thread):
    def __init__(self, name, td):
        super().__init__()
        self.name = name
        self.td = td
    def run(self):
        self.td.VNRegOnFrontDisconnected()

class RegTdThreadOnRspUserLogin(Thread):
    def __init__(self, name, td):
        super().__init__()
        self.name = name
        self.td = td
    def run(self):
        self.td.VNRegOnRspUserLogin()

class RegTdThreadOnRspUserLogout(Thread):
    def __init__(self, name, td):
        super().__init__()
        self.name = name
        self.td = td
    def run(self):
        self.td.VNRegOnRspUserLogout()

class RegTdThreadOnRspQryInvestorPosition(Thread):
    def __init__(self, name, td):
        super().__init__()
        self.name = name
        self.td = td
    def run(self):
        self.td.VNRegOnRspQryInvestorPosition()


class RegTdThreadOnRspQryTradingAccount(Thread):
    def __init__(self, name, td):
        super().__init__()
        self.name = name
        self.td = td
    def run(self):
        self.td.VNRegOnRspQryTradingAccount()


class RegTdThreadOnRtnOrder(Thread):
    def __init__(self, name, td):
        super().__init__()
        self.name = name
        self.td = td
    def run(self):
        self.td.VNRegOnRtnOrder()

class RegTdThreadOnRtnTrade(Thread):
    def __init__(self, name, td):
        super().__init__()
        self.name = name
        self.td = td
    def run(self):
        self.td.VNRegOnRtnTrade()

# ---------------------------------------
class RegMdThreadOnFrontConnected(Thread):
    def __init__(self, name, md):
        super().__init__()
        self.name = name
        self.md = md
    def run(self):
        self.md.VNRegOnFrontConnected()

class RegMdThreadOnFrontDisconnected(Thread):
    def __init__(self, name, md):
        super().__init__()
        self.name = name
        self.md = md
    def run(self):
        self.md.VNRegOnFrontDisconnected()

# RegThreadTdOnRspUserLogin
class RegMdThreadOnRspUserLogin(Thread):
    def __init__(self, name, md):
        super().__init__()
        self.name = name
        self.md = md
    def run(self):
        self.md.VNRegOnRspUserLogin()


# RegThreadTdOnRspUserLogin
class RegMdThreadOnRspUserLogout(Thread):
    def __init__(self, name, md):
        super().__init__()
        self.name = name
        self.md = md
    def run(self):
        self.md.VNRegOnRspUserLogout()

class RegMdThreadOnRtnDepthMarketData(Thread):
    def __init__(self, name, md):
        super().__init__()
        self.name = name
        self.md = md
    def run(self):
        self.md.VNRegOnRtnDepthMarketData()

class RegMdThreadOnRspSubMarketData(Thread):
    def __init__(self, name, md):
        super().__init__()
        self.name = name
        self.md = md
    def run(self):
        self.md.VNRegOnRspSubMarketData()

class RegMdThreadOnRspUnSubMarketData(Thread):
    def __init__(self, name, md):
        super().__init__()
        self.name = name
        self.md = md
    def run(self):
        self.md.VNRegOnRspUnSubMarketData()




instrumenttableid=0
def update_instrument(instrumentID,instrumentName,exchange,jump):
    pass



import os
# https://www.cnblogs.com/AmyHu/p/10654500.html
# https://blog.csdn.net/edward_zcl/article/details/88809212


import importlib
def dynamic_import(module):
    return importlib.import_module(module)


import globalvar
globalvar._init()


def log_todaymd(mystr):
    print(mystr)

global tempdata
thisdate = 0
global savedate
def mounthyear4(thisdate,add):
    year = (int)(thisdate*0.01)
    mounth =  thisdate - year * 100
    mounth = mounth+add
    if mounth > 12:
        mounth = mounth-12
        year = year + 1
    thisdate = year * 100 + mounth
    return thisdate

def mounthyear3(thisdate,add):
    year = (int)(thisdate*0.01)
    y= (int)(thisdate*0.001)
    mounth =  thisdate - year * 100
    mounth = mounth+add
    if mounth > 12:
        mounth = mounth-12
        year = year + 1
    thisdate = year * 100 + mounth
    thisdate=thisdate-1000*y
    return thisdate

def function_md(md):
    #注册异步回调函数线程（多线程回调，可绕过GIL锁）
    RegMdThreadOnFrontConnected('OnFrontConnected', md).start()
    RegMdThreadOnFrontDisconnected('OnFrontDisconnected', md).start()
    RegMdThreadOnRspUserLogin('OnRspUserLogin', md).start()
    RegMdThreadOnRspUserLogout('OnRspUserLogout', md).start()
    RegMdThreadOnRtnDepthMarketData('OnRtnDepthMarketData', md).start()
    RegMdThreadOnRspSubMarketData('OnRspSubMarketData', md).start()
    RegMdThreadOnRspUnSubMarketData('OnRspUnSubMarketData', md).start()

    time.sleep(1)
    result= md.InitMD()
    print("mdresult:"+str(result))

    if result == 0:
        log_todaymd('行情接口配置文件读取成功')
    elif result == 1:
        log_todaymd('行情接口配置文件读取错误，请检查vnctpmd.ini是否存在')
        return
    elif result == 2:
        log_todaymd('行情接口配置文件读取错误，请检查vnctpmd.ini配置文件至少要配置一个行情IP地址')
        return

    #mackinstrumentID()
    # md.RegisterFront()
    # Login()，不需要参数，Login读取QuickLibTD.ini的配置信息，并登录
    # 返回0， 表示登录成功，
    # 返回1， FutureTDAccount.ini错误
    # 返回2， 登录超时
    # 第一次是自动登录，退出登录后，如需再登陆，需添加以下登陆代码
    # 调用交易接口元素，通过 “ 接口变量.元素（接口类内部定义的方法或变量） ” 形式调用
    # Login()，不需要参数，Login读取QuickLibTD.ini的配置信息，并登录
    # 返回0， 表示登录成功，
    # 返回1， FutureTDAccount.ini错误
    # 返回2， 登录超时
    # print ('login: ', retLogin)

    # if md.Login() == 0:
    if md.ReqUserLogin() == 0:
        log_todaymd('发送登录行情服务器请求成功')
    else:
        log_todaymd('发送登录行情服务器请求失败')
    while 1:
        #会一直循环执行，可在这个循环内需增加策略判断，达到下单条件即可下单
        time.sleep(30)  # 系统休眠

def getctpdata():
    class MDThread(Thread):
        def __init__(self, tname):
            super(MDThread, self).__init__()
            self.tname = tname
        def run(self):
            time.sleep(3)
            globalvar.md = MyCTPMarket()
            function_md(globalvar.md)
    tm = MDThread('tm')
    tm.start()


def main():
    getctpdata()


if __name__ == "__main__":
    main()
