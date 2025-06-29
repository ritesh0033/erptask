from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View


class SuperuserLoginView(LoginView):
    template_name = 'home/login.html'

    def form_valid(self, form):
        user = form.get_user()
        if not user.is_superuser:
            # Redirect back to login if user is not superuser
            return redirect('login')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dashboard')


class DashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'home/dashboard.html'

    def test_func(self):
        return self.request.user.is_superuser


class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
