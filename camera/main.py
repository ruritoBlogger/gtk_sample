import gi
import cv2
import os
from window import MyWindow

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf

def main():
    """
    opencvを用いて取得したカメラの情報をgtkを用いて出力する
    """

    Gtk.Settings.get_default().set_property("gtk-icon-theme-name", "Numix")
    Gtk.Settings.get_default().set_property("gtk-theme-name", "win32")

    win = MyWindow()
    win.connect("destroy",Gtk.main_quit)
    win.show_all()
    Gtk.main()
    
if __name__ == "__main__":
    main()
