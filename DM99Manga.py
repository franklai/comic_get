import cgi
import common
import logging
import re
import urlparse

referrer_needed = True
site_url = 'http://dm.99manga.com/'
test_url = 'http://dm.99manga.com/manhua/5473/44805/?s=2'

class DM99Manga:
    def __init__(self):
        self.serverListJS = '/v2/vai.js'
        pass

    def get(self, url):
        self.url = url
        logging.debug('url: %s' % (url, ))

        self.parse_url()

        self.get_image_server()

        list = self.get_image_list()

        return list

    def parse_url(self):
        o = urlparse.urlparse(self.url)
        self.host = o.netloc
        self.query = o.query
        self.query_obj = cgi.parse_qs(o.query)

    def get_image_server(self):
        url = 'http://%s%s' % (self.host, self.serverListJS)
        content = common.get_url_content(url)

        self.image_server = self.parse_image_server(content)

        if self.image_server == '':
            raise Exception('failed to find image_server')

        logging.debug('image_server: %s' % (self.image_server, ) )

    def parse_image_server(self, js):
        pattern = 'ServerList\[([0-9]+)\]="([^"]+)";'
        list = re.findall(pattern, js)
        server_dict = {}

        for pair in list:
            server_dict[int(pair[0])] = pair[1]

        if 's' in self.query_obj:
            serverNo = int(self.query_obj['s'][0]) - 1
            if serverNo in server_dict:
                return server_dict[serverNo]
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

    obj = DM99Manga()
    list = obj.get(test_url)
    logging.debug(list)

