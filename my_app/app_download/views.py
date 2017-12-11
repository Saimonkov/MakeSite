# /usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys
from django.http import HttpResponse



def app_download(request):
    # code = sys.getdefaultencoding()
    os.system('git clone https://github.com/Saimonkov/MY_APP.git test_folder')
    # print(code)
    # print("Привет")
    return HttpResponse('asdf')
