import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="show picture")

        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.input_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.grid.add(self.input_box)
        
        self.entry = Gtk.Entry()
        self.entry.set_text("/home/rurito/mysketch/gtk_sample/lena.png")
        self.input_box.pack_start(self.entry, True, True, 0)

        button_box = Gtk.Box(spacing=6)
        self.grid.attach(button_box, 1, 0, 2, 1)
        button = Gtk.Button.new_with_label("show")
        button.connect("clicked", self.on_show_clicked)
        button_box.pack_start(button, True, True,0)
        
        data = GdkPixbuf.Pixbuf.new_from_file(self.entry.get_text())
        self.image = Gtk.Image()
        self.image.set_from_pixbuf(data)
        self.grid.attach(self.image, 0,1,1,1)
    
    def on_show_clicked(self, button):
        data = GdkPixbuf.Pixbuf.new_from_file(self.entry.get_text())
        self.image.set_from_pixbuf(data)

win = MyWindow()
win.connect("destroy",Gtk.main_quit)
win.show_all()
Gtk.main()
