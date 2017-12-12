# /usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys
import subprocess
import zipfile  # подключаем модуль
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


def link_project_folder():
    link = {
        'link': 'link'
    }


    try:
        newzip = zipfile.ZipFile(r'C:\MyProject\MakeSite\test.zip', 'w')  # создаем архив
        print("Архив bdseoru.zip на диске С:/ создан.")
        newzip.close()  # закрываем архив
    except:
        print("Что-то пошло не так...")

    #return render(self, 'count.html', link)
    #return HttpResponseRedirect('http://ya.ru')
    return HttpResponse('<a href="C:\MyProject\MakeSite\"' + '"test.zip">скачать</a>')


def add_app(sParameter, name_app, puth_set):
    with open(puth_set, 'r') as f:
        text = f.read()

    with open(puth_set, 'w') as f:
        for line in text.splitlines():
            line += '\n'

            if sParameter in line:

                f.write(line)
                f.write('    ')
                f.write("'" + name_app + "'," + '\n')
                #link_project_folder()
            else:
                f.write(line)

    pass

def app_download(request):
    #link_project_folder()
    #return HttpResponse("Как-то так!")
    #return HttpResponseRedirect('http://rambler.ru')
    return link_project_folder()

def app_download2(request):
    # code = sys.getdefaultencoding()
    # os.system('git clone https://github.com/Saimonkov/django_cms_template.git MakeSite_folder')
    # os.chdir(os.path.join(os.getcwd(), "MakeSite_folder"))
    # os.system('git clone https://github.com/Saimonkov/MY_APP.git')
    # print(os.getcwd())
    # os.system('cd charge')

    # print(os.getcwd())
    # print("Привет")

    project_folder = 'MakeSite_folder'

    main_cms = subprocess.call('git clone https://github.com/Saimonkov/django_cms_template.git %s' % project_folder)

    if main_cms == 0:
        print("Success!")
        os.chdir(os.path.join(os.getcwd(), "%s" % project_folder))
        app_load = subprocess.call('git clone https://github.com/Saimonkov/MY_APP.git my_app')

        if app_load == 0:
            puth_set = os.path.join(os.getcwd(), 'django_cms_template', 'settings.py')
            # print(puth_set)
            add_app('INSTALLED_APPS = (', 'my_app.feedback_form', puth_set)
        else:
            print("Eroor!")

    else:
        print("Error!")

    return HttpResponse('Выполняется сборка...%s')
