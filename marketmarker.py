from kivy_garden.mapview import MapMarkerPopup

class MarketMarker(MapMarkerPopup):
    source = './marker.png'
    def on_release(self):
        '''
        Open up the LocationPopupMenu
        '''
        pass