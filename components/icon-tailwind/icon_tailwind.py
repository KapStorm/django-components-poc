from django_components import component


@component.register('icon-tailwind')
class IconTailwind(component.Component):
    template_name = 'icon-tailwind/icon-tailwind.html'

    def get_context_data(self, name, img_url):
        return {
            'name': name,
            'img_url': img_url,
        }

    class Media:
        js = 'icon-tailwind/icon-tailwind.js'
