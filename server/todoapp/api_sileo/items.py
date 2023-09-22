from sileo.sileo.resource import Resource
from sileo.sileo.registration import register

from todoapp.models import Item
from todoapp.forms import ItemForm

class ItemResource(Resource):
    print("this works")
    query_set = Item.objects.exclude(removed=True).order_by('pub_date')

    allowed_methods = [
        'filter', 'get_pk', 'create', 'update', 'delete'
    ]

    fields = [
        'pk', 'text', 'completed'
    ]

    update_filter_fields = ['pk']
    delete_filter_fields = ['pk']

    size_per_request = 20

    form_class = ItemForm


register('todoapp', 'items', ItemResource, version='v1')
