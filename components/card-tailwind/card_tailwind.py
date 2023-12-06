from django_components import component


@component.register('card-tailwind')
class CardTailwind(component.Component):
    template_name = 'card-tailwind/card-tailwind.html'

    def get_context_data(self, user):
        return {
            'user': user
        }
