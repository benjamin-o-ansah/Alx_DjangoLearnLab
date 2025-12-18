# Social Media API Documentation

This API allows users to register, login, manage profiles, create posts, and comment on posts. Built with Django and Django REST Framework (DRF).

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

* Response: Returns the created post with author and comments.

### 3. Retrieve a Post

**Endpoint:** `/posts/<post_id>/`

* Method: GET
* Response includes all post fields and nested comments.

### 4. Update a Post

**Endpoint:** `/posts/<post_id>/`

* Method: PUT/PATCH
* Header: `Authorization: Token <token>`
* Only the author can update.
* Body (JSON):

```json
{
  "title": "Updated Title",
  "content": "Updated content."
}
```

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
* Response:

```json
[
  {
    "id": 1,
    "post": 1,
    "author": "jane",
    "content": "Great post!",
    "created_at": "2025-12-18T12:10:00Z",
    "updated_at": "2025-12-18T12:10:00Z"
  }
]
```

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

* Response: Returns the created comment.

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

## **Notes & Tips**

* All POST, PUT, PATCH, DELETE endpoints require **Token Authentication**.
* Pagination defaults to 10 items per page.
* Use `search` query parameter on `/posts/` to filter posts by title or content.
* Always include `Authorization: Token <token>` in headers for protected endpoints.

---

## **Example Workflow**

1. Register user → receive token
2. Login user → receive token
3. GET profile → verify user info
4. POST new post → token required
5. GET posts → list posts
6. POST comment → token required
7. GET posts/<post_id>/ → see nested comments
8. Update/delete posts or comments → only by author

---

## **Tools for Testing**

* Postman or Insomnia for manual API testing.
* `curl` for command-line testing.
* Include token in `Authorization` header for authenticated requests.
