# -*- coding=utf-8 -*-
from ctypes import *
VN_FEE_CONSTANT = 0  # 固定手续费
VN_FEE_RATE = 1  # 按比例收取手续费
THOST_FTDC_D_Buy   = '0'   #买
THOST_FTDC_D_Sell  = '1'   #卖
THOST_FTDC_OF_Open = '0'  # 开仓
THOST_FTDC_OF_Close = '1'  # 平仓
THOST_FTDC_OF_CloseToday = 3  # 平今仓
TradeType_ACCOUNT         = 1  #报单给柜台的交易(实盘，simnow仿真等柜台交易)
TradeType_VIRTUALACCOUNT  = 2  #回测用本地虚拟账号



class VNDEFTradingAccountField(Structure):
    _fields_ = [('BrokerID', c_char * 11),  # 经纪公司代码
                ('InvestorID', c_char * 13),  # 投资者代码
                ('Prebalance', c_double),  # 合约代码
                ('Current', c_double),  # 报单引用
                ('Available', c_double),  # 用户代码
                ('Rate', c_double),  # 报单价格条件
                ('Positionrate', c_double),  # 买卖方向
                ('TradingDay', c_char * 9)
                ]

class VNInstrument(Structure):
    _fields_ = [('InstrumentID', c_char * 81)]
    pass

class VNAccount(Structure):
    _fields_ = [('sUserName', c_char * 32),  #服务账号
                ('sPassword', c_char * 64)  #服务密码
                ]
    pass

class VN_CThostFtdcRspInfoField(Structure):
    _fields_ = [('ErrorID', c_int32),  # 错误代码
                ('ErrorMsg', c_char * 81)  # 错误信息
                ]
    pass

class VNStrategy(Structure):
    _fields_ = [('StrategyFileName', c_char * 300), ('StrategyType', c_int)]
    pass



class VNKlineData(Structure):
    _fields_ = [('TradingDay', c_int),
                ('klinetime', c_int),
                #('TradingDay', c_char * 9),
                #('klinetime', c_char * 9),
                ('open', c_double),
                ('high', c_double),
                ('low', c_double),
                ('close', c_double),
                ('volume', c_int32),
                ('money', c_double),
                ('open_interest', c_double),
                ('InstrumentID', c_char * 31),
                ('exchange', c_char * 31),
                ]
    pass


















