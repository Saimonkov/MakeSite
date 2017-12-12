# /usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys
import subprocess
from django.http import HttpResponse


def add_app(sParameter, name_app):
    f = open('text.txt', 'r+')

    lines = f.readlines()
    numOfLine = 0

    for temp in lines:
        numOfLine += 1
        if sParameter in temp:
            numOfLine += 1
            print(numOfLine)
            f.writelines('%s' % name_app)

    f.close()
    pass
def app_download(request):
    # code = sys.getdefaultencoding()
    # os.system('git clone https://github.com/Saimonkov/django_cms_template.git MakeSite_folder')
    # os.chdir(os.path.join(os.getcwd(), "MakeSite_folder"))
    # os.system('git clone https://github.com/Saimonkov/MY_APP.git')
    # print(os.getcwd())
    # os.system('cd charge')

    # print(os.getcwd())
    # print("Привет")

    # project_folder = 'MakeSite_folder'
    # main_cms = subprocess.call('git clone https://github.com/Saimonkov/django_cms_template.git %s' % project_folder)
    #
    # if main_cms == 0:
    #     print("Success!")
    #     os.chdir(os.path.join(os.getcwd(), "%s" % project_folder))
    #     subprocess.call('git clone https://github.com/Saimonkov/MY_APP.git')
    #
    # else:
    #     print("Error!")

    add_app('INSTALLED_APPS', 'name_app')

    return HttpResponse('Выполняется сборка...%s')
