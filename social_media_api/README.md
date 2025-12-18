# Social Media API Documentation

This API allows users to register, login, manage profiles, create posts, comment on posts, follow other users, and view an aggregated feed. Built with Django and Django REST Framework (DRF).

---

## **Base URL**

```
http://127.0.0.1:8000/api/
```

---

## **Authentication**

All protected endpoints require **Token Authentication**.

### 1. Register a New User

**Endpoint:** `/accounts/register/`

* Method: POST
* Body (JSON):

```json
{
  "username": "john",
  "email": "john@example.com",
  "password": "password123",
  "bio": "Software developer"
}
```

* Response:

```json
{
  "token": "abc123...",
  "user": {
    "username": "john",
    "email": "john@example.com",
    "bio": "Software developer"
  }
}
```

### 2. Login

**Endpoint:** `/accounts/login/`

* Method: POST
* Body (JSON):

```json
{
  "username": "john",
  "password": "password123"
}
```

* Response:

```json
{
  "token": "abc123..."
}
```

### 3. User Profile

**Endpoint:** `/accounts/profile/`

* Method: GET
* Header: `Authorization: Token <token>`
* Response:

```json
{
  "username": "john",
  "email": "john@example.com",
  "bio": "Software developer",
  "followers_count": 0
}
```

---

## **Follow/Unfollow Users**

### 1. Follow a User

**Endpoint:** `/accounts/follow/<user_id>/`

* Method: POST
* Header: `Authorization: Token <token>`
* Response:

```json
{
  "detail": "You are now following jane"
}
```

### 2. Unfollow a User

**Endpoint:** `/accounts/unfollow/<user_id>/`

* Method: POST
* Header: `Authorization: Token <token>`
* Response:

```json
{
  "detail": "You have unfollowed jane"
}
```

---

## **Posts API**

### 1. List All Posts

**Endpoint:** `/posts/`

* Method: GET
* Optional query params:

  * `search` (filter by title/content)
  * `page` (pagination)
* Response:

```json
[
  {
    "id": 1,
    "author": "john",
    "title": "My First Post",
    "content": "Hello World!",
    "created_at": "2025-12-18T12:00:00Z",
    "updated_at": "2025-12-18T12:00:00Z",
    "comments": []
  }
]
```

### 2. Create a Post

**Endpoint:** `/posts/`

* Method: POST
* Header: `Authorization: Token <token>`
* Body (JSON):

```json
{
  "title": "New Post",
  "content": "Content of the post."
}
```

### 3. Retrieve a Post

**Endpoint:** `/posts/<post_id>/`

* Method: GET

### 4. Update a Post

**Endpoint:** `/posts/<post_id>/`

* Method: PUT/PATCH
* Header: `Authorization: Token <token>`
* Only the author can update.

### 5. Delete a Post

**Endpoint:** `/posts/<post_id>/`

* Method: DELETE
* Header: `Authorization: Token <token>`
* Only the author can delete.

---

## **Comments API**

### 1. List All Comments

**Endpoint:** `/comments/`

* Method: GET
* Pagination available

### 2. Create a Comment

**Endpoint:** `/comments/`

* Method: POST
* Header: `Authorization: Token <token>`
* Body (JSON):

```json
{
  "post": 1,
  "content": "This is my comment."
}
```

### 3. Retrieve a Comment

**Endpoint:** `/comments/<comment_id>/`

* Method: GET

### 4. Update a Comment

**Endpoint:** `/comments/<comment_id>/`

* Method: PUT/PATCH
* Header: `Authorization: Token <token>`
* Only the comment author can update.

### 5. Delete a Comment

**Endpoint:** `/comments/<comment_id>/`

* Method: DELETE
* Header: `Authorization: Token <token>`
* Only the comment author can delete.

---

## **Feed API**

### Get Feed of Followed Users

**Endpoint:** `/feed/`

* Method: GET
* Header: `Authorization: Token <token>`
* Returns posts from users that the current user follows, ordered by most recent.
* Response example:

```json
[
  {
    "id": 5,
    "author": "jane",
    "title": "New Post",
    "content": "Hello followers!",
    "created_at": "2025-12-18T12:00:00Z",
    "updated_at": "2025-12-18T12:00:00Z",
    "comments": []
  }
]
```

---

## **Likes API**

### Like a Post

**Endpoint:** `/posts/<post_id>/like/`

* Method: POST
* Header: `Authorization: Token <token>`
* Response:

```json
{
  "detail": "Post liked successfully."
}
```

### Unlike a Post

**Endpoint:** `/posts/<post_id>/unlike/`

* Method: POST
* Header: `Authorization: Token <token>`
* Response:

```json
{
  "detail": "Post unliked successfully."
}
```

---

## **Notifications API**

### View Notifications

**Endpoint:** `/notifications/`

* Method: GET
* Header: `Authorization: Token <token>`
* Returns a list of notifications related to the user (likes, comments, follows).
* Response example:

```json
[
  {
    "id": 1,
    "actor": "jane",
    "verb": "liked your post",
    "target": "My First Post",
    "is_read": false,
    "timestamp": "2025-12-18T12:00:00Z"
  }
]
```

---

## **Notes & Best Practices**

* Users **cannot follow themselves**.
* Protected endpoints require **Token Authentication**.
* Pagination defaults to 10 items per page.
* Use `search` query parameter on `/posts/` to filter posts by title or content.
* Only authors can edit or delete their posts/comments.
* Use the same token obtained from login/registration for all authenticated requests.

---

## **Example Workflow**

1. Register user → receive token
2. Login user → receive token
3. GET profile → verify user info
4. Follow another user → `/accounts/follow/<user_id>/`
5. Create posts → `/posts/`
6. Comment on posts → `/comments/`
7. View feed → `/feed/`
8. Update/delete posts or comments → only by author
9. Unfollow a user → `/accounts/unfollow/<user_id>/`

---

## **Tools for Testing**

* Postman or Insomnia for manual API testing.
* `curl` for command-line testing.
* Include token in `Authorization` header for authenticated requests.

---

## 🚀 Deployment Notes (Production)

### Procfile Configuration

To run this Django REST API in production, a **Procfile** is required. This file tells the hosting platform how to start the application.

Create a file named **`Procfile`** (no extension) in the project root:

```
web: gunicorn social_media_api.wsgi
```

#### Explanation

* **web** → Defines a web process that handles HTTP requests
* **gunicorn** → A production-grade WSGI server
* **social_media_api.wsgi** → The Django WSGI entry point

Gunicorn loads the Django application using the `wsgi.py` file and serves it to the internet.

### Requirements

Ensure Gunicorn is installed and included in `requirements.txt`:

```
gunicorn
```

### Database Configuration (PostgreSQL)

This project uses **PostgreSQL** via `dj-database-url`.

The database is configured using a single environment variable:

```
DATABASE_URL=postgresql://USER:PASSWORD@HOST:PORT/DB_NAME
```

Django automatically parses this value into engine, name, user, password, host, and port.

### Environment Variables

Common production environment variables:

```
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://...
ALLOWED_HOSTS=your-domain.com
```

### Static Files

Before deployment, collect static files:

```
python manage.py collectstatic
```

### Deployment Checklist

* DEBUG set to False
* ALLOWED_HOSTS configured
* PostgreSQL database connected
* Procfile present
* Gunicorn installed
* Static files collected

---
