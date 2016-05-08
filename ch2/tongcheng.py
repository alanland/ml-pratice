# coding: utf-8

import urllib
from cStringIO import StringIO
from pyquery import PyQuery as pq

import bson.binary

import spider

baseUrl = 'http://jiaoyou.58.com'
mainUrl = '/sh/mm/18-28'


def parseSearch(url):
    html = spider.getPage(baseUrl + url)
    d = pq(html)
    persons = d('.jy_mian .fj_box .fj_list')
    print 'find %s person' % persons.length
    for person in persons:
        person = pq(person)
        url = person('dt a').attr('href')
        avator = person('dt a img').attr('src')
        # print "%s %s" % (url, avator)

        doc = spider.getPerson(url)
        if doc == None:
            try:
                doc = parsePerson(url)
                spider.insertPerson(doc)
            except:
                # todo eg: http://jiaoyou.58.com/user/15455865499142/
                pass
    nextPage = d('#nextPage').attr('href')
    if spider.saveSearchUrl(nextPage):
        parseSearch(nextPage)
    else:
        parseSearch(nextPage)


def parsePerson(url):
    doc = {'href': url, 'baseUrl': baseUrl, 'url': baseUrl + url}
    print '%s' % baseUrl + url

    html = spider.getPage(baseUrl + url)
    d = pq(html)

    person = d('.jy_main .column_zy')
    main = person('.grzl')

    avatorUrl = main('.zy_img span img').attr('src')
    doc['avatorUrl'] = avatorUrl
    doc['charm'] = main('#followcountid').text().split(' ')[0]
    image = urllib.urlopen(avatorUrl).read()
    doc['avator'] = bson.binary.Binary(StringIO(image).getvalue())

    doc['username'] = main('#nickid').text()
    doc['intr'] = main('.zy_zl .m_yh').text()
    for e in main('.zy_zl .m_zl span'):
        key = e.text.split(u'：')[0]
        value = e.text.split(u'：')[1]
        doc[key] = value

    doc['picCount'] = main('.m_xc .xc_dl a')[0].text

    details = person('.zy_xx ul li')
    for detail in details:
        kv = pq(detail).text().replace(u'　', '').replace(u' ', '').split(u'：')
        key = kv[0]
        value = kv[1]
        doc[key] = value
    print '%s %s' % (url, doc['username'])
    return doc

if __name__=='__main__':

    parseSearch(mainUrl)
    # doc = spider.getPerson('/user/20745862187271/')
    # file = open('/home/alan/workspace/pycharm/ml-practice/ch2/aa.jpg', "wb")
    # file.write(doc['avator'])
    # file.flush()
    # file.close()
