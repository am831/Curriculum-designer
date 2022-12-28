# Curriculum-designer
A curriculum designer that allows the user to organize and keep track of learning resources. All data is stored in a postgreSQL database.
* organize learning goals by year
* keep track of courses and subjects you need to learn
* specify how many hours per week you'll spend on each course, for how long, and other details
![5](https://user-images.githubusercontent.com/59581465/209742695-9e5f12fd-ba5f-4f1e-8fa0-1f7e65f76c26.png)

# Getting started
* Download the source code
* Add a .env file to the app directory that stores all sensitive data. See the Settings class in config.py for required fields.
* Download postgres and set up a database
* From within the app directory, start the server by running "python -m uvicorn main:app --reload"
* It is recommended to send requests to the API using the postman app or another API develeopment tool.  

# Routers
## Posts
### GET
* Gets all posts and outputs a table for each year to the command line. Is dependent on the user being logged in. The user needs to provide a bearer token. 
* Send the GET request to url/posts/
* Responses:
![posts-get](https://user-images.githubusercontent.com/59581465/209739627-2b807599-4637-4e74-8db5-5f904fb8454c.png)
### POST
* Create a post. Is dependent on the user being logged in. The user needs to provide a bearer token.
* Send the POST request to url/posts/
* Required request body in json format (only "course" is a required field):
![posts-post-req](https://user-images.githubusercontent.com/59581465/209740142-52c9a80f-7f14-4da4-9eb2-002c1ff6cca3.png)
* Responses:
![posts-post-res](https://user-images.githubusercontent.com/59581465/209740230-c9980dac-37ae-4bbe-bb98-33aa1d1db207.png)
### PUT
* Update a post. Is dependent on the user being logged in. The user needs to provide a bearer token.
* Send the PUT request to url/posts/{id} where id is the unique id of the post.
* Required request body in json format (only provide fields you want to update):
![posts-put-req](https://user-images.githubusercontent.com/59581465/209740488-39a9ee00-eac5-4024-bf9b-73a32c67433e.png)
* Responses:
![posts-put-res](https://user-images.githubusercontent.com/59581465/209740580-2523e156-5bd5-4036-b22f-de9f20f0c9e4.png)
### DELETE
* Delete a post. Is dependent on the user being logged in. The user needs to provide a bearer token.
* Send the DELETE request to url/posts/{id} where id is the unique id of the post.
* Responses:
![posts-put-res](https://user-images.githubusercontent.com/59581465/209740704-79399b3b-3ed2-4816-b305-313abe5180e4.png)
## Users
### POST
* Create a user.
* Send the POST request to url/users/
* Required request body in json format:
![users-post](https://user-images.githubusercontent.com/59581465/209740889-6dd24d08-4901-4f42-acfb-4fb625691f48.png)
* Responses:
![users-post-res](https://user-images.githubusercontent.com/59581465/209740936-814372aa-28b0-4042-a933-92573041af11.png)
### GET
* Get a user's information.
* Send the GET request to url/users/{id} where id is the unique id of the user.
* Responses:
![users-post-res](https://user-images.githubusercontent.com/59581465/209741049-2a0a8d83-23a4-4467-bd18-d3dd968b07a9.png)
## Auth
### POST
* Provide credentials and get a bearer token.
* Send the POST request to url/login 
* Required request body in form-data format:
![users-post-res](https://user-images.githubusercontent.com/59581465/209741271-ecf74e61-5a7e-441c-9070-30fb675947b6.png)
* Responses:
![auth-post-res](https://user-images.githubusercontent.com/59581465/209741333-3507e8d1-539a-4ee9-b717-8aaefec6476e.png)

# Demo using Postman
1. Create a user
![1](https://user-images.githubusercontent.com/59581465/209742645-1b7c6115-f4f9-4840-9fd3-24833e58e724.png)
2. Login. Then copy the bearer token
![2](https://user-images.githubusercontent.com/59581465/209742593-25518324-a200-46e0-afe2-ff3abd1e8950.png)
3. Create a post. Copy the bearer token under the authorization tab.
![3](https://user-images.githubusercontent.com/59581465/209741991-bc1f73cb-c28d-430a-83e5-99233f0c6932.png)
4. See all posts. Copy the bearer token under the authorization tab.
![4](https://user-images.githubusercontent.com/59581465/209742052-82e19aef-74d6-4d68-9eaf-a08f64c48463.png)
Your curriculim will be output to the command line, like this:
![5](https://user-images.githubusercontent.com/59581465/209742371-4ba46267-9b99-4ad4-b62c-be37bcbf428e.png)
