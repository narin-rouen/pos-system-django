from django.shortcuts import render


def landing_page(request):
    """Render the landing page using the SB Admin template."""
    return render(request, 'index.html')
