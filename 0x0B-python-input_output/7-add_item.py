#!/usr/bin/python3
"""This module adds all arguments to a Python list,
and then save them to a file"""
import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    item_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    item_list = list()

item_list.extend(sys.argv[1:])
save_to_json_file(item_list, 'add_item.json')
