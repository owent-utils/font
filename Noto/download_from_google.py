#!/bin/python3

import urllib.request
import os
import re

URL = "http://www.google.com/get/noto/"
DOWN_PATTERN = 'https[\\:\\/\\w\\.\\-]+\\.zip'

if not os.path.exists('hinted'):
    os.mkdir('hinted')
if not os.path.exists('unhinted'):
    os.mkdir('unhinted')


def call_wget_to_down_font(url):
    file_name = os.path.basename(url)
    if 'Noto-' == file_name[0:5]:
        return 0
    if '-hinted.zip' == file_name[-11:]:
        ret = os.system('wget --no-check-certificate -c {0} -O hinted/{1}'.format(url, file_name))
        if ret == 0:
            os.system('unzip -o hinted/{0} -d hinted'.format(file_name))

        return ret
    else:
        ret = os.system('wget --no-check-certificate -c {0} -O unhinted/{1}'.format(url, file_name))
        if ret == 0:
            os.system('unzip -o unhinted/{0} -d unhinted'.format(file_name))

        return ret

with urllib.request.urlopen(URL) as f:
    success_count = 0
    failed_count = 0
    for zip_url in re.findall(DOWN_PATTERN, f.read().decode('utf-8')):
        print('try to download and unzip {0}'.format(zip_url))
        res = call_wget_to_down_font(zip_url)
        if res == 0:
            success_count = success_count + 1
            print('unzip {0} done'.format(zip_url))
        else:
            failed_count = failed_count + 1
            print('unzip {0} failed'.format(zip_url))
    print('All jobs done. success count: {0}, failed count: {1}'.format(success_count, failed_count))
