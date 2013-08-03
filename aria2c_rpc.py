#!/usr/bin/env python  
#-*-coding:utf-8-*-
  
import sys,os  
import xmlrpclib
from rpc_cfg import *

s = xmlrpclib.ServerProxy(RPC_SRV,allow_none=True)

def get_name(uri):
    if uri[-1] == '/' : uri = uri[:-1]
    return uri.split('/')[-1]

def down(uri,_out=None,_dir=None,cookie='Cookie:by=khalidhsu'):
    if not _out:_out = get_name(uri)
    opts = dict(dir=_dir,out=_out,
                header=['Accept-Language: en-US,en','Accept-Charset: utf-8',cookie])
    print 'adding %s...'%uri
    print s.aria2.addUri([uri], opts)
    
    




