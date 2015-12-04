#!/usr/bin/env python
# coding=utf-8
"""
Filename:       main.py
Last modified:  2015-12-04 17:58

Description:

"""

import setting
import pymssql
conn = pymssql.connect(host=setting.DB_HOST, port=setting.DB_PORT,
                       database=setting.DB_DATABASE, user=setting.DB_USER, password=setting.DB_PASSWORD)

cur = conn.cursor()
sql = """
SELECT id , user_name, referrer_name, 
member_team,
len(member_team)-len(replace(member_team, ',', '')) as member_count 
FROM member where member_team like ',cn000042%'
 order by member_count desc
"""
cur.execute(sql)


def create_node(user_name):
    return {'name': user_name, 'children': []}


def append_child(node, member):
    node['children'].append(member)

data = {}  # 层 [结点]

for row in cur.fetchall():
    id, user_name, referrer_name, member_team, member_count = row
    member_list = data.get(member_count, [])
    member_list.append({'user_name': user_name, 'parent': referrer_name})
    data[member_count] = member_list
