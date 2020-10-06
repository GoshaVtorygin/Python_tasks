#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy as np #привычнее выглядит
import matplotlib.pyplot as mpp

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__':
    arguments = np.linspace(0, 200, int((200 - 0) / 0.1)) #теперь для создания массива аргументов используется функция
    mpp.plot(
        arguments,
        [math.sin(x) * math.sin(x/20.0) for x in arguments] #изменилось имя переменной
    )
    mpp.savefig("plot.svg") #теперь график сохранен в файл plot.svg в той же папке, что и файл с кодом
    
