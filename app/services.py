
DATABASE=[]
NEXT_ID=1

def create_menu(payload):
    global NEXT_ID
    item={"id":NEXT_ID,"nama":payload.nama,"sku":payload.sku,"kategori":payload.kategori}
    DATABASE.append(item)
    NEXT_ID+=1
    return item

def get_all_menu(skip=0,limit=10,search=""):
    data=DATABASE
    if search:
        data=[x for x in data if search.lower() in x['nama'].lower()]
    return data[skip:skip+limit]

def get_menu_by_id(id):
    for item in DATABASE:
        if item['id']==id:
            return item
    return None
