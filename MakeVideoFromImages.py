#!/usr/bin/env python
# coding: utf-8
import cv2
import glob
import os

class MakeVideoFromImages:
    #コンストラクタ(this, 画像フォルダパス)
    def __init__(self, folderPath):
        self.__path = folderPath    
        fileExtensions = [ "/*.jpg", "/*.jpeg", "/*.png", "/*.bmp"]
        self.__files = []
        for extension in fileExtensions:
            self.__files.extend(glob.glob(self.__path + extension))
        self.__files.sort()
        self.__fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
        self.__output= "output"
        self.__width = 1200
        self.__height= 800
        self.__fps = 30
        
        
    #出力ビデオのサイズを設定
    def setVideoSize(self, width, height):
        self.__width = width
        self.__height= height
        
        
    #出力ファイル名を設定
    def setOutputName(self, filename):
        self.__output = filename
        
        
    #出力ファイルのfpsを設定
    def setFps(self, fps):
        self.__fps = fps
        
        
    #ビデオを作成
    def makeVideo(self):
        video = cv2.VideoWriter(self.__output+".mp4", self.__fourcc, self.__fps , (self.__width, self.__height))
        for file in self.__files:
            img = cv2.imread(file)
            if not img is None:
                cv2.putText(img, os.path.basename(file),(10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))
                img = cv2.resize(img, dsize=(self.__width, self.__height))
                video.write(img)
        video.release()
        print("success")