#!/usr/bin/env python3
#-*- coding:UTF-8 -*-
#欢迎关注微信公众号：点滴技术
#这里有靠谱、有价值的、免费分享、成长的，专属于网络攻城狮的

'''
用于直接执行本代码
'''
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'My_Django.settings')
django.setup()

from django.shortcuts import render
from datetime import datetime
from data import courses_db
from ddjs_db.models import Courses
import json


#以下代码对应summary.html
def summary(request):
    #%w 用于显示周几
    summary = '课程摘要'
    mytime = int(datetime.now().strftime('%w'))
    # courses_list = ['网络技术', '网络编程','自动化运维','数据分析','网络爬虫','其他']
    # teacher_list = [{'courses':'安全','teacher':'小明'},
    #                 {'courses': '数据中心', 'teacher':'小东'},
    #                 {'courses': '路由交换', 'teacher':'小华'},
    #                 {'courses': '无线', 'teacher':'小李'},
    #                 {'courses': '语音', 'teacher':'小西'},
    #                 ]
    # return render(request, 'summary.html', {'summary':'技术文章',
    #                                         'courses_list':courses_list,
    #                                         'teacher_list':teacher_list,
    #                                         'mytime':mytime})
    courses = Courses.objects.values('courses_FangXiang')
    zuoze_lists = Courses.objects.values_list('courses_FangXiang', 'courses_ZuoZe')
    courses_list = []
    zuoze_list = []
    for c in courses:
        courses_list.append(c['courses_FangXiang'])
    for c_t in zuoze_lists:
        zuoze_list.append({'方向':c_t[0], '作者':c_t[1]})

    return render(request, 'summary.html', locals())


#以下代码对应course.html
def net_tech(request):
    r = Courses.objects.get(courses_FangXiang='网络技术')
    net = {'方向': r.courses_FangXiang,
            '摘要': r.courses_ZhaiYao,
            '主要内容': json.loads(r.courses_ZhuYaoNeiRong),
            '作者': r.courses_ZuoZe}
    return render(request, 'course.html', {'courseinfo':net})

def python_tech(request):
    r = Courses.objects.get(courses_FangXiang='网络编程')
    py = {'方向': r.courses_FangXiang,
            '摘要': r.courses_ZhaiYao,
            '主要内容': json.loads(r.courses_ZhuYaoNeiRong),
            '作者': r.courses_ZuoZe}
    return render(request, 'course.html', {'courseinfo':py})
def devops_tech(request):
    r = Courses.objects.get(courses_FangXiang='自动化运维')
    devops = {'方向': r.courses_FangXiang,
            '摘要': r.courses_ZhaiYao,
            '主要内容': json.loads(r.courses_ZhuYaoNeiRong),
            '作者': r.courses_ZuoZe}
    return render(request, 'course.html', {'courseinfo':devops})

