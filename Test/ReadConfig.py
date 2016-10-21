'''
Created on Oct 20, 2016

@author: zhangxing
'''

# class MyClass(object):
#     '''
#     classdocs
#     '''
# 
# 
#     def __init__(self, params):
#         '''
#         Constructor
#         '''
#         

import configparser

config=configparser.ConfigParser()


user_agent=open('user-agent.cnf')

for line in user_agent.readlines():
    print(line)

