#!/usr/bin/python3

# convert symbol in sqlite db to python persistence format

import os
import sys
import sqlite3
import binascii
import numpy as np
import pandas as pd

# gftIO locates in the upper level folder
scriptFolder = os.path.dirname(__file__)
sys.path.insert(0, os.path.normpath(os.path.join(scriptFolder, "..")))
from lib.gftTools import gftIO

def sqlLite2PythonDataFrame(sqlLiteFileName, pyFileName) :
    conn = sqlite3.connect(sqlLiteFileName)
    c = conn.cursor()


def str2Gid1(str):
    v1 = int.from_bytes(binascii.a2b_hex(str[0][:16]), byteorder='little', signed=False)
    v2 = int.from_bytes(binascii.a2b_hex(str[0][16:]), byteorder='little', signed=False)
    return v1, v2

def str2Gid2(str):
    v1 = int.from_bytes(binascii.a2b_hex(str[0][0:16]), byteorder='big', signed=False)
    v2 = int.from_bytes(binascii.a2b_hex(str[0][16:32]), byteorder='big', signed=False)
    return ((v1,v2),str[1])

def gidInt2Str(gid):
    str1 = binascii.hexlify(gid[0].to_bytes(8,byteorder='big',signed=False)).upper().decode('UTF-8')
    str2 = binascii.hexlify(gid[1].to_bytes(8,byteorder='big',signed=False)).upper().decode('UTF-8')
    return str1 + str2


defaultFileName = "lib/gftTools/convertSymbols/symbols.db"

def sqlLite2Py(sqlLiteFileName=defaultFileName):
    conn = sqlite3.connect(sqlLiteFileName)
    c = conn.cursor()
    datas =  c.execute("SELECT gid,name||symbol FROM Data order by gid").fetchall()
    dataArray = np.array(datas)
    gidO2 = np.apply_along_axis(str2Gid2, 1, dataArray)
    # dataArray = np.concatenate((dataArray,gidO2))
    keys = gidO2[:,0].astype([('v1', '<u8'), ('v2', '<u8')])
    keys = np.chararray(shape=(keys.size), itemsize=16, buffer=keys.data)
    vals = gidO2[:,1].astype(np.str)
    pd1 = pd.DataFrame(data=vals, index=keys, columns=["val"])
    return pd1



def sqlLite2PyFormat(sqlLiteFileName, pyFilename):
    gid2Symbols = dict()

    conn = sqlite3.connect(sqlLiteFileName)
    c = conn.cursor()

    for row in c.execute("SELECT name, symbol, gid FROM Data"):
        gid = row[2].upper()
        gid2Symbols[gid] = row[0] + '-' + row[1] + '-' + gid
    conn.close()
    gftIO.zdump(gid2Symbols, pyFilename)
#
# sqlLite2Py("symbols.db")#
# symbolSqliteDb = os.path.join(scriptFolder, 'symbols.db')
# symbolPklFile = os.path.join(scriptFolder, '..', 'symbols.pkl')
#
# sqlLite2PyFormat(symbolSqliteDb, symbolPklFile)
#
# # Test the converted file
# testOArrFile = os.path.join(scriptFolder, 'testSave_0.pkl')
#
# loadedVal = gftIO.zload(testOArrFile)
# x0 = loadedVal['x0']
# oArr = x0[0]
#
# uuid2Readable = gftIO.Uuid2Readable()
# print(uuid2Readable.oArr2Readable(oArr))
