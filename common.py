# -*- coding: utf8 -*-
import re
import urllib2

class URL:
    def __init__(self, url, data=None, headers=None):
        method = 'get'

        if headers is None:
            headers = {
                'User-Agent': 'Powered by Python',
            }

        if data:
            method = 'post'
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
            }

        req = urllib2.Request(url, data, headers)
        self.handle = urllib2.urlopen(req)

    def get_content(self):
        return self.handle.read()

    def get_info(self):
        return self.handle.info()

def get_url_content(url, data=None, headers=None):
    obj = URL(url, data, headers)

    return obj.get_content()

def half2full(input):
    import re

    ascii = 'a-zA-Z0-9,\' \!\?'
    pattern = '(?<=[^%s]) | (?=[^%s])' % (ascii, ascii)

    return re.sub(pattern, u'　', input)

def unicode2string(input):
    import re

    def point2string(match_obj):
        if match_obj and match_obj.group(1):
            return unichr(int(match_obj.group(1)))

    input = input.replace('&hellip;', u'…')

    pattern = r'&#([0-9]+);'
    return re.sub(pattern, point2string, input)

def get_first_group_by_pattern(input, pattern):
    output = ''
    regex = re.compile(pattern).search(input)
    if regex:
        output = regex.group(1)
    return output

if __name__ == '__main__':
    text = """
&#26085;&#12418;<br />
<br />
"""
    print(unicode2string(text))
