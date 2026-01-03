# POS System - User Management Feature

A comprehensive Point of Sale system with advanced user management and authentication.

## 🎯 Features Implemented

### ✅ User Management

- **Admin-only user CRUD operations**
  - Create new users (admin only)
  - View all users with search functionality
  - Update user information
  - Delete users (cannot delete self)

### ✅ Authentication System

- **No signup** - Only admins can create accounts
- **Login-only access** - Users must have an account created by admin
- Custom user model with roles: ADMIN, MANAGER, CASHIER, GUEST
- Secure password hashing
- Session-based authentication

### ✅ Database Schema

All models implemented per your specification:

**Users Table:**

- id, f_name, l_name, u_name, email, password, profile (image), role

**Categories Table:**

- id, name

**Products Table:**

- id, name, cost, price, qty, category_id, image, barcode

**Stocks Table:**

- id, code, date, total_cost, discount

**Sales Table:**

- id, code, date, total_price, discount

**Stock Details Table:**

- id, product_id, stock_id, qty, cost, discount, total

**Sale Details Table:**

- id, product_id, sale_id, qty, price, discount, total

### ✅ UI/UX

- **Landing page** shows login form with sidebar/navbar
- **Sidebar** includes: User, Category, Product, Stock, Sale, Report
- **Non-authenticated users** are redirected to login on all routes
- Professional Bootstrap admin template (SB Admin)
- Responsive design

## 🚀 Quick Start

### 1. Admin Login

The system comes with a default admin account:

```
Username: admin
Password: admin123
```

**Visit:** http://127.0.0.1:8000/

### 2. Access User Management

After logging in as admin:

- Click **"User"** in the sidebar
- View all users
- Create new users (only admin can do this)
- Edit or delete existing users

## 📋 User Roles

| Role    | Description                          | Access Level        |
| ------- | ------------------------------------ | ------------------- |
| ADMIN   | Full system access + user management | All features        |
| MANAGER | Manage operations                    | Limited features    |
| CASHIER | Process sales                        | POS operations only |
| GUEST   | View-only access                     | Read-only           |

## 🔐 Security Features

1. **No Public Registration** - Only admins can create accounts
2. **Login Required** - All routes protected by authentication
3. **Role-based Access** - Users see only what their role permits
4. **Password Hashing** - All passwords securely hashed
5. **Session Management** - Secure session handling

## 📁 Project Structure

```
point-of-sale-sysetm/
├── core/                          # Main POS application
│   ├── models.py                  # Database models (User, Product, etc.)
│   ├── views.py                   # View functions
│   ├── forms.py                   # Forms (Login, User management)
│   ├── backends.py                # Custom authentication backend
│   ├── urls.py                    # URL routing
│   └── management/
│       └── commands/
│           └── createadmin.py     # Command to create admin user
├── templates/                     # HTML templates
│   ├── login.html                 # Login page (landing page)
│   ├── dashboard.html             # Dashboard after login
│   └── users/                     # User management templates
│       ├── list.html              # User list
│       ├── form.html              # Create/Edit user
│       └── delete.html            # Delete confirmation
├── pos_system/                    # Django project settings
│   ├── settings.py                # Configuration
│   └── urls.py                    # Main URL routing
├── startbootstrap-sb-admin-gh-pages/  # Bootstrap template assets
└── db.sqlite3                     # SQLite database
```

## 🔧 Management Commands

### Create Admin User

```bash
python manage.py createadmin
```

### Create Custom User (via Django shell)

```bash
python manage.py shell
```

```python
from core.models import User

User.objects.create_user(
    u_name='johndoe',
    email='john@example.com',
    password='secure123',
    f_name='John',
    l_name='Doe',
    role='CASHIER'
)
```

## 🌐 Available URLs

| URL                   | Description        | Access        |
| --------------------- | ------------------ | ------------- |
| `/`                   | Redirects to login | Public        |
| `/login/`             | Login page         | Public        |
| `/logout/`            | Logout             | Authenticated |
| `/dashboard/`         | Main dashboard     | Authenticated |
| `/users/`             | User list          | Admin only    |
| `/users/create/`      | Create new user    | Admin only    |
| `/users/<id>/update/` | Update user        | Admin only    |
| `/users/<id>/delete/` | Delete user        | Admin only    |
| `/admin/`             | Django admin panel | Superuser     |

## 🎨 Sidebar Navigation

The sidebar includes these sections (icons included):

- 👥 **User** - User management (admin only)
- 📋 **Category** - Product categories
- 📦 **Product** - Product management
- 🏪 **Stock** - Inventory management
- 🛒 **Sale** - Sales transactions
- 📊 **Report** - Reports and analytics

## 🔄 Workflow

### For Admin:

1. Login with admin credentials
2. Navigate to **User** section
3. Click **"Create New User"**
4. Fill in user details and assign role
5. Save - User can now login

### For Regular Users:

1. Admin creates account for them
2. User receives credentials
3. User logs in at login page
4. Access features based on their role
5. Cannot create accounts for others

## 🛠️ Technical Details

### Custom User Model

- Uses `u_name` as USERNAME_FIELD instead of default username
- Custom authentication backend for `u_name` login
- Extends AbstractBaseUser and PermissionsMixin
- Password validation and hashing built-in

### Authentication

- Custom backend: `core.backends.UsernameAuthBackend`
- Login required on all routes via `@login_required` decorator
- Role checking via `@user_passes_test(is_admin)`

### Database

- SQLite for development
- All tables use custom table names matching your schema
- Foreign keys with proper relationships
- Decimal fields for money values

## 📝 Next Steps

You can now extend the system with:

1. **Category Management** - CRUD for product categories
2. **Product Management** - Add/edit products with images
3. **Stock Management** - Track inventory purchases
4. **Sales Module** - Process customer transactions
5. **Reports** - Sales reports, inventory reports, etc.

## 🔑 Default Credentials

**Admin Account:**

- Username: `admin`
- Password: `admin123`
- Role: ADMIN

⚠️ **Important:** Change the admin password after first login!

## 🎯 Key Achievements

✅ No signup functionality - admin-only user creation  
✅ Login form as landing page with full navigation  
✅ All sidebar links redirect to login for unauthenticated users  
✅ Complete user CRUD for admins  
✅ Role-based access control  
✅ All database models implemented  
✅ Professional UI with SB Admin template  
✅ Secure authentication system

---

**Server Running:** http://127.0.0.1:8000/  
**Login to get started!**
