from kivy_garden.mapview import MapMarkerPopup

class MarketMarker(MapMarkerPopup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source = 'marker.png'
    def on_release(self):
        '''
        Open up the LocationPopupMenu
        '''
        pass