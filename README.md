# NewsHere-API

## Step by step instruction how to launch this project.

1. Clone this repository to your local computer by pasting the command below:

`git clone https://github.com/StarLooorD/NewsHere-API.git`

If docker works:

2. Open the directory with this repository cloned on you local computer and past the command below to launch project:

`docker-compose up`

All is DONE! Now project should work.

Else:

2. Install all requirements from requirements.txt:

`pip install -r requirements.txt`

3. Migrate database with command below:

`python manage.py migrate`

4. Run server using command below:

`python manage.py runserver`

All is DONE! Now project should work.


## Using API endpoints:

### API deployed on Heroku:

https://newsheartx.herokuapp.com/api/v1/news/posts/

### Adding Postman Documentation link for more detailed info:

https://documenter.getpostman.com/view/9281520/TW6zFSaL

Choose there NewsHereEnv as environment, and you are ready to use it.

### Main endpoints:

1. Login User -> method: POST `https://newsheartx.herokuapp.com/auth/token/login/`;

2. Logout User -> method: POST `https://newsheartx.herokuapp.com/auth/token/logout/`;

3. Register new user -> method: POST `https://newsheartx.herokuapp.com/auth/users/`;


4. Get all posts(news) -> method: GET `https://newsheartx.herokuapp.com/api/v1/news/posts/`;

5. Get post bu id -> method: GET `https://newsheartx.herokuapp.com/api/v1/news/post/<post_id>/`;

6. Create new post -> method: POST `https://newsheartx.herokuapp.com/api/v1/news/posts/`;

7. Update post by id -> method: PUT `https://newsheartx.herokuapp.com/api/v1/news/post/<post_id>/`;

8. Delete post by id -> method: DELETE `https://newsheartx.herokuapp.com/api/v1/news/post/<post_id>/`;


9. Get all comments -> method: GET `https://newsheartx.herokuapp.com/api/v1/news/comments/`;

10. Create new comment -> method: POST `https://newsheartx.herokuapp.com/api/v1/news/comment/`;

11. Update comment by id -> method: PUT `https://newsheartx.herokuapp.com/api/v1/news/comment/<comment_id>/`;

12. Delete comment by id -> method: DELETE `https://newsheartx.herokuapp.com/api/v1/news/comment/<comment_id>/`;


13. Upvote/Unvote on post -> method: POST `https://newsheartx.herokuapp.com/api/v1/news/post/upvote/<post_id>/`.
