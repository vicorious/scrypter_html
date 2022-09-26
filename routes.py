
import logging
from fastapi import APIRouter
from fastapi import Depends
from fastapi.security import HTTPBearer

from AuthUtil import is_authorized

tags_metadata = [
    {"name": "Product Refernce", "description": "Get APIs to populate product Refernce"},
]

bearer = HTTPBearer()

router = APIRouter(
    prefix="/api",
    tags=["Product Refernce"],
    dependencies=[Depends(is_authorized)],
    responses={403: {"description": "Not found"}},
)

@router.get("/v1/main")
def main(param: str = ""):
    return "el param es: "+param