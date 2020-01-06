import time

import win32process#进程模块
from win32con import PROCESS_ALL_ACCESS #Opencress 权限
import win32api#调用系统模块
import ctypes#C语言类型
from win32gui import FindWindow#界面
import win32ui
import win32con
import win32gui


def left_cl(x,y):

    win32api.SetCursorPos([x, y])
    #根据横纵坐标定位光标
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
hld = win32gui.FindWindow(None, u"神武4 - 浩气冲霄")  # 返回窗口标题为Adobe Acrobat的句柄


if hld == 0:
         MoniterDev = win32api.EnumDisplayMonitors(None, None)
         width = MoniterDev[0][2][2]
         print(width)
         height = MoniterDev[0][2][3]
         print(height)
else:
     win32gui.SetForegroundWindow(hld)
     left, top, right, bot = win32gui.GetWindowRect(hld)
     time.sleep(0.3)
     x = left+698
     y = top+60
     left_cl(x,y)
     print(left)
     print(top)
     print(right)
     print(bot)
     time.sleep(0.3)

     width = right - left
     height = bot - top
     # 返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
     hwndDC = win32gui.GetWindowDC(hld)
     # 创建设备描述表
     mfcDC = win32ui.CreateDCFromHandle(hwndDC)
     # 创建内存设备描述表
     saveDC = mfcDC.CreateCompatibleDC()
     # 创建位图对象准备保存图片
     saveBitMap = win32ui.CreateBitmap()
     # 为bitmap开辟存储空间
     saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
     # 将截图保存到saveBitMap中
     saveDC.SelectObject(saveBitMap)
     # 保存bitmap到内存设备描述表
     saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)
     try:
      saveBitMap.SaveBitmapFile(saveDC, "1.jpg")
     except:
      pass

    #删除专用设备场景或信息场景，释放所有相关窗口资源
     win32gui.DeleteObject(saveBitMap.GetHandle())
     saveDC.DeleteDC()
     mfcDC.DeleteDC()
     win32gui.ReleaseDC(hld, hwndDC)





#给光标定位的位置进行单击操作（若想进行双击操作，可以延时几毫秒再点击一次）
# win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN,  300, 300, 0, 0)

win32api.keybd_event(13,0,0,0)
win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)

#截图函数
