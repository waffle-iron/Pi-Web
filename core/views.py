from django.shortcuts import render


def home(request):
    if request.user.is_authenticated():
        return render(request, 'core/cover.html', {'base': 'base.html'})
    else:
        return render(request, 'core/cover.html', {'base': 'base_visitor.html'})
