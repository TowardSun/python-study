#-*- coding:utf-8 -*-

#它的设计思想是用一种描述性的语言来给字符串定义一个规则，
#凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。

#在正则表达式中，如果直接给出字符，就是精确匹配。用\d可以匹配一个数字，\w可以匹配一个字母或数字
#.可以匹配任意字符

#要匹配变长的字符，在正则表达式中，用*表示任意个字符（包括0个），用+表示至少一个字符，
#用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符
#\s可以匹配一个空格（也包括Tab等空白符）

#如果要匹配'010-12345'这样的号码呢？由于'-'是特殊字符，在正则表达式中，要用'\'转义，
#所以，上面的正则是\d{3}\-\d{3,8}


#要做更精确地匹配，可以用[]表示范围
#[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；


#A|B可以匹配A或B，所以[P|p]ython可以匹配'Python'或者'python'。

#^表示行的开头，^\d表示必须以数字开头。

#$表示行的结束，\d$表示必须以数字结束。

#建议使用Python的r前缀，就不用考虑转义的问题

import re

#test_str = raw_input('Please input string:')
test_str = '045-853456'
if re.match(r'^\d{3}\-\d{3,8}$', test_str):
	print 'ok'
else:
	print 'failed'

'''
用正则表达式切分字符串比用固定的字符更灵活，请看正常的切分代码：

>>> 'a b   c'.split(' ')
['a', 'b', '', '', 'c']
嗯，无法识别连续的空格，用正则表达式试试：

>>> re.split(r'\s+', 'a b   c')
['a', 'b', 'c']
'''

#*****************************切分字符串**********************
print re.split(r'\s+', 'a b   c')
print re.split(r'[\s\,\;]+', 'a,b;; c  d')

#************************分组*********************
#()用于将匹配的字符串再分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
#如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来。
#注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串
print m.group(0), m.group(1), m.group(2)

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print m.groups()  #('19', '05', '30')


#**********************贪婪匹配***************************
#正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
print re.match(r'^(\d+)(0*)$', '102300').groups()
print re.match(r'^(\d+?)(0*)$', '102300').groups()


#当我们在Python中使用正则表达式时，re模块内部会干两件事情：
#1.编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
#2.用编译后的正则表达式去匹配字符串

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')		#预编译正则表达式
print re_telephone.match('010-12345').groups()

email_str = '<Tom Paris> tom@voyager.org'

if re.match(r'^<(\w+\s\w+)>\s+(.+?@\w+\.org)$', email_str):
	print 'ok', email_str
else:
	print 'failed', email_str

#百度方案
def is_email_address(self,address):
    if re.match(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$',address):
        return True
    else:
        return False
