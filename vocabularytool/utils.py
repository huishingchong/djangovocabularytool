import random
import string
from django.template import defaultfilters

from django.utils.text import slugify

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title, allow_unicode=True)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def render_to_pdf(template_src, context_dict={}): #context_dict parameter passed from views function contains all variables required for the PDF
    template = get_template(template_src) #invoice template is passed into function as template_src parameter to be rendered
    html  = template.render(context_dict)
    result = BytesIO() #to deal with bytes objects
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result, encoding='UTF-8') #UTF- 8 encoding supports Chinese language
    if not pdf.err: #checks for error in PDF generation
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
