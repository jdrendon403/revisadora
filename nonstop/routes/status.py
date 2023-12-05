from fastapi import APIRouter, Body, status as httpstatus, Depends
from fastapi.responses import JSONResponse
from schemas.status import Status
from middleware.jwt_bearer import JWTBearer

gdata = Status()
status = APIRouter()

@status.put("/write_status/", 
            tags=["Non Stop Status"],
            response_model=Status,
            dependencies=[Depends(JWTBearer())]
            )
def write_status(data: Status = Body(...)):
    global gdata
    gdata = data
    return JSONResponse(content=gdata.model_dump(), status_code=httpstatus.HTTP_202_ACCEPTED)

@status.get("/read_status/",
            tags=["Non Stop Status"],
            response_model=Status,
            dependencies=[Depends(JWTBearer())]
            )
def read_status():
    return JSONResponse(content=gdata.model_dump(), status_code=httpstatus.HTTP_200_OK)
