import requests
from urllib import quote
import base64
import re
import time

cookies = '_fofapro_ars_session=xxxxxxxxxxxxxx;'

def main(params):
    with open('list.txt', 'w+') as f:
        for i in range(1, 101):
            for x in getData(i, params):
                f.write(x+'\n')
                f.flush()
    f.close()

def getData(page, q):
    print '[START] Page '+str(page)
    time.sleep(2.5)
    qbase64 = quote(base64.b64encode(q).encode('utf-8'))
    data = requests.get('https://fofa.so/result?page='+str(page)+"&q="+q+'&qbase64='+qbase64, headers = {'Cookie':cookies}).text
    if 'Retry later' in data:
        print '[!!+!!!]'+str(page)+'[!!!!!]'
        time.sleep(20)
        return getData(page, q)
    r = re.compile(r'"javascript:view\(\'(.*)\'\)')
    ret = r.findall(data)
    print ret
    print '[END] Page ' + str(page)
    return ret

if __name__ == '__main__':
    main('app="Solr"')
