from kivy.app import App
from kivy.utils import platform
from kivymd.uix.dialog import MDDialog

class GpsHelper():
    has_centered_map = False
    def run(self):
        # Get a reference to GpsBlinker, then call Blink()
        gpsblinker = App.get_running_app().root.ids.mapview.ids.blinker
        # Start blinking the GpsBlinker
        gpsblinker.blink()
        # Request Permission to use GPS
        if platform == 'android':
            from android.permissions import request_permission, Permission
            def callback(permission, results):
                if all([res for res in results]):
                    print('Permission granted')
                else:
                    print("Did not get all permissions")
        # Configure GPS
        if platform == 'android' or platform == 'ios':
            from plyer import gps
            gps.configure(on_location=self.update_blinker_position, on_status=self.on_auth_status)
            gps.start(minTime=1000, minDistance=0)

    def update_blinker_position(self, *args, **kwargs):
        my_lat = kwargs['lat']
        my_lon = kwargs['lon']
        print("GPS Position: ", my_lat, my_lon)
        # Update GpsBlinker position
        gpsblinker = App.get_running_app().root.ids.mapview.ids.blinker
        gpsblinker.lat = my_lat
        gpsblinker.lon = my_lon

        # Center map on gps
        if not self.has_centered_map:
            mapview = App.get_running_app().root.ids.mapview
            mapview.center_on(my_lat, my_lon)
            self.has_centered_map = True
    

    def on_auth_status(self, general_status, status_message):
        if general_status == 'provider-enabled':
            ...
        else:
            self.open_gps_access_popup()

    def open_gps_access_popup(self):
        dialog = MDDialog(title= "GPS Error", text="You need to enable GPS access for the app to function properly")
        dialog.size_hint = [.8, .8]
        dialog.pos_hint = {'center_x': .5, 'center_y': .5}
        dialog.open()