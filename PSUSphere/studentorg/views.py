from django.views.generic.list import ListView
from studentorg.models import Organization

template_name = "home.hmtl"

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = "org_list.html"
    paginate_by = 5