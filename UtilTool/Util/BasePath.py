# -*- coding: utf-8 -*-
import os

BASE_DIR =os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) )
SYS_DIR = os.path.join(os.path.join(BASE_DIR,'Conf'),'sys.conf')
DB_DIR = os.path.join(os.path.join(BASE_DIR,'Conf'),'db.conf')