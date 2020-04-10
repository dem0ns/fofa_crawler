import requests
from urllib.parse import quote
import base64
import re
import time
import os

fofa_session = os.environ.get('fofa_session')
cookies = '_fofapro_ars_session={};'.format(fofa_session)

def main(params):
    with open('list.txt', 'w+') as f:
        for i in range(1, 101):
            for x in getData(i, params):
                f.write(x+'\n')
                f.flush()
    f.close()

def getData(page, search):
    print('[START] Page '+str(page))
    time.sleep(2.5)
    url = 'https://fofa.so/result?page={}&q={}&qbase64={}'.format(str(page), quote(search), quote(base64.b64encode(search.encode('utf-8'))))
    data = requests.get(url, headers = {"Cookie": cookies}).text
    if 'Retry later' in data:
        print('[!!+!!!]'+str(page)+'[!!!!!]')
        time.sleep(20)
        return getData(page, search)
    r = re.compile(r'"javascript:view\(\'(.*)\'\)')
    ret = r.findall(data)
    print(ret)
    print('[END] Page ' + str(page))
    return ret

if __name__ == '__main__':
    if fofa_session == None:
        print("Session not set")
        exit(0)
    print(cookies)
    search = input('Search command: (app="Solr")'+"\n")
    main(search)