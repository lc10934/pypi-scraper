import setuptools
 
requirements = ['configparser']       # 自定义工具中需要的依赖包
 
setuptools.setup(
    name="vnapi",       # 自定义工具包的名字
    version="1.0",             # 版本号
    author="上海量贝信息科技有限公司",           # 作者名字
    author_email="public@vnpy.cn",  # 作者邮箱
    description="Quantitative software", # 自定义工具包的简介
    license='GPLV3',           # 许可协议
    url="http://www.vnpy.cn",              # 项目开源地址
    packages=setuptools.find_packages(),  # 自动发现自定义工具包中的所有包和子包
    install_requires=requirements,  # 安装自定义工具包需要依赖的包
    python_requires='>=3.5'         # 自定义工具包对于python版本的要求
)