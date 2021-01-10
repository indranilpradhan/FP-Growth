# -*- coding: utf-8 -*-

import csv
import json
from itertools import combinations
import threading
import math
from multiprocessing.pool import ThreadPool as Pool
import datetime
from collections import OrderedDict, defaultdict
import matplotlib.pyplot as plt

class TrieNode(object):
  def __init__(self,maxnumber):
    self.children = [None]*(maxnumber+1)
    self.parent_pointer=None
    self.parent ='-1'
    self.root ='-1'
    self.isEndOfWord = False
    self.count = [0]*(maxnumber+1)

def createTrie(rootnode,items,tree,maxnumber):
    node = rootnode
    root_element = '-1' 
    for item in items:
      item = int(item)
      if root_element == '-1':
        root_element = str(item)
      node.count[item] += 1
      if not node.children[item]:
        tree[item].append(node)
        node.children[item] = TrieNode(maxnumber)
      parent_node = node
      node = node.children[item]
      node.parent_pointer = parent_node
      node.parent = item
      node.root = root_element
    node.isEndOfWord = True

def fp_growth(itemset, minsup):
  singleton_item_count = {}
  for lst in itemset:
    for i in lst:
      if i in singleton_item_count:
        singleton_item_count[i] += 1
      else:
        singleton_item_count[i] = 1
  freq_singleton_item = {}
  for k,v in singleton_item_count.items():
    if v >= minsup:
      freq_singleton_item[k] = v
  maxnumber = 0
  test_list = [int(i) for i in list(freq_singleton_item.keys())] 
  maxnumber = max(maxnumber, max(test_list))
  ordered_item_set = []
  ordered_item_set_dict = []
  for lst in itemset:
    temp = {}
    for i in lst:
      if i in freq_singleton_item:
        temp[i] = freq_singleton_item[i]
    temp = OrderedDict(sorted(temp.items(), key=lambda kv: kv[1], reverse=True))
    ordered_item_set.append(list(temp.keys()))
    ordered_item_set_dict.append(dict(temp))
    
  rootnode = TrieNode(maxnumber)
  tree = defaultdict(list) 
  for lst in ordered_item_set:
    createTrie(rootnode,lst,tree,maxnumber)

  conditional_pattern_base={}
  for i in tree.keys():
      conditional_pattern=defaultdict(list)
      roots = []
      for node in tree[i]:
          cond_pattern=[]
          pattern = {}
          temp=node
          value=node.count[int(i)]
          parent=node.parent
          root_value=node.root
          while(temp.parent_pointer):
              cond_pattern.append(parent)
              temp=temp.parent_pointer
              parent=temp.parent
          if len(cond_pattern) != 0:
            pattern[tuple(cond_pattern)] = value
            if root_value in roots:
              conditional_pattern[int(root_value)].append(pattern)
            else:
              roots.append(root_value)
              conditional_pattern[int(root_value)].append(pattern)          
            conditional_pattern_base[i]=conditional_pattern

  frequent_pattern = defaultdict(list)
  for key,value in conditional_pattern_base.items():
    for key2,value2 in value.items():
      freq = {}
      for item in value2:
        for k,v in item.items():
          for i in list(k):
            if i in freq:
              freq[i] = freq[i] + v
            else:
              freq[i] = v
      freq_p = {}
      for k,v in freq.items():
        freq_p[k] = v
      frequent_pattern[key].append(freq_p)

  before_final_pattern = {}
  for key, value in frequent_pattern.items():
    for item in value:
      keys = list(item.keys())
      for i in range(1,len(keys)+1):
        comb = list(combinations(keys,i))
        for c in comb:
          lst = list(c)
          mincount= 99999999
          for j in lst:
            mincount = min(mincount,item[j])
          lst.append(key)
          if tuple(sorted(lst)) not in before_final_pattern:
            before_final_pattern[tuple(sorted(lst))] = mincount
          else:
            before_final_pattern[tuple(sorted(lst))] += mincount

  final_pattern = []
  for k, v in before_final_pattern.items():
    if v >= minsup:
      final_pattern.append(list(k))
  return final_pattern

"""##Sign Dataset

**0.9**
"""

itemset = []
minsup = 657
with open('/content/data/sign.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()       
        itemset.append(temp)
st = datetime.datetime.now()
final_pattern=fp_growth(itemset,minsup)
end = datetime.datetime.now()
diff = end - st
print(diff.total_seconds())
final_pattern

"""**0.8**"""

itemset = []
minsup = 584
with open('/content/data/sign.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()       
        itemset.append(temp)
st = datetime.datetime.now()
final_pattern=fp_growth(itemset,minsup)
end = datetime.datetime.now()
diff = end - st
print(diff.total_seconds())
final_pattern

"""**0.7**"""

itemset = []
minsup = 511
with open('/content/data/sign.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()       
        itemset.append(temp)
st = datetime.datetime.now()
final_pattern=fp_growth(itemset,minsup)
end = datetime.datetime.now()
diff = end - st
print(diff.total_seconds())
final_pattern

"""##Leviathan

**0.7**
"""

itemset = []
minsup = 4084
with open('/content/data/Leviathan.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()       
        itemset.append(temp)
st = datetime.datetime.now()
final_pattern=fp_growth(itemset,minsup)
end = datetime.datetime.now()
diff = end - st
print(diff.total_seconds())
final_pattern

"""**0.6**"""

itemset = []
minsup = 3501
with open('/content/data/Leviathan.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()       
        itemset.append(temp)
st = datetime.datetime.now()
final_pattern=fp_growth(itemset,minsup)
end = datetime.datetime.now()
diff = end - st
print(diff.total_seconds())
final_pattern

"""**0.5**"""

itemset = []
minsup = 2917
with open('/content/data/Leviathan.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()       
        itemset.append(temp)
st = datetime.datetime.now()
final_pattern=fp_growth(itemset,minsup)
end = datetime.datetime.now()
diff = end - st
print(diff.total_seconds())
final_pattern

"""##Library

##Sign

**0.9**
"""

import pyfpgrowth
itemset = []
minsup = 657
with open('/content/data/sign.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()       
        itemset.append(temp)
st = datetime.datetime.now()
patterns = pyfpgrowth.find_frequent_patterns(itemset, minsup)
for tup,val in patterns.items():
  if len(list(tup)) > 1:
    print(tup)
end = datetime.datetime.now()
diff = end - st
print(diff.total_seconds()/60.0)

import pyfpgrowth
itemset = []
minsup = 584
with open('/content/data/sign.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()       
        itemset.append(temp)
st = datetime.datetime.now()
patterns = pyfpgrowth.find_frequent_patterns(itemset, minsup)
for tup,val in patterns.items():
  if len(list(tup)) > 1:
    print(tup)
end = datetime.datetime.now()
diff = end - st
print(diff.total_seconds()/60.0)

import pyfpgrowth
itemset = []
minsup = 511
with open('/content/data/sign.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()       
        itemset.append(temp)
st = datetime.datetime.now()
patterns = pyfpgrowth.find_frequent_patterns(itemset, minsup)
for tup,val in patterns.items():
  if len(list(tup)) > 1:
    print(tup)
end = datetime.datetime.now()
diff = end - st
print(diff.total_seconds()/60.0)

"""##Leviathan"""

import pyfpgrowth
itemset = []
minsup = 5000
with open('/content/data/Leviathan.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()       
        itemset.append(temp)
st = datetime.datetime.now()
patterns = pyfpgrowth.find_frequent_patterns(itemset, minsup)
for tup,val in patterns.items():
  if len(list(tup)) > 1:
    print(tup)
end = datetime.datetime.now()
diff = end - st
print(diff.total_seconds()/60.0)

import pyfpgrowth
itemset = []
minsup = 3501
with open('/content/data/Leviathan.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()       
        itemset.append(temp)
st = datetime.datetime.now()
patterns = pyfpgrowth.find_frequent_patterns(itemset, minsup)
for tup,val in patterns.items():
  if len(list(tup)) > 1:
    print(tup)
end = datetime.datetime.now()
diff = end - st
print(diff.total_seconds()/60.0)

import pyfpgrowth
itemset = []
minsup = 2917
with open('/content/data/Leviathan.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [i.strip() for i in row[0].split('-1')]
        if temp[-1] != '-2':
          print('wrong')
        temp.pop()       
        itemset.append(temp)
st = datetime.datetime.now()
patterns = pyfpgrowth.find_frequent_patterns(itemset, minsup)
for tup,val in patterns.items():
  if len(list(tup)) > 1:
    print(tup)
end = datetime.datetime.now()
diff = end - st
print(diff.total_seconds()/60.0)

