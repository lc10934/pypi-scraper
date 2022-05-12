# -*- coding: utf-8 -*-
import os
# 本页面用于多个py文件之间共享全局变量
global ui
pool = 0
pool2 = 0
gui=0
csvfile=''
tdinit=False
mdinit=False
totaltasknum = 0
finishtasknum = 0
DialogBackTestPoint=0
BackTestThreadPoint=0
#存储合约组的交易的合约
list_instrumentgroupenable = [{},{},{},{},{},{},{},{},{},{},{}]
#屏蔽第一次K线更新
notfirstupdateklineUi=False
#存储Talib公式条件
dict_talibcondition = {}
#设置Talib窗口打开状态
DialogTalibState=False
#设置合约的窗口打开状态
DialogSetInstrumentState=False
#过滤规则窗口打开状态
DialogSetRuleState =False
dict_position = {}
dict_order = {}
dict_trader = {}
# 只有 data_kline_M1  (M1周期数据)是从服务器获取或实时生成
# 其他周期K线数据是通过Python的Pandas本地合成
# 本地生成数据包括 data_kline_M3、data_kline_M5、data_kline_M10、data_kline_M15、data_kline_M30、data_kline_M60、data_kline_M120、data_kline_D1
# 字段分别为 ID,Data,Time,Open,Close,Low,High
# 调用方式如下
# print("data_kline_M1: " + str(data_kline_M1))
# print("data_kline_M1: " + str(data_kline_M1[0]))
# print("data_kline_M1: " + str(data_kline_M1[1]))
# print("data_kline_M1: " + str(data_kline_M1[2]))
# print("data_kline_M11: " + str(data_kline_M1[2][1]))
# print("data_kline_M12: " + str(data_kline_M1[2][2]))
# 保存订阅的合约的数据， 取值方法 dict_data_kline_M1['ag2110']
dict_dataframe_kline_M1 = {}
dict_dataframe_kline_M3 = {}
dict_dataframe_kline_M5 = {}
dict_dataframe_kline_M10 = {}
dict_dataframe_kline_M15 = {}
dict_dataframe_kline_M30 = {}
dict_dataframe_kline_M60 = {}
dict_dataframe_kline_M120 = {}
dict_dataframe_kline_D1 = {}
# 显示的K线图的个周期数据
data_kline_M1 = []
data_kline_M3 = []
data_kline_M5 = []
data_kline_M10 = []
data_kline_M15 = []
data_kline_M30 = []
data_kline_M60 = []
data_kline_M120 = []
data_kline_D1 = []
global ticklist
ticklist = []
# VNPY官方Plus服务账号
global Plus_UserName, Plus_Password
Plus_UserName = "admin"
Plus_Password = "000000"
# 认证用户权限
global PlusAuthState
# K线数据模式，0实时TICK生成K线，1从服务器补齐当日K线，2从服务器补齐多日K线（需Plus会员）
global klineserverstate
# 用于保存选择框变量
global list_INE, list_CFFEX, list_SHFE, list_DCE, list_CZCE
global dict_exchange, dict_instrument
global tradestate, thistoday,backteststate
# 保存策略执行的合约编码
global dict_strategyinstrument
# 保存当前pygraph K线图、闪电图选中选中合约对应的交易所，合约编码，周期
global selectperiod, selectexchange, selectinstrumenid
# 实例化交易库和行情库作为全局遍历保存
global td, md, rc, vk, currpath
currpath = os.path.abspath(os.path.dirname(__file__))
td = 0
md = 0
rc = 0
vk = 0
selectinstrumenid = '1'
selectperiod = 1


def _init():  # 初始化
    global PlusAuthState
    PlusAuthState = 0
    global klineserverstate
    klineserverstate = 0
    global tradestate, thistoday,backteststate
    thistoday = 0
    tradestate = 0
    backteststate = 0
    global td, md, rc, vk, currpath
    global list_INE, list_CFFEX, list_SHFE, list_DCE, list_CZCE, selectperiod, selectexchange, selectinstrumenid
    global dict_strategyinstrument
    list_INE = []
    list_CFFEX = []
    list_SHFE = []
    list_DCE = []
    list_CZCE = []
    global dict_exchange, dict_instrument
    dict_exchange = {}
    dict_instrument = {}
    dict_strategyinstrument = {}
    global _global_dict
    _global_dict = {}


def caompareinstrumwent(InstrumentID):
    global selectinstrumenid
    # print(selectinstrumenid+', '+InstrumentID)
    if selectinstrumenid == InstrumentID:
        return True
    else:
        return False


def set_value(key, value):
    """ 定义一个全局变量 """
    _global_dict[key] = value


def get_value(key, defValue=None):
    """ 获得一个全局变量,不存在则返回默认值 """
    try:
        return _global_dict[key]
    except:
        pass
        # KeyError


def set_list_INE(value):
    """ 定义一个全局变量 """
    # list_INE[id] = value
    list_INE.append(value)


def get_list_INE(id, defValue=None):
    """ 获得一个全局变量,不存在则返回默认值 """
    try:
        return list_INE[id]
    except:
        pass
        # KeyError


def getlen_list_INE():
    return len(list_INE)


def set_list_CFFEX(value):
    """ 定义一个全局变量 """
    list_CFFEX.append(value)


def get_list_CFFEX(id, defValue=None):
    """ 获得一个全局变量,不存在则返回默认值 """
    try:
        return list_CFFEX[id]
    except:
        pass
        # KeyError


def getlen_list_CFFEX():
    return len(list_CFFEX)


def set_list_SHFE(value):
    """ 定义一个全局变量 """
    list_SHFE.append(value)


def get_list_SHFE(id, defValue=None):
    """ 获得一个全局变量,不存在则返回默认值 """
    try:
        return list_SHFE[id]
    except:
        pass
        # KeyError


def getlen_list_SHFE():
    return len(list_SHFE)


def set_list_DCE(value):
    """ 定义一个全局变量 """
    list_DCE.append(value)


def get_list_DCE(id, defValue=None):
    """ 获得一个全局变量,不存在则返回默认值 """
    try:
        return list_DCE[id]
    except:
        pass
        # KeyError


def getlen_list_DCE():
    return len(list_DCE)


def set_list_CZCE(value):
    """ 定义一个全局变量 """
    list_CZCE.append(value)


def get_list_CZCE(id, defValue=None):
    """ 获得一个全局变量,不存在则返回默认值 """
    try:
        return list_CZCE[id]
    except:
        pass
        # KeyError


def getlen_list_CZCE():
    return len(list_CZCE)


TRADINGDATE = 0
KLINETIME = 1
INSTRUMENT = 2
OPEN = 3
CLOSE = 4
LOW = 5
HIGH = 6
VOL = 7
