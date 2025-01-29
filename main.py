from fastapi import FastAPI
from datetime import datetime,timezone
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=False, 
    allow_methods=["*"], 
    allow_headers=["*"], 
)

@app.get('/stage_zero')
def index():
    #return registered email,current datetime as an ISO format,GitHub url
    utc_current = datetime.now(timezone.utc)
    return{
        "email":"oguntayohabeebullah@gmail.com",
        "current_datetime":utc_current.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "github_url":"https://github.com/Oguntayo/hng12-stage-public-api"
    }