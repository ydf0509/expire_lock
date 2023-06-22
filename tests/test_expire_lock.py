import time
from threading import Thread
from expire_lock import ExpireLockConf, ExpireLockContextManager

lockx1_expire = ExpireLockConf(expire_seconds=4, lock_key='test_lock_name_expire', )


def f(x):
    with ExpireLockContextManager(lockx1_expire):
        print(x, time.time())
        time.sleep(5)



for i in range(100):
    Thread(target=f, args=[i]).start()

''''
400秒钟内就把100个函数的print(x)运行完成了， 过期锁的设置 expire=4 和原生锁.acquire(timeout=4) 作用完全不同。

过期锁意思是一个锁获取后，最多能占用这个锁n秒。
原生锁.acquire(timeout=4) 意思是最多只等待这个锁4秒钟，强行获得锁。
'''