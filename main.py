#!/usr/bin/env python
# coding=utf-8
"""
Filename:       main.py
Last modified:  2015-12-04 21:08

Description:

"""

import json
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

all_members = []
all_nodes = {}
children_dict = {}  # node : children

layer_data = {}  # 层 [结点]

for row in cur.fetchall():
    id, user_name, referrer_name, member_team, member_count = row
    member_list = layer_data.get(member_count, [])
    all_nodes[user_name] = create_node(user_name)
    member = {'name': user_name, 'parent': referrer_name}
    all_members.append(member)
    member_list.append({'name': user_name})
    layer_data[member_count] = member_list


# 去掉重复的member


# 找出节点的所有子节点
for member in all_members:
    member_name = member['name']
    children = [member['name']
                for member in all_members if member['parent'] == member_name]
    children_dict[member_name] = children


print 'children_dict', children_dict


max_layer = len(layer_data)
print 'max_layer', max_layer

top_layer = layer_data[1]
top_node = top_layer[0]['name']
print 'top_node', top_node

for layer in range(max_layer - 1, 0, -1):
    # print 'layer', layer
    # 替换节点
    members = layer_data[layer]
    for member in members:
        name = member['name']
        new_childred = []
        children = children_dict.get(name)
        if not children:
            print 'not children'
        for child in children_dict.get(name):
            new_childred.append(all_nodes[child])
        member['children'] = new_childred
        # print 'new member', member
        all_nodes[name] = member

root_node = all_nodes[top_node]
print root_node


with open('data.json', 'w') as f:
    data = {'data': [root_node]}
    f.write(json.dumps(data))
