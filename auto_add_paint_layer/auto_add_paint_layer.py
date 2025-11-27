from krita import *

class AutoAddPaintLayer(Extension):

    def __init__(self, parent):
        super().__init__(parent)

    # Krita.instance() exists, so do any setup work
    def setup(self):
        notifier = Krita.instance().notifier()
        notifier.imageCreated.connect(self.onDocumentCreated)

    def onDocumentCreated(self):
        doc = Krita.instance().activeDocument()
        if not doc:
            return
        nodes = doc.topLevelNodes()
        if len(nodes) == 1 and nodes[0].name() == "Background":
            Krita.instance().action("add_new_paint_layer").trigger()

    # called after setup(self)
    def createActions(self, window):
        pass
