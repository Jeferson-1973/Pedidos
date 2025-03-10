# pip install xhtml2pdf
from xhtml2pdf import pisa
from django.template.loader import get_template
from io import BytesIO
from django.http import HttpResponse


def render_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result) # Sistema de codificación para formatos pdf
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    return HttpResponse("<h1>NO SE PUDO CREAR EL DOCUMENTO</h1>")


