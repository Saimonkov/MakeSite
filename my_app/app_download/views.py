# /usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys
import subprocess
from django.http import HttpResponse


def add_app(sParameter, name_app, puth_set):

    with open(puth_set, 'r') as f:
        text = f.read()

    with open(puth_set, 'w') as f:
        for line in text.splitlines():
            line += '\n'

            if sParameter in line:

                f.write(line)
                f.write('    ')
                f.write("'" + name_app + "'," +'\n')
            else:
                f.write(line)

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

    project_folder = 'MakeSite_folder'

    main_cms = subprocess.call('git clone https://github.com/Saimonkov/django_cms_template.git %s' % project_folder)

    if main_cms == 0:
        print("Success!")
        os.chdir(os.path.join(os.getcwd(), "%s" % project_folder))
        app_load = subprocess.call('git clone https://github.com/Saimonkov/MY_APP.git my_app')

        if app_load == 0:
            puth_set = os.path.join(os.getcwd(), 'django_cms_template', 'settings.py')
            #print(puth_set)
            add_app('INSTALLED_APPS = (', 'my_app.feedback_form', puth_set)
        else:
            print("Eroor!")

    else:
        print("Error!")



    return HttpResponse('Выполняется сборка...%s')
