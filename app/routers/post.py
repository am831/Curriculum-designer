import models, schemas, oauth2
from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import session
from database import get_db
from typing import List, Optional
from prettytable import PrettyTable

router = APIRouter(
    prefix = "/posts",
    tags= ['Posts']
)

@router.get("/", response_model=List[schemas.PostResponse])
def get_posts(db: session = Depends(get_db), 
current_user: int = Depends(oauth2.get_current_user), 
search: Optional[str] = ""):
    """
    gets all posts makes a table for each year. is dependent on a user being 
    logged in. the user needs to provide an access token. the dependency calls 
    get_current_user(), and runs the access token. if an error is returned, 
    the user can't perform the action
    """
    posts = db.query(models.Post).filter(models.Post.owner_id == 
    current_user.id, models.Post.course.contains(search)).all()
    tables = {}
    years = []
    for item in posts:
        if item.year not in years:
            tables[str(item.year)] = PrettyTable()
            tables[str(item.year)].field_names = ["course", "duration", 
            "effort", "comments", "link"]
            years.append(item.year)
    for item in posts:
        tables[str(item.year)].add_row([item.course, item.duration, 
        item.effort, item.comments, item.link])
        tables[str(item.year)].add_row([" ", " ", " ", " ", " "])
    years.sort()
    for item in years:
        print("Year", str(item))
        print(tables[str(item)], "\n")
    return posts

@router.post("/", status_code = status.HTTP_201_CREATED, 
response_model=schemas.PostResponse)
def create(post: schemas.PostCreate, db: session = Depends(get_db), 
current_user: int = Depends(oauth2.get_current_user)):
    """
    create a post. is dependent on a user being logged in. the user needs to 
    provide an access token. the dependency calls get_current_user(), and runs 
    the access token. if an error is returned, the user can't perform the 
    action
    """
    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def deletePost(id: int, db: session = Depends(get_db), 
current_user: int = Depends(oauth2.get_current_user)):
    """
    delete a post. is dependent on a user being logged in. the user needs to 
    provide an access token. the dependency calls get_current_user(), and runs 
    the access token. if an error is returned, the user can't perform the 
    action
    """
    #set up the query
    post_query = db.query(models.Post).filter(models.Post.id == id) 
    #run the query and find the post
    post = post_query.first() 

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"post with id: {id} does not exist ")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
        detail="Not authorized to perform requested action")

    post_query.delete(synchronize_session =False)
    db.commit()
    return Response(status_code = status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.PostResponse)
def update(id: int, updated_post: schemas.PostCreate, 
db: session = Depends(get_db), 
current_user: int = Depends(oauth2.get_current_user)):
    """
    update a post. is dependent on a user being logged in. the user needs to 
    provide an access token. the dependency calls get_current_user(), and runs 
    the access token. if an error is returned, the user can't perform the 
    action 
    """
    post_query = db.query(models.Post).filter(models.Post.id == id) 
    post = post_query.first() 

    if post == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"post with id: {id} does not exist ")
    if post.owner_id != current_user.id: 
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
        detail="Not authorized to perform requested action")

    post_query.update(updated_post.dict(), synchronize_session = False) 
    db.commit()
    return post_query.first()