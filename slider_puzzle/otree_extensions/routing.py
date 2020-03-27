from django.conf.urls import url
from slider_puzzle.consumers import SliderPuzzleConsumer

websocket_routes = [
    url(r'^slider_puzzle/(?P<game_id>\w+)/$', SliderPuzzleConsumer),
]