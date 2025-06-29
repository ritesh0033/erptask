from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Organization
from django.contrib.auth.mixins import LoginRequiredMixin

class OrganizationListView(LoginRequiredMixin, ListView):
    model = Organization
    template_name = 'usermanagement/organization_list.html'
    context_object_name = 'organizations'


class OrganizationCreateView(LoginRequiredMixin, CreateView):
    model = Organization
    fields = ['name', 'code']
    template_name = 'usermanagement/organization_form.html'
    success_url = reverse_lazy('organization_list')


class OrganizationUpdateView(LoginRequiredMixin, UpdateView):
    model = Organization
    fields = ['name', 'code']
    template_name = 'usermanagement/organization_form.html'
    success_url = reverse_lazy('organization_list')


class OrganizationDeleteView(LoginRequiredMixin, DeleteView):
    model = Organization
    template_name = 'usermanagement/organization_confirm_delete.html'
    success_url = reverse_lazy('organization_list')

