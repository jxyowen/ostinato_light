__author__ = 'jxy'

from setuptools import setup, find_packages

setup(
    name = 'ostinato_light',
    version = '0.1.7',
    keywords = ('wrapper', 'ostinato'),
    description = 'use ostinato in a more elegant way, python3 is incompatible',
    license = 'MIT License',

    url = 'http://www.jxyowen.cn',
    author = 'jxyowen',
    author_email = '506092147@qq.com',

    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = ['protobuf>=2.6.1', 'python-ostinato>=0.7.1'],
)