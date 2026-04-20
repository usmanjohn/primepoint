from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Master
from .forms import MasterForm

class MasterListView(ListView):
    model = Master
    template_name = 'masters/master_list.html'
    context_object_name = 'masters'
    ordering = ['-created_at']

class MasterDetailView(DetailView):
    model = Master
    template_name = 'masters/master_detail.html'
    pk_url_kwarg = 'master_id'

class MasterCreateView(LoginRequiredMixin, CreateView):
    model = Master
    form_class = MasterForm
    template_name = 'masters/master_form.html'
    success_url = reverse_lazy('masters-list')

class MasterUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Master
    form_class = MasterForm
    template_name = 'masters/master_form.html'
    success_url = reverse_lazy('masters-list')

    def test_func(self):
        # Only allow the owner of the profile associated with this Master to edit
        master = self.get_object()
        return self.request.user == master.profile.user

class MasterDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Master
    template_name = 'masters/master_confirm_delete.html'
    success_url = reverse_lazy('masters-list')

    def test_func(self):
        master = self.get_object()
        return self.request.user == master.profile.user
