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
    return new_item, 200

def destroy(req):
    body = req.get_json()
    item = find_by_id(body.uid)
    shopping_list.remove(item)
    return f'DELETED: {item}', 204



def find_by_id(uid):
    try:
        return next(item for item in shopping_list if shopping_list['id'] == uid)
    except:
        raise BadRequest(f"We don't have that cat with id {uid}!")
