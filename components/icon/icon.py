from django_components import component


@component.register('icon')
class IconComponent(component.Component):
    template_name = 'icon/icon.html'

    def get_context_data(self, name, img_url):
        return {
            'name': name,
            'img_url': img_url,
        }

    class Media:
        css = 'icon/icon.css'
        js = 'icon/icon.js'
