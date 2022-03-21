from numpy import source
from kivy_garden.mapview import MapMarkerPopup

class MarketMarker(MapMarkerPopup):
    source = 'part2/marker.png'
    def on_release(self):
        '''
        Open up the LocationPopupMenu
        '''
        pass