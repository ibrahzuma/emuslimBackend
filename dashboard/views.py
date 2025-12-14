from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

class DashboardHomeView(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_users'] = User.objects.count()
        context['recent_users'] = User.objects.order_by('-date_joined')[:5]
        return context

class UserManagementView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = User
    template_name = 'dashboard/users.html'
    context_object_name = 'users'
    paginate_by = 10

    def get_queryset(self):
        queryset = User.objects.all().order_by('-date_joined')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(username__icontains=query) | 
                Q(email__icontains=query)
            )
        return queryset

    def get_template_names(self):
        if self.request.headers.get('HX-Request'):
            return ['dashboard/partials/user_list.html']
        return ['dashboard/users.html']
