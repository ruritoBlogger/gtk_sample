import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf, Gdk

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
        # testというclassを付与
        input_box_context = self.input_box.get_style_context()
        input_box_context.add_class("test")

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

def gtk_style():
    style_provider = Gtk.CssProvider()
    style_provider.load_from_path("./test.css")

    Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(),
        style_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )

def main():
    gtk_style()
    Gtk.Settings.get_default().set_property("gtk-icon-theme-name", "Numix")
    Gtk.Settings.get_default().set_property("gtk-theme-name", "Mojave-light")
    win = MyWindow()
    win.connect("destroy",Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
