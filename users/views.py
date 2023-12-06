from django.shortcuts import render

# Create your views here.
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

icons = [
    {
        'name': 'React',
        'img_url': 'https://cdn.worldvectorlogo.com/logos/react-2.svg',
    },
    {
        'name': 'Angular',
        'img_url': 'https://cdn.worldvectorlogo.com/logos/angular-icon.svg',
    },
    {
        'name': 'Scala',
        'img_url': 'https://cdn.worldvectorlogo.com/logos/scala-4.svg',
    }
]

context = {
    'users': mocked_users,
    'icons': icons,
}


def users(request):
    return render(request, 'users.html', context)


def users_tailwind(request):
    return render(request, 'users-tailwind.html', context)
