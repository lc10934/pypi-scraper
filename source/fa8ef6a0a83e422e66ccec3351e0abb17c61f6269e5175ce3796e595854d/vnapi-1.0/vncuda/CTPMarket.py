# -*- coding=utf-8 -*-
# 官方网站：http://www.vnpy.cn

import time
from CTPMarketType import *
from globalType import *
from ctypes import *
import os.path
import globalvar

global Index

from PyQt5.QtWidgets import QMessageBox

Index = {}


class CTPMarket(object):
    def __init__(self):
        #self.signal_md_tick = signal_md_tick
        currpath = os.path.abspath(os.path.dirname(__file__))
        #self.vnmd = CDLL(currpath + '\\vnctpmd.dll')
        self.vnmd = CDLL('vnctpmd.dll')
        global Index

        '''
        i = 0
        while (i < 5):
            time.sleep(1)
            if (self.vnmd.IsInitOK() == 0):
                i += 1
            else:
                break
        else:
            print('market init error')
            return
        '''
        self.fReqUserLogin = self.vnmd.ReqUserLogin
        self.fReqUserLogin.argtypes = []
        self.fReqUserLogin.restype = c_int32

        self.fReqUserLogout = self.vnmd.ReqUserLogout
        self.fReqUserLogout.argtypes = []
        self.fReqUserLogout.restype = c_int32

        self.fUnSubscribeMarketData = self.vnmd.UnSubscribeMarketData
        self.fUnSubscribeMarketData.argtypes = [c_char_p]
        self.fUnSubscribeMarketData.restype = c_int32

        self.fGetApiVersion = self.vnmd.GetApiVersion
        self.fGetApiVersion.argtypes = []
        self.fGetApiVersion.restype = c_char_p

        self.fGetTradingDay = self.vnmd.GetTradingDay
        self.fGetTradingDay.argtypes = []
        self.fGetTradingDay.restype = c_char_p

        self.fRegisterFront = self.vnmd.RegisterFront
        self.fRegisterFront.argtypes = [c_char_p]

        self.fRegisterNameServer = self.vnmd.RegisterNameServer
        self.fRegisterNameServer.argtypes = [c_char_p]

        self.fSetPrintState = self.vnmd.SetPrintState
        self.fSetPrintState.argtypes = [c_bool]

        self.fGetKlineData = self.vnmd.GetKlineData
        self.fGetKlineData.argtypes = [c_int32]
        self.fGetKlineData.restype = c_void_p

        self.fOpenLog = self.vnmd.OpenLog
        self.fOpenLog.argtypes = []

        self.fCloseLog = self.vnmd.CloseLog
        self.fCloseLog.argtypes = []

        self.fSubscribeMarketData = self.vnmd.SubscribeMarketData
        self.fSubscribeMarketData.argtypes = [c_void_p]
        self.fSubscribeMarketData.restype = c_int32

        self.fSubscribeForQuoteRsp = self.vnmd.SubscribeForQuoteRsp
        self.fSubscribeForQuoteRsp.argtypes = [c_char_p]

        self.InstrumentNum = self.vnmd.GetInstrumentNum()

        self.fInitMD = self.vnmd.InitMD
        self.fInitMD.argtypes = []
        self.fInitMD.restype = c_int32

        self.fLog = self.vnmd.Log
        self.fLog.argtypes = [c_char_p, c_char_p]
        self.fLog.restype = c_void_p

        self.fSetRejectdataTime = self.vnmd.SetRejectdataTime
        self.fSetRejectdataTime.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double,
                                            c_double]
        self.fSetRejectdataTime.restype = c_void_p

        self.fGetKline = self.vnmd.GetKline
        self.fGetKline.argtypes = [c_char_p, c_int32]
        self.fGetKline.restype = c_void_p

        # self.Index = {}#dict()
        '''
        self.InstrumentNum = self.vnmd.GetInstrumentNum()
        self.KlineMaxLen = self.vnmd.GetKlineMaxLen()
        print('InstrumentNum  : ' + str(self.InstrumentNum) + ',' + str(self.KlineMaxLen))

        for i in range(self.InstrumentNum):
            for j in range(self.KlineMaxLen):
                klinedata = self.fGetKlineData(i, j)
                klinedata = cast(klinedata, POINTER(KLineDataType))
                # self.Index[str(data[0].InstrumentID)] = data
                self.Index[str(klinedata[0].InstrumentID)] = klinedata
        pass
        '''

        '''
        self.Index = dict()
        for i in range(self.InstrumentNum):
            data = self.fGetData(i)
            #data = cast(data, POINTER(sDepMarketData))
            self.Index[str(data[0].InstrumentID.encode('gb2312'))] = data
        pass
        '''

        '''
        self.InstrumentNum = self.vnmd.GetInstrumentNum()
        self.Index = dict()
        for i in range(self.InstrumentNum):
            data = self.fGetData(i)
            data = cast(data, POINTER(VNDepMarketData))
            self.Index[str(data[0].InstrumentID)] = data
        pass
        '''

    '''
    def TradingDay(self, InstrumentID):
        # 交易日
        if InstrumentID.encode('gb2312') in self.Index:
            return self.Index[InstrumentID.encode('gb2312')][0].TradingDay
        else:
            return ''

    def InstrumentID(self, InstrumentID):
        # 合约代码
        if InstrumentID.encode('gb2312') in self.Index:
            return self.Index[InstrumentID.encode('gb2312')][0].InstrumentID
        else:
            return ''

    def ExchangeID(self, InstrumentID):
        # 交易所代码
        if InstrumentID.encode('gb2312') in self.Index:
            return self.Index[InstrumentID.encode('gb2312')][0].ExchangeID
        else:
            return ''

    def ExchangeInstID(self, InstrumentID):
        # 合约在交易所的代码
        if InstrumentID.encode('gb2312') in self.Index:
            return self.Index[InstrumentID.encode('gb2312')][0].ExchangeInstID
        else:
            return ''

    def LastPrice(self, InstrumentID):
        # 最新价
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].LastPrice, 1)
        else:
            return -1

    def PreSettlementPrice(self, InstrumentID):
        # 上次结算价
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].PreSettlementPrice, 1)
        else:
            return -1

    def PreClosePrice(self, InstrumentID):
        # 昨收盘
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].PreClosePrice, 1)
        else:
            return -1

    def PreOpenInterest(self, InstrumentID):
        # 昨持仓量
        if InstrumentID.encode('gb2312') in self.Index:
            return self.Index[InstrumentID.encode('gb2312')][0].PreOpenInterest
        else:
            return -1

    def OpenPrice(self, InstrumentID):
        # 今开盘
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].OpenPrice, 1)
        else:
            return -1

    def highestprice(self, InstrumentID):
        # 最高价
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].HighestPrice, 1)
        else:
            return -1

    def LowestPrice(self, InstrumentID):
        # 最低价
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].LowestPrice, 1)
        else:
            return -1

    def Volume(self, InstrumentID):
        # 数量
        if InstrumentID.encode('gb2312') in self.Index:
            return self.Index[InstrumentID.encode('gb2312')][0].Volume
        else:
            return -1

    def Turnover(self, InstrumentID):
        # 成交金额
        if InstrumentID.encode('gb2312') in self.Index:
            return self.Index[InstrumentID.encode('gb2312')][0].Turnover
        else:
            return -1

    def OpenInterest(self, InstrumentID):
        # 持仓量
        if InstrumentID.encode('gb2312') in self.Index:
            return self.Index[InstrumentID.encode('gb2312')][0].OpenInterest
        else:
            return -1

    def ClosePrice(self, InstrumentID):
        # 今收盘
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].ClosePrice, 1)
        else:
            return -1

    def SettlementPrice(self, InstrumentID):
        # 本次结算价
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].SettlementPrice, 1)
        else:
            return -1

    def UpperLimitPrice(self, InstrumentID):
        # 涨停板价
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].UpperLimitPrice, 1)
        else:
            return -1

    def LowerLimitPrice(self, InstrumentID):
        # 跌停板价
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].LowerLimitPrice, 1)
        else:
            return -1

    def PreDelta(self, InstrumentID):
        # 昨虚实度
        if InstrumentID.encode('gb2312') in self.Index:
            return self.Index[InstrumentID.encode('gb2312')][0].PreDelta
        else:
            return -1

    def CurrDelta(self, InstrumentID):
        # 今虚实度
        if InstrumentID.encode('gb2312') in self.Index:
            return self.Index[InstrumentID.encode('gb2312')][0].CurrDelta
        else:
            return -1

    def UpdateTime(self, InstrumentID):
        # 最后修改时间
        if InstrumentID.encode('gb2312') in self.Index:
            return self.Index[InstrumentID.encode('gb2312')][0].UpdateTime
        else:
            return ''

    def UpdateMillisec(self, InstrumentID):
        # 最后修改毫秒
        if InstrumentID.encode('gb2312') in self.Index:
            return self.Index[InstrumentID.encode('gb2312')][0].UpdateMillisec
        else:
            return 0

    def BidPrice1(self, InstrumentID):
        # 申买价一
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].BidPrice1, 1)
        else:
            return -1

    def BidVolume1(self, InstrumentID):
        # 申买量一
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].BidVolume1, 1)
        else:
            return -1

    def AskPrice1(self, InstrumentID):
        # 申卖价一
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].AskPrice1, 1)
        else:
            return -1

    def AskVolume1(self, InstrumentID):
        # 申卖量一
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].AskVolume1, 1)
        else:
            return -1

    def BidPrice2(self, InstrumentID):
        # 申买价二
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].BidPrice2, 1)
        else:
            return -1

    def BidVolume2(self, InstrumentID):
        # 申买量二
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].BidVolume2, 1)
        else:
            return None

    def AskPrice2(self, InstrumentID):
        # 申卖价二
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].AskPrice2, 1)
        else:
            return None

    def AskVolume2(self, InstrumentID):
        # 申卖量二
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].AskVolume2, 1)
        else:
            return None

    def BidPrice3(self, InstrumentID):
        # 申买价三
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].BidPrice3, 1)
        else:
            return None

    def BidVolume3(self, InstrumentID):
        # 申买量三
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].BidVolume3, 1)
        else:
            return None

    def AskPrice3(self, InstrumentID):
        # 申卖价三
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].AskPrice3, 1)
        else:
            return None

    def AskVolume3(self, InstrumentID):
        # 申卖量三
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].AskVolume3, 1)
        else:
            return None

    def BidPrice4(self, InstrumentID):
        # 申买价四
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].BidPrice4, 1)
        else:
            return None

    def BidVolume4(self, InstrumentID):
        # 申买量四
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].BidVolume4, 1)
        else:
            return None

    def AskPrice4(self, InstrumentID):
        # 申卖价四
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].AskPrice4, 1)
        else:
            return None

    def AskVolume4(self, InstrumentID):
        # 申卖量四
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].AskVolume4, 1)
        else:
            return None

    def BidPrice5(self, InstrumentID):
        # 申买价五
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].BidPrice5, 1)
        else:
            return None

    def BidVolume5(self, InstrumentID):
        # 申买量五
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].BidVolume5, 1)
        else:
            return None

    def AskPrice5(self, InstrumentID):
        # 申卖价五
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].AskPrice5, 1)
        else:
            return None

    def AskVolume5(self, InstrumentID):
        # 申卖量五
        if InstrumentID.encode('gb2312') in self.Index:
            return (self.Index[InstrumentID.encode('gb2312')][0].AskVolume5, 1)
        else:
            return None

    def AveragePrice(self, InstrumentID):
        # 当日均价
        if InstrumentID.encode('gb2312') in self.Index:
            return round(self.Index[InstrumentID.encode('gb2312')][0].AveragePrice, 1)
        else:
            return None
    '''

    '''
    def UpdateGetKlineData(self):
        self.InstrumentNum = self.vnmd.GetInstrumentNum()
        self.Index = dict()
        for i in range(self.InstrumentNum):
            data = self.fGetKlineData(i)
            data = cast(data, POINTER(KLineDataType))
            self.Index[str(data[0].InstrumentID)] = data
        pass
    '''

    def GetKline(self, InstrumentID, ID):
        try:
            data = self.fGetKline(InstrumentID.encode("utf-8"),ID)
            return cast(data, POINTER(KLineDataType))
        except Exception as e:
            print("GetKline Error:" + repr(e))

    def GetKline2(self, InstrumentID, ID):
        try:
            print('BBB: '+InstrumentID)

            data = self.fGetKline(InstrumentID.encode("utf-8"), ID)
            # data = self.fGetKline(InstrumentID,ID)
            return cast(data, POINTER(KLineDataType))
        except Exception as e:
            print("GetKline Error:" + repr(e))

    def UpdateGetKlineData(self, InstrumentID):
        linelist = []
        '''
        for k in iter(linelist):
            self.Index[InstrumentID][k] = k
        
        self.Index[InstrumentID]=linelist
        for j in range(self.KlineMaxLen):
            klinedata = self.fGetKlineData(len(self.Index),j)
            klinedata = cast(klinedata, POINTER(KLineDataType))
            #self.Index[InstrumentID][j] = klinedata
            self.Index[InstrumentID].append(klinedata)

        '''

    def KlineM1_InstrumentID(self, InstrumentID, ID):
        print('len: ' + str(len(self.Index)))
        # 交易日
        if InstrumentID in self.Index:
            print('python KlineM1_InstrumentID' + self.Index[InstrumentID][ID].InstrumentID +
                  self.Index[InstrumentID][ID][0].InstrumentID)

            return self.Index[InstrumentID][ID].InstrumentID
        else:
            return ''

    def KlineM1_OpenPrice(self, InstrumentID, ID):
        # 交易日
        if InstrumentID in self.Index:
            return self.Index[InstrumentID][ID].OpenPrice

    # 订阅询价
    def SubscribeForQuoteRsp(self, InstrumentID):
        # 订阅合约时，请注意合约的大小写，中金所和郑州交易所是大写，上海和大连期货交易所是小写的
        self.fSubscribeForQuoteRsp(c_char_p(InstrumentID.encode('gb2312')))
        # data = self.fGetData(len(self.Index))
        # data = cast(data, POINTER(sDepMarketData))
        # self.Index[InstrumentID] = data

    def SubscribeMarketData(self, InstrumentID):
        # 订阅合约时，请注意合约的大小写，中金所和郑州交易所是大写，上海和大连期货交易所是小写的
        try:
            thisInstrumentID = VNInstrument()
            thisInstrumentID.InstrumentID = bytes(InstrumentID, encoding="utf-8")
            result = self.fSubscribeMarketData(byref(thisInstrumentID))
            self.UpdateGetKlineData(InstrumentID)
        except Exception as e:
            globalvar.vnfa.AsynSleep(2000)
            self.SubscribeMarketData(InstrumentID)
        return result

    def UnSubscribeMarketData(self, a):
        # 订阅合约时，请注意合约的大小写，中金所和郑州交易所是大写，上海和大连期货交易所是小写的
        thisInstrumentID = VNInstrument()
        thisInstrumentID.InstrumentID = bytes(a, encoding="utf-8")
        return self.fUnSubscribeMarketData(byref(thisInstrumentID))

    def Log(self, content):
        return self.fLog(content.encode('gb2312'))

    def SetRejectdataTime(self, begintime1, endtime1, begintime2, endtime2, begintime3, endtime3, begintime4, endtime4):
        return self.fSetRejectdataTime(begintime1, endtime1, begintime2, endtime2, begintime3, endtime3, begintime4,
                                       endtime4)

    def ReqUserLogin(self):
        return self.fReqUserLogin()

    def ReqUserLogout(self):
        return self.fReqUserLogout()

    def UnSubscribeMarketData(self, InstrumentID):
        return self.fUnSubscribeMarketData(InstrumentID.encode('gb2312'))

    def SetPrintState(self, printstate):
        return self.fSetPrintState(printstate)

    def GetApiVersion(self):
        return self.fGetApiVersion()

    def GetTradingDay(self):
        return self.fGetTradingDay()

    def RegisterFront(self, pszFrontAddress):
        self.fRegisterFront(pszFrontAddress.encode('gb2312'))

    def RegisterNameServer(self, pszNsAddress):
        self.fRegisterNameServer(pszNsAddress.encode('gb2312'))

    # 建立连接回调
    def OnFrontConnected(self):
        pass

    # 断开连接回调
    def OnFrontDisconnected(self, a):
        pass

    # 登录回调
    def OnRspUserLogin(self, a):
        pass

    # 退出登录回调
    def OnRspUserLogout(self, a):
        pass

    # 行情回调
    def OnRtnDepthMarketData(self, a):
        pass

    # 合约订阅合约回调
    def OnRspSubMarketData(self, a):
        pass

    # 合约反订阅合约回调
    def OnRspUnSubMarketData(self, a):
        pass

    # 注册Python的OnFrontConnected回调函数指针，对应CTP c++的OnFrontConnected方法
    def VNRegOnFrontConnected(self):
        CMPFUNC = CFUNCTYPE(None)
        self.vnmd.VNRegOnFrontConnected(CMPFUNC(self.OnFrontConnected))

    # 注册Python的OnFrontDisconnected回调函数指针，对应CTP c++的OnFrontDisconnected方法
    def VNRegOnFrontDisconnected(self):
        CMPFUNC = CFUNCTYPE(None, c_void_p)
        self.vnmd.VNRegOnFrontDisconnected(CMPFUNC(self.OnFrontDisconnected))

    # 注册Python的OnRspUserLogin回调函数指针，对应CTP c++的OnRspUserLogin方法
    def VNRegOnRspUserLogin(self):
        CMPFUNC = CFUNCTYPE(None, POINTER(VNCThostFtdcRspUserLoginField))
        self.vnmd.VNRegOnRspUserLogin(CMPFUNC(self.OnRspUserLogin))

    # 注册Python的OnRspUserLogout回调函数指针，对应CTP c++的OnRspUserLogout方法
    def VNRegOnRspUserLogout(self):
        CMPFUNC = CFUNCTYPE(None, POINTER(VNCThostFtdcRspUserLoginField))
        self.vnmd.VNRegOnRspUserLogout(CMPFUNC(self.OnRspUserLogout))

    # 注册Python的OnRspSubMarketData回调函数指针，对应CTP c++的OnRspSubMarketData方法
    def VNRegOnRspSubMarketData(self):
        CMPFUNC = CFUNCTYPE(None, POINTER(VNDepMarketData))
        self.vnmd.VNRegOnRspSubMarketData(CMPFUNC(self.OnRspSubMarketData))

    # 注册行情回调
    def VNRegOnRtnDepthMarketData(self):
        CMPFUNC = CFUNCTYPE(None, POINTER(VNDepMarketData))
        self.vnmd.VNRegOnRtnDepthMarketData(CMPFUNC(self.OnRtnDepthMarketData))

    # 注册订阅合约回调
    def VNRegOnRspSubMarketData(self):
        CMPFUNC = CFUNCTYPE(None, POINTER(VNInstrument))
        self.vnmd.VNRegOnRspSubMarketData(CMPFUNC(self.OnRspSubMarketData))

    # 注册反订阅合约回调
    def VNRegOnRspUnSubMarketData(self):
        CMPFUNC = CFUNCTYPE(None, POINTER(VNInstrument))
        self.vnmd.VNRegOnRspUnSubMarketData(CMPFUNC(self.OnRspUnSubMarketData))

    # 注册策略管理
    def VNRegStrategyManager(self):
        pass

    def InitMD(self):
        return self.fInitMD()

    def OpenLog(self):
        self.fOpenLog()

    def CloseLog(self):
        self.fCloseLog()

    # 策略管理
    # 合约反订阅合约回调
    def OnStrategyCalculate(self, a):
        pass

    # 注册反订阅合约回调
    def VNRegOnStrategyCalculate(self, strategyfile):
        currpath = os.path.abspath(os.path.dirname(__file__))
        self.strategyfile = strategyfile
        print('构造策略类：' + self.strategyfile)
        CMPFUNC = CFUNCTYPE(None, POINTER(VNStrategy))
        self.vnmd.VNRegOnStrategyCalculate(CMPFUNC(self.OnStrategyCalculate))

    # 打开策略窗口
    def OpenStrategyProcessWindow(self):
        self.vnmd.OpenStrategyProcessWindow()

    # 关闭策略窗口
    def CloseStrategyProcessWindow(self):
        self.vnmd.CloseStrategyProcessWindow()

    # --------------------------策略管理器----------------------
    '''
    # 注册C++策略管理器的1个进程的句柄
    def VNRegOnStrategyCalculate(self,hwnd):
        self.vnmd.VNRegOnStrategyCalculate222(hwnd)
    '''
    # --------------------------策略管理器----------------------
