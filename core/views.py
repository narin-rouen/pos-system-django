from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Q
from .models import User, Category
from .forms import LoginForm, UserForm, CategoryForm


def is_admin(user):
    """Check if user is admin."""
    return user.is_authenticated and user.role == 'ADMIN'


def login_view(request):
    """Login view - landing page for all users."""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, u_name=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.full_name}!')
                next_url = request.GET.get('next', 'dashboard')
                return redirect(next_url)
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    """Logout view."""
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('login')


@login_required
def dashboard_view(request):
    """Dashboard view - shows after login."""
    context = {
        'user': request.user,
    }
    return render(request, 'dashboard.html', context)


# User Management Views (Admin only)
@login_required
@user_passes_test(is_admin, login_url='dashboard')
def user_list_view(request):
    """List all users - admin only."""
    search_query = request.GET.get('search', '')
    
    users = User.objects.all().order_by('-date_joined')
    
    if search_query:
        users = users.filter(
            Q(f_name__icontains=search_query) |
            Q(l_name__icontains=search_query) |
            Q(u_name__icontains=search_query) |
            Q(email__icontains=search_query)
        )
    
    context = {
        'users': users,
        'search_query': search_query,
    }
    return render(request, 'users/list.html', context)


@login_required
@user_passes_test(is_admin, login_url='dashboard')
def user_create_view(request):
    """Create a new user - admin only."""
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'User {user.full_name} created successfully!')
            return redirect('user_list')
    else:
        form = UserForm()
    
    context = {
        'form': form,
        'action': 'Create',
    }
    return render(request, 'users/form.html', context)


@login_required
@user_passes_test(is_admin, login_url='dashboard')
def user_update_view(request, user_id):
    """Update a user - admin only."""
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'User {user.full_name} updated successfully!')
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    
    context = {
        'form': form,
        'action': 'Update',
        'user_obj': user,
    }
    return render(request, 'users/form.html', context)


@login_required
@user_passes_test(is_admin, login_url='dashboard')
def user_delete_view(request, user_id):
    """Delete a user - admin only."""
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        if user.id == request.user.id:
            messages.error(request, 'You cannot delete your own account!')
        else:
            username = user.full_name
            user.delete()
            messages.success(request, f'User {username} deleted successfully!')
        return redirect('user_list')
    
    context = {
        'user_obj': user,
    }
    return render(request, 'users/delete.html', context)


# Category Management Views (All authenticated users)
@login_required
def category_list_view(request):
    """List all categories."""
    search_query = request.GET.get('search', '')
    
    categories = Category.objects.all().order_by('name')
    
    if search_query:
        categories = categories.filter(name__icontains=search_query)
    
    context = {
        'categories': categories,
        'search_query': search_query,
    }
    return render(request, 'categories/list.html', context)


@login_required
def category_create_view(request):
    """Create a new category."""
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, f'Category "{category.name}" created successfully!')
            return redirect('category_list')
    else:
        form = CategoryForm()
    
    context = {
        'form': form,
        'action': 'Create',
    }
    return render(request, 'categories/form.html', context)


@login_required
def category_update_view(request, category_id):
    """Update a category."""
    category = get_object_or_404(Category, id=category_id)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            messages.success(request, f'Category "{category.name}" updated successfully!')
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    
    context = {
        'form': form,
        'action': 'Update',
        'category': category,
    }
    return render(request, 'categories/form.html', context)


@login_required
def category_delete_view(request, category_id):
    """Delete a category."""
    category = get_object_or_404(Category, id=category_id)
    
    if request.method == 'POST':
        category_name = category.name
        category.delete()
        messages.success(request, f'Category "{category_name}" deleted successfully!')
        return redirect('category_list')
    
    context = {
        'category': category,
    }
    return render(request, 'categories/delete.html', context)
