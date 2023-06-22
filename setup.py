# coding=utf-8
from setuptools import setup, find_packages

setup(
    name='expire_lock',  #
    version='0.3',
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
    packages=find_packages(),
    include_package_data=True,
    platforms=["all"],
    url='https://github.com/ydf0509/expire_lock',
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
        'nb_log',
    ],
    extras_require={},
)

"""

python setup.py sdist & python -m  twine upload dist/expire_lock-0.3.tar.gz




"""
