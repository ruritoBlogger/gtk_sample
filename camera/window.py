import gi
import cv2
import numpy as np
from PIL import Image

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf, GLib

class MyWindow(Gtk.Window):
    """
    opencvから受け取ったカメラの情報を出力する.

    """
    def __init__(self):
        Gtk.Window.__init__(self, title="show picture")
      
        # 画面のレイアウトを整える
        grid = Gtk.Grid(column_spacing=20, row_spacing=10)
        self.add(grid)
        self.set_border_width(10)

        # 画像名を入力する欄の設定
        input_box = Gtk.Box(spacing=0)
        grid.add(input_box)
        self.entry = Gtk.Entry()
        self.entry.set_text("test.jpg")
        input_box.pack_start(self.entry, True, True, 0)

        # 保存するボタンの設定
        button_box = Gtk.Box(spacing=0)
        #self.grid.attach(button_box, 1, 0, 2, 1)
        input_box.add(button_box)
        button = Gtk.Button.new_with_label("保存")
        button.connect("clicked", self.save_image)
        button_box.pack_start(button, True, True,0)

        self.cap = cv2.VideoCapture(0)
        self._image = Gtk.Image()
        grid.attach(self._image, 0,1,1,1)
        GLib.timeout_add( 32, self.getImage )

    def save_image(self, button):
        """
        opencvから取得したカメラの情報を保存する
        取得したカメラの情報をnp.arrayに変換する
        変換後の情報はPILを用いて保存する
        """
        while True:
            _, frame = self.cap.read()
        
            if frame is not None:
                frame = np.array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                image = Image.fromarray(frame)
                image.save("./pictures/" + self.entry.get_text())
                break

    def getImage(self):
        """
        opencvからカメラの情報を取得する
        """

        while True:
            _, frame = self.cap.read()
        
            if frame is not None:

                # opencvではBGR, GdkではRGBが用いられているので変換してから渡す
                self.update_image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                break

        return True

    def update_image(self, capture_data):
        """
        受け取ったカメラの情報をGdk特有のクラスに変形してウィンドウに出力する


        Parameters
        ----------
        capture_data: list
            カメラから取得した画像データ
        """

        capture_data=capture_data.astype('uint8')
        h,w,c=capture_data.shape
        if hasattr(GdkPixbuf.Pixbuf,'new_from_bytes'):
            Z = GLib.Bytes.new(capture_data.tobytes())
            self._image.set_from_pixbuf(GdkPixbuf.Pixbuf.new_from_bytes(Z, GdkPixbuf.Colorspace.RGB, c==4, 8, w, h, w*c))
        self._image.set_from_pixbuf(GdkPixbuf.Pixbuf.new_from_data(capture_data.tobytes(),  GdkPixbuf.Colorspace.RGB, c==4, 8, w, h, w*c, None, None))
