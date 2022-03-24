from kivymd.uix.dialog import MDInputDialog
from urllib.parse import quote
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
class SearchPopupMenu(MDInputDialog):
    title = 'Search by Address'
    text_button_ok = "Search"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = [.9, .3]
        self.events_callback = self.callback

    def callback(self, *args):
        address = self.text_field.text
        self.geocode_get_lat_lon(address)

    def geocode_get_lat_lon(self, address):
        address = quote(address)
        api_key = "jspHzeMeAxIm3GmSSyiVFV9ZD36sI61FWQjSrvRF134"
        url = f"https://geocoder.ls.hereapi.com/6.2/geocode.json?searchtext={address}&apiKey={api_key}"
        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.failure)

    def success(self, urlrequst, result):
        print("Success")
        latitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Latitude']
        longitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Longitude']
        app = App.get_running_app()
        mapview = app.root.ids.mapview
        mapview.center_on(latitude, longitude)

    def failure(self, urlrequst, result):
        print("Failure")
        print(result)
    
    def error(self, urlrequst, result):
        print("Error")
        print(result)