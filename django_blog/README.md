## Blog Post Management

Users can:
- View all blog posts
- View individual post details

Authenticated users can:
- Create new blog posts
- Edit their own posts
- Delete their own posts

Permissions:
- Only the author of a post may edit or delete it
- Unauthorized users are redirected or denied access

Technologies Used:
- Django Class-Based Views
- Django Authentication System
- ModelForms

## Comment System

Users can view comments on all blog posts.

Authenticated users can:
- Add comments to blog posts
- Edit their own comments
- Delete their own comments

Permissions:
- Only the comment author may edit or delete a comment
- Anonymous users can only read comments

Technologies:
- Django ModelForm
- Django Class-Based Views
- Authentication & Permissions


## Tagging & Search

### Tagging
- Posts can have multiple tags
- Tags are added as comma-separated values when creating or editing a post
- Clicking a tag displays all posts with that tag

### Search
- Users can search posts by title, content, or tag name
- Search is case-insensitive
- Results are displayed on a dedicated search results page
