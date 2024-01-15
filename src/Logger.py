#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: xRuffKez
'''

import logging, os, time

#vars
#BG- Променливи
logtime = time.strftime("%d-%m-%y-%H.%M.%S")

if not os.path.exists('logs'):
    os.makedirs('logs')

def logger():
    logging.basicConfig(handlers=[logging.FileHandler(f'logs/wurzelbot {logtime}.log', 'a', 'utf-8')], level=logging.DEBUG, format='%(asctime)s - %(message)s')
