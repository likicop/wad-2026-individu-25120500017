
from fastapi import APIRouter, HTTPException, Response
from app.schemas import MenuCreate, MenuOut
from app.services import create_menu, get_all_menu, get_menu_by_id

router = APIRouter(prefix='/api/menu', tags=['Menu'])

@router.post('', response_model=MenuOut, status_code=201)
def create(payload: MenuCreate, response: Response):
    item=create_menu(payload)
    response.headers['Location']=f"/api/menu/{item['id']}"
    return item

@router.get('', response_model=list[MenuOut])
def get_all(skip:int=0, limit:int=10, search:str=''):
    return get_all_menu(skip,limit,search)

@router.get('/{id}', response_model=MenuOut)
def get_one(id:int):
    item=get_menu_by_id(id)
    if not item:
        raise HTTPException(status_code=404, detail='Menu not found')
    return item
