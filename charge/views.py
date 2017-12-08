from django.shortcuts import render
import urllib
# import datetime
from xml.etree import ElementTree as ET

# from djangocms_forms.forms import FormBuilder


def test(request):
    per = 'per'
    context = {
        'per': per
    }
    return render(request, 'base.html', context)


def dollar(request):
    id_dollar = "R01235"

    valuta = ET.parse(urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req"))

    for line in valuta.findall('Valute'):
        id_v = line.get('ID')
        if id_v == id_dollar:
            rub_dollar = line.find('Value').text

    # return rub_dollar
    return render(request, 'base.html', {'rub_dollar': rub_dollar})


# def base_form(request):
#     var1 = FormBuilder.save.__code__
#     index = var1.co_varnames.index('form_data')
#     value = var1.co_consts
#     perem = value
#     return render(request, 'make.html', {'perem': perem})
