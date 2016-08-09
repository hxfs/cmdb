#!/usr/bin/python
#coding=utf-8
import boto.ec2

conn = boto.ec2.connect_to_region('cn-north-1')

def get_all_instances():
    intance_ids = conn.get_only_instances()
    return intance_ids


#get_all_instances = get_all_instances()
    


