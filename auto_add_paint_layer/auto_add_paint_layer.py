from krita import *

class AutoAddPaintLayer(Extension):

    def __init__(self, parent):
        super().__init__(parent)
        self.win = None

    # Krita.instance() exists, so do any setup work
    def setup(self):
        notifier = Krita.instance().notifier()
        notifier.windowCreated.connect(self.onWindowCreated)

    def onWindowCreated(self):
        self.win = Krita.instance().activeWindow()
        self.win.activeViewChanged.connect(self.addPaintLayer)

    def addPaintLayer(self):
        doc = Krita.instance().activeDocument()
        if not doc:
            return
        nodes = doc.topLevelNodes()
        if len(nodes) == 1 and nodes[0].name() == "Background":
            Krita.instance().action("add_new_paint_layer").trigger()

    # called after setup(self)
    def createActions(self, window):
        pass
