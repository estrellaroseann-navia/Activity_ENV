from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from studentorg.models import Organization
from studentorg.forms import OrganizationForm
from django.urls import reverse_lazy

template_name = "home.hmtl"

paginated_by=5

class HomePageView(ListView):
        model = Organization
        context_object_name = 'home'
        template_name = "home.html"

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_add.html"
    success_url = reverse_lazy('organization-list')

class OrganizationCreateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_edit.html"
    success_url = reverse_lazy('organization-list')