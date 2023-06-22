
import time
from threading import Thread, Lock

test_raw_lock = Lock()


def test_raw_lock_fun(x):
    try:
        test_raw_lock.acquire(timeout=4)
        print(x, time.time())
        time.sleep(5)
        test_raw_lock.release()
    except Exception as e:
        if 'release unlocked lock' in str(e):
            return
        print(e)


for i in range(100):
    Thread(target=test_raw_lock_fun, args=[i]).start()


''''
4秒钟内就把100个函数的print(x)运行完成了， 原生锁.acquire(timeout=4) timeout 和 过期锁的4秒过期完全不一样。
'''