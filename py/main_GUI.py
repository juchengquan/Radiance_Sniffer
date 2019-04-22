# -*- coding: utf-8 -*-
"""
Last updated on: 20190311
@author: cqju
"""
#GUI related
import tkinter as tk
#import other class:
from RadianceSniffer import RadianceSniffer

class MainApp(RadianceSniffer):
    
    dalayTime = 55*1000 #set less than 60s to avoid delay
    Flag_do = True
    
    def __init__(self):  
        super(MainApp, self).__init__() 
        self.mainWin = tk.Tk()
        self.mainWin.title('Nasty Snap')
        self.mainWin.geometry('400x200') 
        
        self.mainFrame = tk.Frame(self.mainWin)
        self.mainFrame.pack()
        
        self.bannerText =  tk.StringVar()
        self.bannerText.set("Press \"Start\" button to start.")
        
        self.footText = tk.StringVar()
        self.footText.set("Not yet started")
        
        self.infoText = tk.StringVar()
        self.infoText.set("")
        
        self.createWidgets()
        
    def createWidgets(self):
        self.btnStart = tk.Button(self.mainFrame, text='Start', command=self.startDownload)
        self.btnClose = tk.Button(self.mainFrame, text = "Stop", command = self.stopDownload)
        self.bannerLabel = tk.Label(self.mainFrame, textvariable = self.bannerText )
        self.footLabel = tk.Label(self.mainFrame, textvariable = self.footText )
        self.infoLabel = tk.Label(self.mainFrame, textvariable = self.infoText )
        #
        
        self.btnStart.grid(row=0, column=4,sticky='nsew')
        self.btnClose.grid(row=1, column=4,sticky='nsew')
        self.bannerLabel.grid(row=0, column=0,rowspan = 2, columnspan = 2, sticky='nsew')
        self.infoLabel.grid(row=2, column=4,columnspan=2, rowspan=1)
        self.footLabel.grid(row=2, column=0)
        
    def startDownload(self):
        self.bannerText.set('Save image to \"' + self.localPath + '\"... ')
        self.footText.set("Started")
        self.task()
        #self.mainWin.after(self.dalayTime, self.task)
        
    def stopDownload(self):
        self.Flag_do = False
        self.footText.set("Stopped")
        self.infoText.set(" ")
        self.bannerText.set("Press \"Start\" button to start.")
        
        
    def task(self): 
        if self.Flag_do == True:
            fileName = self.loopProcess()
            self.mainWin.after(self.dalayTime, self.task) # reschedule event in 2 seconds
            self.infoText.set("Image name: " + fileName)
        

Win = MainApp()
Win.mainWin.mainloop()

#end
