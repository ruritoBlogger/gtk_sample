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
    css = b"""
    * {
        transition-property: color, background-color, border-color, background-image, padding, border-width;
        transition-duration: 1s;
        font-family: Cantarell;
        font-size: 20px;
    }
    GtkWindow {
        background: linear-gradient(153deg, #151515, #151515 5px, transparent 5px) 0 0,
                    linear-gradient(333deg, #151515, #151515 5px, transparent 5px) 10px 5px,
                    linear-gradient(153deg, #222, #222 5px, transparent 5px) 0 5px,
                    linear-gradient(333deg, #222, #222 5px, transparent 5px) 10px 10px,
                    linear-gradient(90deg, #1b1b1b, #1b1b1b 10px, transparent 10px),
                    linear-gradient(#1d1d1d, #1d1d1d 25%, #1a1a1a 25%, #1a1a1a 50%, transparent 50%, transparent 75%, #242424 75%, #242424);
        background-color: #131313;
        background-size: 20px 20px;
    }
    .button {
        color: black;
        background-color: #bbb;
        border-style: solid;
        border-width: 2px 0 2px 2px;
        border-color: #333;
        padding: 12px 4px;
    }
    .button:first-child {
        border-radius: 5px 0 0 5px;
    }
    .button:last-child {
        border-radius: 0 5px 5px 0;
        border-width: 2px;
    }
    .button:hover {
        padding: 12px 48px;
        background-color: #4870bc;
    }
    .button *:hover {
        color: white;
    }
    .button:hover:active,
    .button:active {
        background-color: #993401;
    }
        """
    style_provider = Gtk.CssProvider()
    style_provider.load_from_data(css)

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
