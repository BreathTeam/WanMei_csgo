import wx
import win32gui, win32ui
import win32api, sys
from win32api import GetSystemMetrics
from ctypes import *
from PyQt5.Qt import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect, QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets
import os, time, threading
dl = windll.LoadLibrary(r"kernel32.dll")
pid = dl.GetCurrentProcessId()
dl = CDLL(r"ThaseDriverBigD1ckIntoThePipeSharedDynamicLinkLibrary.vmp.dll")
dl.T_GetProcessModuleBase.argtypes = [c_int, POINTER(c_char)]
dl.T_ReadInt.argtypes = [c_int, c_void_p]
dl.T_WriteFloat.argtypes = [c_int, c_void_p, c_float]
dl.T_ReadFloat.restype = c_float
card = ""
card = (c_char * 100)(*bytes(card, 'utf-8'))
dl.T_ConnectPipe()
dl.T_Login(card, pid)
p = "csgo.exe"
p = (c_char * 100)(*bytes(p, 'utf-8'))
PID_ = dl.T_GetProcessId(p)
screen_x = 1280#abs(left - right)
screen_y = 960#abs(bottom - top)
m = "\client.dll"
m = (c_char * 200)(*bytes(m, 'utf-8'))
client = (dl.T_GetProcessModuleBase(PID_, m))  & 0xffffffff
print(client)
ViewMatrix_point = 0x4DEECB4
Entitylist_head = 0x4DFDE84
local = 0xDE8964
ViewMatrix_point = 0x4DEECB4
Entitylist_head = 0x4DFDE84
local = 0xDE8964
# init

app=wx.App()
dc=wx.ScreenDC()

# set line and fill style
dc.SetBrush(wx.TRANSPARENT_BRUSH) 
dc.SetPen(wx.Pen((255, 255, 255), width=3, style=wx.PENSTYLE_SOLID))
def rect(x, y, w, h):
    dc.DrawRectangle(x, y, w, h)
# draw (x, y, width, height)
while True:
    Me = dl.T_ReadInt(PID_, client + local) & 0xffffffff
    My_team =  dl.T_ReadInt(PID_, Me + 0xF4) & 0xffffffff
    for i in range(0, 48):
        try:
            try:
                Enemy_adr = dl.T_ReadInt(PID_, client + Entitylist_head + i * 8)& 0xffffffff
                Enemy_heath =  dl.T_ReadInt(PID_, Enemy_adr + 256)& 0xffffffff
                Enemy_team =  dl.T_ReadInt(PID_, Enemy_adr + 0xF4)& 0xffffffff
                Enemy_state =  dl.T_ReadInt(PID_, Enemy_adr + 0xED)& 0xffffffff
            
            except:
                continue
            if Enemy_heath > 0 and Enemy_heath <= 100 and My_team != Enemy_team and Enemy_state == 0:
                GGD = dl.T_ReadInt(PID_, Enemy_adr + 0x26A8) + 8 * 48 & 0xffffffff #0x26A8
                e_x = dl.T_ReadFloat(PID_, GGD + 12)
                e_y = dl.T_ReadFloat(PID_, GGD + 28)
                e_z = dl.T_ReadFloat(PID_, GGD + 44)
                matrix_0 =dl.T_ReadFloat(PID_, client + ViewMatrix_point)
                matrix_1 = dl.T_ReadFloat(PID_, client + ViewMatrix_point + 4)
                matrix_2 = dl.T_ReadFloat(PID_, client + ViewMatrix_point + 8)
                matrix_3 = dl.T_ReadFloat(PID_, client + ViewMatrix_point + 12)
                matrix_4 = dl.T_ReadFloat(PID_, client + ViewMatrix_point + 16)
                matrix_5 = dl.T_ReadFloat(PID_, client + ViewMatrix_point + 20)
                matrix_6 = dl.T_ReadFloat(PID_, client + ViewMatrix_point + 24)
                matrix_7 = dl.T_ReadFloat(PID_, client + ViewMatrix_point + 28)
                matrix_8 = dl.T_ReadFloat(PID_, client + ViewMatrix_point + 32)
                matrix_9 = dl.T_ReadFloat(PID_, client + ViewMatrix_point + 36)
                matrix_10 = dl.T_ReadFloat(PID_, client + ViewMatrix_point + 40)
                matrix_11 = dl.T_ReadFloat(PID_, client + ViewMatrix_point + 44)
                matrix_12 = dl.T_ReadFloat(PID_, client + ViewMatrix_point + 48)
                matrix_13 = dl.T_ReadFloat(PID_, client + ViewMatrix_point + 52)
                matrix_14 = dl.T_ReadFloat(PID_, client + ViewMatrix_point + 56)
                matrix_15 = dl.T_ReadFloat(PID_, client + ViewMatrix_point + 60)
                ViewMatrix = [[matrix_0, matrix_1, matrix_2, matrix_3],
                 [
                  matrix_4, matrix_5, matrix_6, matrix_7],
                 [
                  matrix_8, matrix_9, matrix_10, matrix_11],
                 [
                  matrix_12, matrix_13, matrix_14, matrix_15]]
                screen_width = screen_x / 2
                screen_high = screen_y / 2  
                ViewW = ViewMatrix[2][0] * e_x + ViewMatrix[2][1] * e_y + ViewMatrix[2][2] * e_z + ViewMatrix[2][3]
                if ViewW < 0:
                    pass
                else:
                    ViewW = 1 / ViewW
                    BoxX0 = screen_width + (ViewMatrix[0][0] * e_x + ViewMatrix[0][1] * e_y + ViewMatrix[0][2] * e_z + ViewMatrix[0][3]) * ViewW * screen_width
                    BoxY0 = screen_high - (ViewMatrix[1][0] * e_x + ViewMatrix[1][1] * e_y + ViewMatrix[1][2] * e_z + ViewMatrix[1][3]) * ViewW * screen_high
                    BoxY00 = screen_high - (ViewMatrix[1][0] * e_x + ViewMatrix[1][1] * e_y + ViewMatrix[1][2] * (e_z + 75) + ViewMatrix[1][3]) * ViewW * screen_high
                    BoxY10 = screen_high - (ViewMatrix[1][0] * e_x + ViewMatrix[1][1] * e_y + ViewMatrix[1][2] * (e_z - 5) + ViewMatrix[1][3]) * ViewW * screen_high
                    x = screen_width + (ViewMatrix[0][0] * e_x + ViewMatrix[0][1] * e_y + ViewMatrix[0][2] * e_z + ViewMatrix[0][3]) * ViewW * screen_width / 3
                    y = screen_high - (ViewMatrix[1][0] * e_x + ViewMatrix[1][1] * e_y + ViewMatrix[1][2] * e_z + ViewMatrix[1][3]) * ViewW * screen_high / 2
                    #rect(BoxX0 - (BoxY10 - BoxY00) / 4, BoxY00, (BoxY10 - BoxY00) / 2, BoxY10 - BoxY00)
                    rect(BoxX0, BoxY0, 5, 5)
                    #dc.DrawCircle(BoxX0, BoxY0, 3)
        except Exception as e:
            print(e)
    