from django.shortcuts import render


# Create your views here.
def index(request):
    mocked_users = [
        {
            'name': 'Kappa',
            'position': 'Developer',
        },
        {
            'name': 'John Doe',
            'position': 'Designer',
        },
        {
            'name': 'Foo',
            'position': 'Manager',
        },
        {
            'name': 'Bar',
            'position': 'Tester',
        },
    ]

    context = {
        'users': mocked_users,
    }
    return render(request, 'index.html', context)
