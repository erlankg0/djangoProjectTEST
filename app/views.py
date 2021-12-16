from django.shortcuts import render
from app.models import SAP
from django.views.generic import ListView, DetailView
from app.filters import SAPFilter


class SAPListView(ListView):
    model = SAP
    template_name = 'app/table.html'
    context_object_name = 'saps'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SAPListView, self).get_context_data(**kwargs)
        context['filters'] = SAPFilter(self.request.GET, queryset=self.get_queryset())
        return context


# def show_all_sap(request):
#     saps = SAP.objects.all()
#
#     filter_saps = SAPFilter(
#         request.GET,
#         queryset=SAP.objects.all()
#     )
#     context['filtered_apps'] = filter_saps.qs
#
#     return render(request, 'app/table.html', context)


class Home(ListView):
    model = SAP
    paginate_by = 5
    context_object_name = 'saps'
    template_name = 'app/index.html'


class DetailTableFilter(DetailView):
    model = SAP

# Create your views here.
