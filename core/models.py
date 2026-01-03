from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """Custom user manager."""
    
    def create_user(self, u_name, email, password=None, **extra_fields):
        """Create and save a regular user."""
        if not u_name:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(u_name=u_name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, u_name, email, password=None, **extra_fields):
        """Create and save a superuser."""
        extra_fields.setdefault('role', 'ADMIN')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(u_name, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model matching the database schema."""
    
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('MANAGER', 'Manager'),
        ('CASHIER', 'Cashier'),
        ('GUEST', 'Guest'),
    ]
    
    f_name = models.CharField(max_length=100, verbose_name='First Name')
    l_name = models.CharField(max_length=100, verbose_name='Last Name')
    u_name = models.CharField(max_length=100, unique=True, verbose_name='Username')
    email = models.EmailField(unique=True, verbose_name='Email')
    password = models.CharField(max_length=255)  # Handled by AbstractBaseUser
    profile = models.ImageField(upload_to='profiles/', blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='GUEST')
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'u_name'
    REQUIRED_FIELDS = ['email', 'f_name', 'l_name']
    
    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return f"{self.f_name} {self.l_name} ({self.u_name})"
    
    @property
    def full_name(self):
        return f"{self.f_name} {self.l_name}"
    
    def is_admin(self):
        return self.role == 'ADMIN'


class Category(models.Model):
    """Category model."""
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Product(models.Model):
    """Product model."""
    name = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.IntegerField(default=0, verbose_name='Quantity')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    barcode = models.CharField(max_length=100, unique=True, blank=True, null=True)
    
    class Meta:
        db_table = 'products'
    
    def __str__(self):
        return self.name


class Stock(models.Model):
    """Stock/Purchase model."""
    code = models.CharField(max_length=50, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    class Meta:
        db_table = 'stocks'
    
    def __str__(self):
        return f"Stock {self.code}"


class StockDetail(models.Model):
    """Stock detail/line items."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stock_details')
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='details')
    qty = models.IntegerField(verbose_name='Quantity')
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = 'stock_details'
    
    def __str__(self):
        return f"{self.product.name} - Stock {self.stock.code}"


class Sale(models.Model):
    """Sale/Invoice model."""
    code = models.CharField(max_length=50, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    class Meta:
        db_table = 'sales'
    
    def __str__(self):
        return f"Sale {self.code}"


class SaleDetail(models.Model):
    """Sale detail/line items."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sale_details')
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='details')
    qty = models.IntegerField(verbose_name='Quantity')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = 'sale_details'
    
    def __str__(self):
        return f"{self.product.name} - Sale {self.sale.code}"
