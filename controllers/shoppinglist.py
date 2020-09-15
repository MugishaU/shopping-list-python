shopping_list = [
    {'id': 1, 'item':'Bread', 'qty': 1},
    {'id': 2, 'item':'Milk', 'qty':2},
    {'id': 3, 'item':'Eggs', 'qty':12},  
]
def index(req):
    return [item for item in shopping_list], 200

def create(req):
    new_item = req.get_json()
    new_item['id'] = len(shopping_list) + 1
    shopping_list.append(new_item)
    return new_item,200