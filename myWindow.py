import time

import win32api
import win32con
import win32gui


class MyWindowLog:
    wndProc = True


class MyWindow:
    rect = [400, 100, 500, 200]
    win = []

    def wndProc(self, hWnd, message, wParam, lParam):
        print("Painting") if MyWindowLog.wndProc else None
        if message == win32con.WM_PAINT:
            hdc, paintStruct = win32gui.BeginPaint(hWnd)
            self.drawRectangle(hdc, (
                self.rect[0],
                self.rect[1],
                self.rect[2],
                self.rect[3],
            ))
            win32gui.EndPaint(hWnd, paintStruct)
            win32gui.ReleaseDC(hWnd, hdc)
            return 0
        elif message == win32con.WM_DESTROY:
            print('Closing the window.')
            win32gui.PostQuitMessage(0)
            return 0
        else:
            return win32gui.DefWindowProc(hWnd, message, wParam, lParam)

    def moveLeft(self):
        self.rect[0] = self.rect[0] - 1  # x1
        self.rect[2] = self.rect[2] - 1  # x2

    def __init__(self):
        self.createWindow()

    def createWindow(self):
        hInstance = win32api.GetModuleHandle()
        className = 'MyWindowClassName'

        message_map = {
            win32con.WM_PAINT: self.wndProc,
        }

        wndClass = win32gui.WNDCLASS()
        wndClass.style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
        wndClass.lpfnWndProc = message_map
        wndClass.hInstance = hInstance
        wndClass.hCursor = win32gui.LoadCursor(None, win32con.IDC_ARROW)
        wndClass.hbrBackground = win32gui.GetStockObject(win32con.WHITE_BRUSH)
        wndClass.lpszClassName = className

        wndClassAtom = win32gui.RegisterClass(wndClass)

        hWindow = win32gui.CreateWindowEx(
            win32con.WS_EX_COMPOSITED, wndClassAtom, None,  # WindowName
            win32con.WS_VISIBLE,
            200,  # x
            200,  # y
            500,  # width
            500,  # height
            None,  # hWndParent
            None,  # hMenu
            hInstance, None)  # lpParam
        self.win = hWindow

    def mainStart(self):
        win32gui.PumpMessages()

    def mainEnd(self):
        win32gui.PostMessage(self.win, win32con.WM_DESTROY)

    def drawRectangle(self, Fhdc, rect: tuple[int, int, int, int]):
        win32gui.MoveToEx(Fhdc, rect[0], rect[1])
        win32gui.LineTo(Fhdc, rect[2], rect[1])
        win32gui.LineTo(Fhdc, rect[2], rect[3])
        win32gui.LineTo(Fhdc, rect[0], rect[3])
        win32gui.LineTo(Fhdc, rect[0], rect[1])
