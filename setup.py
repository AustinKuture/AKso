# coding=utf-8

"""
    @header setup.py
    @abstract   
    
    @MyBlog: http://www.kuture.com.cn
    @author  Created by Kuture on 2021/11/4
    @version 1.0.0 2021/11/4 Creation()
    
    @Copyright © 2021年 Mr.Li All rights reserved
"""
from setuptools import setup, find_packages

setup(
    name = "akso",
    version = "0.0.1",
    keywords = ("pip", "akso", ".so", "cython", "kuture", "transform so"),
    description = "transform python file to .so file",
    long_description = "将python项目批量编译成.so 文件",
    license = "MIT Licence",

    url = "",
    author = "Kuture",
    author_email = "kuture@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ['tqdm', 'distutils', 'cythonize']
)