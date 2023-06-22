'''
基于程序内存的过期锁。
'''

import copy
from threading import Thread, Event, Lock
import time
import typing
import uuid

from funboost.utils import time_util
from nb_log import get_logger

lock_key__event_is_free_map: typing.Dict[str, Event] = {}


class LockStore:
    lock_for_operate_store = Lock()

    lock_key__info_map: typing.Dict[str, typing.Dict] = {}

    _has_start_delete_expire_lock_key_thread = False

    THREAD_DELETE_DAEMON = False
    DELETE_INTERVAL = 0.01

    logger = get_logger('LockStore')

    @classmethod
    def _auto_delete_expire_lock_key_thread(cls):
        while 1:
            with cls.lock_for_operate_store:
                lock_key__info_map_copy = copy.copy(cls.lock_key__info_map)
                for lock_key, info in lock_key__info_map_copy.items():
                    if time.time() - info['set_time'] > info['ex']:
                        cls.lock_key__info_map.pop(lock_key)
                        cls.logger.warning(
                            f'''自动删除占用耗时长的锁 {lock_key} {time_util.DatetimeConverter(info['set_time'])} {info['ex']}''')
                        lock_key__event_is_free_map[lock_key].set()
            time.sleep(cls.DELETE_INTERVAL)

    @classmethod
    def set(cls, lock_key, value, ex):
        set_succ = False
        with cls.lock_for_operate_store:
            if lock_key not in cls.lock_key__info_map:
                cls.lock_key__info_map[lock_key] = {'value': value, 'ex': ex, 'set_time': time.time()}
                set_succ = True

                event_is_free = Event()
                event_is_free.set()
                lock_key__event_is_free_map[lock_key] = event_is_free

            if cls._has_start_delete_expire_lock_key_thread is False:
                cls._has_start_delete_expire_lock_key_thread = True
                Thread(target=cls._auto_delete_expire_lock_key_thread, daemon=cls.THREAD_DELETE_DAEMON).start()

        return set_succ

    @classmethod
    def delete(cls, lock_key, value):
        with cls.lock_for_operate_store:
            if lock_key in cls.lock_key__info_map:
                if cls.lock_key__info_map[lock_key]['value'] == value:
                    cls.lock_key__info_map.pop(lock_key)
                    lock_key__event_is_free_map[lock_key].set()
                    cls.logger.warning(f'expire delete {lock_key}')
                    return True
            return False


class ExpireLockConf:
    def __init__(self, expire_seconds=30, lock_key=None, ):
        self.expire_seconds = expire_seconds
        self.lock_key = lock_key or uuid.uuid4().hex


class ExpireLockContextManager:
    """
    分布式redis锁上下文管理.
    """

    def __init__(self, lock_expire_conf: ExpireLockConf):
        self.expire_seconds = lock_expire_conf.expire_seconds
        self.lock_key = lock_expire_conf.lock_key
        self.identifier = str(uuid.uuid4())
        self.has_aquire_lock = False

    def acquire(self):
        # self._line = sys._getframe().f_back.f_lineno  # noqa 调用此方法的代码的函数
        # self._file_name = sys._getframe(1).f_code.co_filename  # noqa 哪个文件调了用此方法

        while 1:
            # print(self.lock_key)
            ret = LockStore.set(self.lock_key, value=self.identifier, ex=self.expire_seconds)
            self.has_aquire_lock = ret

            if not self.has_aquire_lock:
                lock_key__event_is_free_map[self.lock_key].wait()
                continue
            else:
                lock_key__event_is_free_map[self.lock_key].clear()
                break

    def realese(self):
        return LockStore.delete(self.lock_key, self.identifier)

    def __enter__(self):
        return self.acquire()

    def __bool__(self):
        return self.has_aquire_lock

    def __exit__(self, exc_type, exc_val, exc_tb):
        result = self.realese()


if __name__ == '__main__':

    lockx1_expire = ExpireLockConf(expire_seconds=4, lock_key='test_lock_name_expire', )


    def f(x):
        with ExpireLockContextManager(lockx1_expire):
            print(x, time.time())
            time.sleep(5)


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
        Thread(target=f, args=[i]).start()
        # Thread(target=test_raw_lock_fun, args=[i]).start()
