from django.shortcuts import render

def test_page(request, menu_path = ""):
    return render(request, 'test_page.html', {'menu_path': menu_path})
