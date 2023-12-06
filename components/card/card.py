from django_components import component


@component.register('card')
class CardComponent(component.Component):
    template_name = 'card/card.html'

    def get_context_data(self, user):
        return {
            'user': user
        }

    class Media:
        css = 'card/card.css'
