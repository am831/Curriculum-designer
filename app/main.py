from fastapi import FastAPI
from routers import post, user, auth
from config import Settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

#allows user to make requests from a different domain
app.add_middleware( 
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#re-routes requests
app.include_router(post.router) 
app.include_router(user.router)
app.include_router(auth.router)