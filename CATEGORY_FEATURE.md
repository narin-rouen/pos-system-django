# Category Management Feature

## Overview

The Category Management feature allows all authenticated users to perform CRUD (Create, Read, Update, Delete) operations on product categories.

## Access Level

✅ **All authenticated users** can manage categories (not restricted to admin)

## Features

### 1. View Categories

- **URL:** `/categories/`
- List all categories with search functionality
- Shows category ID, name, and product count
- DataTables integration for sorting and pagination

### 2. Create Category

- **URL:** `/categories/create/`
- Simple form with category name field
- Validation for unique category names
- Success message after creation

### 3. Update Category

- **URL:** `/categories/<id>/update/`
- Edit existing category name
- Pre-filled form with current data
- Success message after update

### 4. Delete Category

- **URL:** `/categories/<id>/delete/`
- Confirmation page before deletion
- Warning if category has products
- Products with deleted category will have category set to NULL

## Navigation

- Click **"Category"** in the sidebar from any page
- Available to all logged-in users

## Usage Examples

### Create a Category

1. Login to the system
2. Click "Category" in sidebar
3. Click "Create New Category" button
4. Enter category name (e.g., "Electronics", "Beverages", "Snacks")
5. Click "Create Category"

### Edit a Category

1. Go to Categories list
2. Click the yellow edit icon next to a category
3. Modify the category name
4. Click "Update Category"

### Delete a Category

1. Go to Categories list
2. Click the red delete icon next to a category
3. Review the confirmation page
4. Click "Yes, Delete Category"

## Technical Details

### Models

```python
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
```

### Views

- `category_list_view` - List all categories
- `category_create_view` - Create new category
- `category_update_view` - Update existing category
- `category_delete_view` - Delete category

### Templates

- `templates/categories/list.html` - Category list
- `templates/categories/form.html` - Create/Edit form
- `templates/categories/delete.html` - Delete confirmation

### URLs

```python
/categories/ - List
/categories/create/ - Create
/categories/<id>/update/ - Update
/categories/<id>/delete/ - Delete
```

## Database Relationships

- Categories can have multiple Products (One-to-Many)
- When a category is deleted, products are set to NULL (SET_NULL)

## Search Functionality

The category list includes a search bar that filters categories by name in real-time.

## Screenshots Flow

1. **Dashboard** → Click "Category" in sidebar
2. **Category List** → View all categories, search, create new
3. **Create Form** → Simple form with name field
4. **Edit Form** → Pre-filled form to update
5. **Delete Confirmation** → Warning with product count

## Benefits

- Organize products by categories
- Easy product grouping
- Quick category management
- Search and filter capabilities
- Track products per category

---

**Status:** ✅ Fully functional and tested
**Server:** http://127.0.0.1:8000/categories/
