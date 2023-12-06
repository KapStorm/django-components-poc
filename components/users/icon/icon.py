from django_components import component


@component.register('icon')
class IconComponent(component.Component):
    template_name = 'users/icon/icon.html'

    def get_context_data(self, name, img_url):
        return {
            'name': name,
            'img_url': img_url,
        }

    class Media:
        css = 'users/icon/icon.css'
        js = 'users/icon/icon.js'
