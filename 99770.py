import cgi
import common
import logging
import re
import urlparse

class MH99770:
    def __init__(self):
        self.serverListJS = '/v2/ii.js'
        pass

    def get(self, url):
        self.url = url

        self.parse_url()

        self.get_image_server()
        logging.debug(url)

        list = self.get_image_list()

        return list

    def parse_url(self):
        o = urlparse.urlparse(self.url)
        self.host = o.netloc
        self.query = o.query
        self.query_obj = cgi.parse_qs(o.query)
        logging.debug(o)
        logging.debug(self.query_obj)

    def get_image_server(self):
        url = 'http://%s%s' % (self.host, self.serverListJS)
        content = common.get_url_content(url)

        self.image_server = self.parse_image_server(content)

        if self.image_server == '':
            raise Exception('failed to find image_server')


    def parse_image_server(self, js):
        pattern = 'ServerList\[([0-9]+)\]="([^"]+)";'
        list = re.findall(pattern, js)

        if 's' in self.query_obj:
            serverNo = self.query_obj['s'][0]
            for pair in list:
                print(pair, serverNo)
                if pair[0] == serverNo:
                    return pair[1]
        logging.debug(list)

#         logging.debug(js)
        return ''

    def get_image_list(self):
        content = common.get_url_content(self.url)

        list = self.parse_image_list(content)

        if len(list) > 0:
            list = ['%s%s' % (self.image_server, img, ) for img in list]
        return list

    def parse_image_list(self, html):
        list = []
        pattern = 'var PicListUrl = "([^"]+)";'

        matchObj = re.search(pattern, html)
        if matchObj:
            list = matchObj.group(1).split('|')

        return list
            
        

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    # Young Guns Vol.1
    url = 'http://www.cococomic.com/manhua/6066/51627/?s=11'

    # Young Guns Vol.1
    url = 'http://www.cococomic.com/manhua/6066/51627/?s=11'

    urls = [
        'http://www.cococomic.com/manhua/6066/51627/?s=11',
        'http://www.cococomic.com/manhua/6066/51628/?s=11',
    ]
    # Young Guns page
    # url = 'http://www.cococomic.com/comic/6066/'

    obj = MH99770()
    list = obj.get(url)
    logging.debug(list)

