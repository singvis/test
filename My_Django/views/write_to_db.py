#!/usr/bin/env python3
#-*- coding:UTF-8 -*-
#欢迎关注微信公众号：点滴技术
#这里有靠谱、有价值的、免费分享、成长的，专属于网络攻城狮的

import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'My_Django.settings')
django.setup()

net_tech_dict = {'方向':'网络技术',
                 '摘要':'日常网络技术分享',
                 '主要内容':'["路由","交换","安全","无线","SDN"]',
                 '作者':'点滴技术'}

python_tech_dict = {'方向':'网络编程',
               '摘要':'日常网络编程、数据分析、网络爬虫分享',
               '主要内容':'["TCP/IP","UDP"]',
               '作者':'点滴技术'}

devops_tech_dict = {'方向':'自动化运维',
               '摘要':'日常网络自动化运维分享',
               '主要内容':'["Zabbix","ELK","Ansible"]',
               '作者':'点滴技术'}

from ddjs_db.models import Courses

c_list = [net_tech_dict, python_tech_dict, devops_tech_dict]
for x in c_list:
    r = Courses(courses_FangXiang=x.get('方向'),
                courses_ZhaiYao=x.get('摘要'),
                courses_ZhuYaoNeiRong=x.get('主要内容'),
                courses_ZuoZe=x.get('作者'),
                )
    r.save()