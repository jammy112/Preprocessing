# coding=utf-8
import urllib2
import re
# 6285399016554496258 6282837243963048194
content = urllib2.urlopen('http://toutiao.com/group/6285399016554496258/comments/?count=901&format=json').read()
comment = re.findall('"text": "(.*?)",', content)
f1 = open('dataSet/c2.txt', 'w')
for j in comment:
    f1.write(j.decode('unicode-escape').encode('utf-8') + '\n')
