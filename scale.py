#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python program for scaling webservices with HAproxy
from haproxy import haproxy
from nova import openstack

backends = []
min_backends = 2

# figure out how to get the difference and keep count

def scale_up():
    # nova create server
    # get information
    # haproxy add server
    pass

def scale_down():
    # haproxy set offline
    # wait untill no more connections
    # nova remove server
    pass

def what_do():
    pass

def main():
    # while testing connections
        # check difference
        # scale up / scale down

    stack = openstack()
    ha = haproxy.HAproxy()

    ha.compile(stack.backends())

if __name__ == '__main__':
    main()