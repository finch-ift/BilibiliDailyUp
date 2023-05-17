import os
import random


def env(key):
    return os.environ.get(key)


def env_key(key):
    data = ''  # 数据
    if env(key):
        data = env(key)
    return data


def env_key_list(key):
    data = []  # 数据
    if env(key):
        data.extend(env(key).split('&'))
    return data
