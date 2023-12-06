from django_components import component


@component.register('card')
class CardComponent(component.Component):
    template_name = 'users/card/card.html'

    def get_context_data(self, user):
        return {
            'user': user
        }

    class Media:
        css = 'users/card/card.css'
