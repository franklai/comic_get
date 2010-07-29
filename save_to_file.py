import time

import CocoComic
import DM99Manga
import MH99770

def save_file(output, url, engine):
    filename = '%s.%s.txt' % (output, time.ctime())
    out = open(filename.replace(':', '_'), 'wb')

    list = engine.get(url)

    out.write('\n'.join(list))
    out.close()

    print('save image list to %s' % (filename, ))

def try_mh99770():
    output = 'image_list.mh99770.txt'
    url = 'http://mh.99770.cc/manhua/352/55499/?s=4'

    engine = MH99770.MH99770()
    save_file(output, url, engine)

def try_cococomic():
    output = 'image_list.cococomic.txt'
    url = 'http://www.cococomic.com/manhua/3063/51485/?s=1'

    engine = CocoComic.CocoComic()
    save_file(output, url, engine)

def try_dm99manga():
    output = 'image_list.dm99manga.txt'
    url = 'http://dm.99manga.com/manhua/6498/56302/?s=11'

#     url = DM99Manga.test_url
    engine = DM99Manga.DM99Manga()
    save_file(output, url, engine)

if __name__ == '__main__':
#     try_mh99770()
#     try_cococomic()
    try_dm99manga()

