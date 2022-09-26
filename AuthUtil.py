from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

bearer = HTTPBearer()

def is_authorized(token: HTTPAuthorizationCredentials = Depends(bearer)):
    try:
        return True
    except Exception as ex:
        raise HTTPException(status_code=403)
    raise HTTPException(status_code=403)
