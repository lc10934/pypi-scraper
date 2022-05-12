#### 关注支持VNPY的4件事

1.右上角Fork和Star代码

2.关注VNPY官方社区  https://q.vnpy.cn 常见技术问题

3.关注VNPY官方微信公众号，扫描下方微信二维码，或微信搜“VNPY官方”

![VNPY](https://images.gitee.com/uploads/images/2021/1127/144239_33e658b5_1204097.png "vnpyf2.png")

![挖掘VNPY开源量化交易软件6个功能特点](https://images.gitee.com/uploads/images/2022/0124/055820_4b1ee516_9312679.png "vnpyf2.png")

![谈谈VNPY量化交易回测过程视图](https://images.gitee.com/uploads/images/2022/0124/060424_423a0cd2_9312679.png "介绍2x3.png")
#### 介绍
VNPY是VNPY官方 http://www.vnpy.cn 推出的一款国内期货量化交易开源软件，
VNPY 属于 上海量贝信息科技有限公司是国内运用全面的开源量化交易框架。 我司上海量贝信息科技有限公司是中国大陆从事量化相关软件的信息和软件服务企业，公司位于上海，在国内市场，我们的客户定位包括个人量化交易爱好者、高校、证券公司、基金管理公司、银行和投资公司等金融企业。 

精于量化，以回测为起点，VNPY官方系列量化交易软件产品紧密跟随金融市场日新月异的发展，不断向新的领域发展，新的产品和服务战略不断在延伸,在金融领域，我司已建成完整的产品系列 。

下图为VNPY窗口，代码开源


![VNPY主界面窗口](https://images.gitee.com/uploads/images/2021/1203/111218_1a1fab6e_1204097.jpeg  "backtest2.jpeg ")

回测过程中，双击参数记录，即可显示该参数组的资金曲线

 登录点击上方“FORK”按钮 ，选择FORK。
开源托管页面： https://gitee.com/vnpypro/vnpy

《CTP接口视频课程》
http://www.vnpy.cn/course/1ctp/

《VNPY运行演示视频》
http://www.vnpy.cn/course/2vnpy/

加入VNHub量化社区，开立个人量化专栏

https://www.vnhub.cn

![输入图片说明](https://images.gitee.com/uploads/images/2022/0315/104501_d04526bd_9312679.png "vnhub社区2.png")

目前VNPY经过不断迭代，经过众人努力，已不断更新成熟。使用GIT工具更新更方便。

 QQ群：256163463

VNPY官方微信公众号

![VNPY3.0微信公众号](https://images.gitee.com/uploads/images/2021/1127/144239_33e658b5_1204097.png   "backtest2.jpeg ")

VNPY开源版本，开发环境安装建议采用PyCharm+Anacanda配置环境。
VNPY 需要的插件有：
PyQT5,pyqtgraph,numpy,pandas,Talib
除了Talib以外，Anacanda默认base配置已包含了这些插件，无需再安装。
由于Anacanda内置了Python环境，也无需自己安装Python。
可以理解为Anacanda 是一个Python安装包的超集，并且做到了插件之间的兼容性，推荐使用。
talib安装包下载 ： https://www.ta-lib.org/hdr_dw.html
其他参考文章
1. 《VNPY开发环境快速入门教程》
2. 《VNPY新手常见问题说明》
3. 《VNPY3.0 架构图》
4. 《VNPY策略自动生成回测文件功能代码解析》
5. 《VNPY3.0以后版本为什么不用数据库设计架构？》
6. 《VNPY3.0行情数据调用的5种方式 》

以上6篇都在这个链接 https://q.vnpy.cn/comm/thread-13-1-1.html

如果对我们开源项目支持，就请点击上方的“Fork”按钮。
为及时更新代码，推荐使用Gitdesktop软件差异更新项目，这样就不用每次下载压缩包了。 
《VNTrader开源项目采用Github Desktop差异更新代码步骤》
https://zhuanlan.zhihu.com/p/386181364

VNPY官网
http://www.vnpy.cn
VNTA 证券和期货方案
http://www.vnta.cn

# VNPY官方 VNTrader 
（基于期货CTP接口专用量化交易开源软件）

《VNPY官方发布VNTrader期货CTP框架开发环境配置快速入门教程》 
https://zhuanlan.zhihu.com/p/388316382

![VNPY架构图](https://images.gitee.com/uploads/images/2022/0124/061407_10328538_9312679.png "23525.png")

关于VNPY的架构
Python在2022年已经位于编程语言排行榜第一名，得益于这几年量化交易、大数据、人工智能等技术的发展。金融工程等专业，在校期间学习的就是Python语言，所以无论从招聘专业人才的角度、或是对开发效率的要求，都首选Python语言。Python在量化交易领域，专业机构已经接近90%采用Python开发量化策略。

虽然Python并不是完美的，而我们选择一门编程语言，是因为他的优点，Python结合底层C++开发弥补了Python的缺点，通过C++封装的DLL文件，成为原生CTP API的桥梁。通过Python向C++ DLL注册一个回调函数，可以做到由C++回调触发Python的回调。也不像C++调用Python那样只针对某一个Python版本。
在数据上，我们摒弃了数据库，因为经过测试CSV的读取性能是MSSQL这类关系型数据库的100倍，即便是时间序列数据库和NOSQL也远不及csv文件的读取速度，更快的性能，发璞归真，简化开发环境是VNPY3.0以后版本采用csv文件存储数据的理由。



#### 目录说明：

strategy  策略存放目录
temp CTP接口产生的临时流文件存放目录
setting.ini 账户和服务器配置文件




![输入图片说明](https://images.gitee.com/uploads/images/2022/0124/061738_f8f2b7a3_9312679.png "13.png")
####上期CTP原生API
1.  thostmduserapi_se.dll                CTP接口原生行情接口，在VNPY客户端代码中
2.  thosttraderapi_se.dll                  CTP接口原生交易接口，在VNPY客户端代码中
3.  thostmduserapi_se.lib                仅存在于编译vnctpmd.dll 的C++代码中
4.  thosttraderapi_se.lib                  仅存在于编译vnctpmd.dll 的C++代码中
5.  ThostFtdcMdApi.h                     仅存在于编译vnctpmd.dll 和vnctptd.dll的C++代码中
6.  ThostFtdcTraderApi.h                仅存在于编译vnctpmd.dll 和vnctptd.dll的C++代码中
7.  ThostFtdcUserApiDataType.h    仅存在于编译vnctpmd.dll 和vnctptd.dll的C++代码中
8.  ThostFtdcUserApiStruct.h          仅存在于编译vnctpmd.dll 和vnctptd.dll的C++代码中

![输入图片说明](https://images.gitee.com/uploads/images/2022/0124/061738_f8f2b7a3_9312679.png "13.png")
####VNPY模块
以下文件都在VNPY客户端代码中
1.   建议双击VNTrader.py打开项目

VNTrader.py  启动程序，包含了入口方法main()  ，
注意项目目录下有一个.idea目录，这是PyCharm（IDE）读取的配置文件，主要配置了 ui.example_pyqt5_ui.py路径，要读到.idea，这样是以 VNTrader.py 为父进程，而不是IDE为父进程 。

，这时VNTrader.py进程才是父进程，他才会从这个VNTrader.py路径作为根目录读取模块和配置文件。

正确启动VNPY程序做法： 在未运行IDE（比如Pycharm）时，用双击VNTrader.py的方式启动Pycharm （操作系统会把VNTrader.py作为父进程，读取VNTrader.py目录下的.idea目录配置文件，以及所有该目录下的文件）。

还有一个不推荐的办法：就是配置 Windows全局系统环境path字段，但不推荐这个方法，因为插件太多，处理太麻烦，而且每个运行项目的电脑都要设置。
ui.example_pyqt5_ui  文件路径为：VNTrader(CTP6.6.1)\QDarkStyleSheet-master\example\ui\example_pyqt5_ui.py

 
1.  module_backtest.py                        
2.  module_backtestreport.py
3.  module_backtestwindow.py
4.  module_combinekline.py
5.  module_config.py
6.  module_instrumentgroup.py
7.  module_kline.py
8.  module_md.py
9.  module_myindicatrix.py
10.  module_strategy.py
11.  module_strategybacktestprocess.py
12.  module_strategyprocess.py
13.  module_talib.py
14.  module_td.py

![VNPY ctp api说明](https://images.gitee.com/uploads/images/2022/0124/061738_f8f2b7a3_9312679.png "13.png")
####Ctypes技术开发的代理DLL（代码开源）
以下文件都在VNPY客户端代码中
1.  vnctpmd.py      Python ctypes 方式封装；
2.  vnctpmd.dll      CTP接口原生交易接口的代理库，用于和ctypes方式封装的CTPMarket.py 引用；
3.  vnctpmd.ini
4.  vnctptd.py        Python ctypes 方式封装；
5.  vnctptd.dll        CTP接口原生交易接口的代理库，用于和ctypes方式封装的CTPTrader 引用；
6.  vnctptd.ini
7.  vnctpmdType661.py    Python类型定义,对应CTP6.6.1版本；
8.  vnctptdType661.py     Python类型定义, 对应CTP6.6.1版本；

![输入图片说明](https://images.gitee.com/uploads/images/2022/0124/061738_f8f2b7a3_9312679.png "13.png")
####K线补齐服务（可选服务，该API可独立使用）
以下文件都在VNPY客户端代码中，因为用到SSL，依赖的库需要安装VC2013运行时库64位版本，否则提示找不到vnklineservice.dll
1.  vnklineservice.py
2.  vnklineservice.dll
3.  vnklineservice.ini


基于GPLV3开源协议，任何机构和个人可以免费下载和使用，无需付费。

注意，需要在期货开盘时间前后20分钟，放开登录CTP接口服务器
期货开盘时间  9:00-11:30   ,1:30 - 15:00   ,  21:00-2:30

仿真账户支持 (支持股指期货、股指期权、商品期货、商品期权仿真交易)
 (只能工作日白天访问网址，其他时间网站关闭)
http://www.simnow.com.cn


基于CTP接口的开源性，打破收费软件垄断，采用VNTrader开源项目也可解决自己造轮子导致周期长门槛高的问题。
VNTrader是专门针对商品期货CTP接口的GUI窗口程序，支持多个Python策略组成策略池，支持回测，支持多周期量化交易。

注意目前行情服务器市SIMNOW仿真，所以数据可能不对，8月底会将实时行情K线服务和SIMNOW分开服务。

VNPY官方提供的CTP开源项目客户端源代码，
支持国内149家期货公司的CTP接入，
支持股指期货，股指期权、商品期货、商品期权的程序化交易和量化交易的仿真回测。

全新架构，性能再次升级，python的便捷,C++性能加持，比老版本更好用，性能大幅提升， 属于VNPY官方发布的重点全新架构的产品。


VNTrader的Python和底层C++代码全部开源， 这个是一个有具大性能提升大版本


VNPY官方网站 http://www.vnpy.cn 

 


![VNPY官方发布全新一代期货CTP框架，Python框架VNTrader](https://images.gitee.com/uploads/images/2021/0624/111454_46c70c7a_1204097.png "VNPY.png")


![输入图片说明](https://images.gitee.com/uploads/images/2021/0624/111503_6980ce37_1204097.jpeg "bird.jpg")


![CTP接口支持交易和期货公司](https://images.gitee.com/uploads/images/2021/0624/112928_eea13eb4_1204097.png "s1.png")

![VNTrader CTP接口Python开源框架架构图](https://images.gitee.com/uploads/images/2021/0624/112936_c222d986_1204097.png "S2.png")

![输入图片说明](https://images.gitee.com/uploads/images/2021/1029/110827_fc2c8df4_1204097.png "window.png")

![VNTrader委托记录，成交记录，持仓记录](https://images.gitee.com/uploads/images/2021/0624/143814_4ecd69e6_1204097.png "S4.png")

![VNTrader期货账户详情](https://images.gitee.com/uploads/images/2021/0624/143826_1afee0ca_1204097.png "S5.png")

![VNTrader添加期货账户](https://images.gitee.com/uploads/images/2021/0624/143835_563f3c7c_1204097.png "S6.png")

![VNTrader资金曲线记录](https://images.gitee.com/uploads/images/2021/0624/143905_68094eda_1204097.png "S8.png")

![VNPY商标证](https://images.gitee.com/uploads/images/2022/0226/102737_b3146c7e_9312679.jpeg "商标1.jpg")

![输入图片说明](https://images.gitee.com/uploads/images/2022/0226/102912_801ea207_9312679.jpeg "商标4.jpg")
重点：
在未来 VNTrader 将继承http://www.virtualapi.cn 的强大功能，具体可以见 http://www.gucps.cn
完全不同于历史老版本，这个版本不仅性能优异，开源，而且结合C++的特点，结合底层仿真（获得国家发明专利）成为程序化交易最佳利器。

抛弃历史曾出现的大杂烩版本，专门面向国内商品期货、股指期货实现程序化交易CTP接口的专属版本，符合“精简、高性能、精细化回测、功能强大、入门更容易”等特点。




#### 软件架构
软件架构说明

需要安装的模块
Python3.0 + PyQT5 + numpy+ pandas + qdarkstyle+pyqtgraph 


python下载

https://www.python.org/

Pycharm下载

https://www.jetbrains.com/pycharm/

除了通过Pycharm安装模块外（有时，点击 “插件”->" +" 不能正常显示可安装的模块），也可以通过anacoda安装模块
https://www.anaconda.com/

默认英文版，可安装中文版本插件

注意：Python、IDE、VNTrader DLL模块必须一致，必须同时是32位或同时是64位。

支持Windows平台

#### 安装教程

1.  安装Python3.0
2.  安装Pycharm
3.  在Pycharm安装PyQT插件
4.  在Pycharm 中菜单 “运行”-> "运行"

#### 使用说明

VNTrader是VNPY官方 http://www.vnpy.cn 推出的一款国内期货量化交易开源软件，
主要支持CTP接口，支持国内149家期货公司程序化交易，实现程序化交易是免费的。
支持股指期货、商品期货、股指期权、商品期权，
支持中国8大合规交易所中的5所，包括上海期货交易所，大连期货交易所、
郑州期货交易所、中金所、能源所。



#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


