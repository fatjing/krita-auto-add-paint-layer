from .auto_add_paint_layer import AutoAddPaintLayer

Krita.instance().addExtension(AutoAddPaintLayer(Krita.instance()))
