# -*- coding: utf-8 -*-

import wda
import logging
import os
import random
from time import sleep
import time
import json
import sys
import datetime

# 日志输出
logging.basicConfig(format='[%(asctime)s][%(name)s:%(levelname)s(%(lineno)d)][%(module)s:%(funcName)s]:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S',
                    level=logging.INFO)
logging.getLogger("requests").setLevel(logging.WARNING)

# 读取json配置
with open("{path}/devices/iphone8Plus.json".format(path=sys.path[0],), 'r') as f:
    config = json.load(f)

time_repeat = config["time"]
btn_replay  = config["button_replay"]
btn_start = config["button_start"]
screen = config["screen"]


c = wda.Client()
s = c.session()

def event_replay():
    logging.info("点击-重新开始")
    tap_screen(btn_replay)
    sleep(time_repeat)

def event_start():
    logging.info("点击-开始")
    tap_screen(btn_start)
    sleep(time_repeat)

def tap_screen(point):
    base_x, base_y = 1920, 1080
    real_x = int(point["x"] / base_x * screen["x"])
    real_y = int(point["y"] / base_y * screen["y"])

    s.tap(real_x, real_y)

def main():
    starttime = datetime.datetime.now()

    logging.info("=== 王者荣耀刷金币 ===")
    logging.info("1. 进入游戏<王者荣耀>")
    logging.info("2. 进入剧情模式-魔女之泉<困难>")
    logging.info("3. 确保打开自动模式")
    logging.info("读取device.json...")
    while True:
        event_start()
        event_replay()
        time.sleep(random.uniform(time_repeat,time_repeat+1))

        runTime = datetime.datetime.now() - starttime
        logging.info("运行时间: %s",runTime.seconds)
        if (runTime.seconds > 60*10):
            sleep(60*2)
            logging.info("运行10分钟, 休息2分钟")
            starttime = datetime.datetime.now()

if __name__ == '__main__':
    main()