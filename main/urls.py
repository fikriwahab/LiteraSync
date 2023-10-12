from django.urls import path
from main.views import display_items, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from .views import increment_item
from .views import decrement_item
from .views import delete_item
from .views import get_items_json
from .views import add_item
from .views import delete_item_ajax

app_name = 'main'

urlpatterns = [
    path('', display_items, name='display_items'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('increment-item/<int:item_id>/', increment_item, name='increment_item'),
    path('decrement-item/<int:item_id>/', decrement_item, name='decrement_item'),
    path('delete-item/<int:item_id>/', delete_item, name='delete_item'),
    path('get-items-json/', get_items_json, name='get_items_json'),
    path('add-item/', add_item, name='add_item'),
    path('create-ajax/', add_item, name='create_ajax_item'),
    path('delete-item-ajax/<int:item_id>/', delete_item_ajax, name='delete_item_ajax'),

]
