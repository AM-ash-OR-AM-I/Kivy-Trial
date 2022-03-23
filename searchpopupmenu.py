from kivymd.uix.dialog import MDInputDialog

class SearchPopupMenu(MDInputDialog):
    type = "custom"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        type = "custom"
        self.size_hint = [.9, .9]