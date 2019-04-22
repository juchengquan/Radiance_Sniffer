# -*- coding: utf-8 -*-
"""
Last updated on: 20190311
@author: cqju
"""
import os, urllib.request   
import time  
import datetime as dt
import pathlib

class RadianceSniffer:
    urlPath = []
    localPath = []

    def __init__(self):
        self.seturlPath(self.urlPath)
        self.setlocalPath(self.localPath)
        self.int = 3;
    
    #generate fileName 
    def generateFileName(self):  
        timenow = dt.datetime.now()
        return str(timenow.strftime("%Y%m%d_%H%M"))  
    
    #generate IMG file    
    def createFileWithFileName(self, fileName):  
        totalPath=self.localPath+'\\'+fileName  
        if not os.path.exists(totalPath):  
            file=open(totalPath,'a+')  
            file.close()  
            return totalPath  
    
    def setLoopTime(self, loopTime):
        self.loopTime = loopTime
    
    def seturlPath(self,urlPath):
        if len(urlPath) == 0 :
            self.urlPath = 'http://www.solar-repository.sg/ftp_up/irradiance/NSR_IrrMap.png/'
        else :
            self.urlPath = urlPath
            
    def setlocalPath(self,localPath):
        if len(localPath) == 0 :
            self.localPath = '.\pythonPath'  
        else :
            self.localPath = localPath    
        pathlib.Path(self.localPath).mkdir(parents=True, exist_ok=True) 

    # 打印时间函数
    def loopProcess(self):
        #print(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        fileName=self.generateFileName()+'.png'
        urllib.request.urlretrieve(self.urlPath, self.createFileWithFileName(fileName))  
        #print('image saved')
        return fileName

#end