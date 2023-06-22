# coding=utf-8
from setuptools import setup, find_packages

setup(
    name='expire_lock',  #
    version='0.1',
    description=(
        '可以过期的python线程锁，基于python字典实现的锁可以过期,实现方式类似于redis锁过期的实现机制。使用字典代替 redis服务。'
    ),
    # long_description=open('README.md', 'r',encoding='utf8').read(),
    keywords=['lock','lock timeout','lock expire','expire'],
    long_description_content_type="text/markdown",
    long_description=open('README.md', 'r', encoding='utf8').read(),
    author='bfzs',
    author_email='ydf0509@sohu.com',
    maintainer='ydf',
    maintainer_email='ydf0509@sohu.com',
    license='BSD License',
    packages=find_packages() + ['funboost.beggar_version_implementation', 'funboost.assist'],  # 也可以写在 MANiFEST.in
    include_package_data=True,
    platforms=["all"],
    url='https://github.com/ydf0509/funboost',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'eventlet==0.33.3',
        'gevent==22.10.2',
        'pymongo==4.3.3',  # 3.5.1  -> 4.0.2
        'AMQPStorm==2.10.6',
        'rabbitpy==2.0.1',
        'decorator==4.4.0',
        # 'pysnooper==0.0.11',
        'Flask',
        'flask_bootstrap',
        'flask_wtf',
        'wtforms',
        'flask_login',
        'tomorrow3==1.1.0',
        'persist-queue>=0.4.2',
        'elasticsearch',
        'kafka-python==2.0.2',
        'requests',
        'gnsq==1.0.1',
        'psutil',
        # 'sqlalchemy==1.3.10',
        # 'sqlalchemy_utils==0.36.1',    # 用户使用数据库作为消息队列时候，自行安装，不自动安装这个包。也可以使用kombu中间件的sqlalchemy模式来操作数据库或者peewee操作。
        'peewee==3.15.1',
        'apscheduler==3.10.1',
        'pikav0',
        'pikav1',
        'redis2',
        'redis3',
        'redis',
        'nb_log>=8.5',
        'rocketmq',
        'zmq',
        'pyzmq',
        'paho-mqtt',
        'setuptools_rust',
        'fabric2==2.6.0',  # 有的机器包rust错误， 这样做 curl https://sh.rustup.rs -sSf | sh
        'nats-python',
        # 'pulsar-client==3.1.0',   # python3.6 无法安装 pulsar-client
        # 'kombu',
        'nb_filelock',
        'aiohttp==3.8.3',
        'pysnooper',
        'deprecated',
        'cryptography',
        'auto_run_on_remote',
        'frozenlist',
    ],
    extras_require={'extra_brokers': ['confluent_kafka==1.7.0',
                                      "pulsar-client==3.1.0; python_version>='3.7'",
                                      'celery',
                                      'flower',
                                      'nameko==2.14.1',
                                      'sqlalchemy==1.4.8',
                                      'sqlalchemy_utils==0.36.1',
                                      'dramatiq==1.14.2',
                                      'huey==2.4.5',
                                      'rq==1.15.0',
                                      'kombu'
                                      ]},
)

"""
官方 https://pypi.org/simple
清华 https://pypi.tuna.tsinghua.edu.cn/simple
豆瓣 https://pypi.douban.com/simple/ 
阿里云 https://mirrors.aliyun.com/pypi/simple/
腾讯云  http://mirrors.tencentyun.com/pypi/simple/

打包上传
python setup.py sdist upload -r pypi

# python setup.py bdist_wheel
python setup.py bdist_wheel ; python -m twine upload dist/funboost-15.0-py3-none-any.whl
python setup.py bdist_wheel && python -m twine upload dist/funboost-23.3-py3-none-any.whl
python setup.py sdist & twine upload dist/funboost-10.9.tar.gz

最快的下载方式，上传立即可安装。阿里云源同步官网pypi间隔要等很久。
./pip install funboost==3.5 -i https://pypi.org/simple   
最新版下载
./pip install funboost --upgrade -i https://pypi.org/simple     

pip install funboost[extra_brokers]     # 安装其他所有冷门的中间件操作包。


从git安装
pip install git+https://github.com/ydf0509/funboost.git 
pip install git+https://gitee.com/bfzshen/funboost.git

"""
