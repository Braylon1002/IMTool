#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='imtool',
    # 正式版本.测试版本
    version=0.1,
    description=(
        'this package aims to contain Influence Maximization tools as much as possible.'
    ),
    # long_description=open('README.rst').read(),
    author='Braylon',
    author_email='S.Braylon1002@gmail.com',
    maintainer='Braylon',
    maintainer_email='S.Braylon1002@gmail.com',
    packages=find_packages(),
    platforms=["all"],
    url='https://gitee.com/S_Braylon/dashboard/projects',
    classifiers=[
        # 'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        # 'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        # 'Programming Language :: Python',
        # 'Programming Language :: Python :: Implementation',
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
        # 'Programming Language :: Python :: 3.6',
        # 'Topic :: Software Development :: Libraries'
    ],
)
