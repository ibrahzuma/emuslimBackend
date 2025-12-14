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

# --- Dua Management ---
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from duas.models import Dua, Category

class DuaListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Dua
    template_name = 'dashboard/duas.html'
    context_object_name = 'duas'
    paginate_by = 10

    def get_queryset(self):
        queryset = Dua.objects.select_related('category').all().order_by('id')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(short_name_en__icontains=query) | 
                Q(full_dua_en__icontains=query)
            )
        return queryset

class DuaCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Dua
    fields = ['category', 'short_name_en', 'short_name_ar', 'full_dua_en', 'full_dua_ar']
    template_name = 'dashboard/dua_form.html'
    success_url = reverse_lazy('dashboard:duas')

class DuaUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Dua
    fields = ['category', 'short_name_en', 'short_name_ar', 'full_dua_en', 'full_dua_ar']
    template_name = 'dashboard/dua_form.html'
    success_url = reverse_lazy('dashboard:duas')

class DuaDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Dua
    template_name = 'dashboard/dua_confirm_delete.html'
    success_url = reverse_lazy('dashboard:duas')

# --- Category Management ---
class CategoryListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Category
    template_name = 'dashboard/categories.html'
    context_object_name = 'categories'
    paginate_by = 10

class CategoryCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Category
    fields = ['name']
    template_name = 'dashboard/category_form.html'
    success_url = reverse_lazy('dashboard:categories')

class CategoryUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Category
    fields = ['name']
    template_name = 'dashboard/category_form.html'
    success_url = reverse_lazy('dashboard:categories')

class CategoryDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Category
    template_name = 'dashboard/category_confirm_delete.html'
    success_url = reverse_lazy('dashboard:categories')

# --- Islamic Content Management ---
from islamic_content.models import Announcement, DailyReminder

# Announcements
class AnnouncementListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Announcement
    template_name = 'dashboard/announcements.html'
    context_object_name = 'announcements'
    paginate_by = 10

class AnnouncementCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Announcement
    fields = ['title', 'content', 'is_active']
    template_name = 'dashboard/announcement_form.html'
    success_url = reverse_lazy('dashboard:announcements')

class AnnouncementUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Announcement
    fields = ['title', 'content', 'is_active']
    template_name = 'dashboard/announcement_form.html'
    success_url = reverse_lazy('dashboard:announcements')

class AnnouncementDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Announcement
    template_name = 'dashboard/announcement_confirm_delete.html'
    success_url = reverse_lazy('dashboard:announcements')

# Daily Reminders
class ReminderListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = DailyReminder
    template_name = 'dashboard/reminders.html'
    context_object_name = 'reminders'
    paginate_by = 10
    ordering = ['-date_for']

class ReminderCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = DailyReminder
    fields = ['date_for', 'content_type', 'title', 'arabic_text', 'translation', 'reference']
    template_name = 'dashboard/reminder_form.html'
    success_url = reverse_lazy('dashboard:reminders')

class ReminderUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = DailyReminder
    fields = ['date_for', 'content_type', 'title', 'arabic_text', 'translation', 'reference']
    template_name = 'dashboard/reminder_form.html'
    success_url = reverse_lazy('dashboard:reminders')

class ReminderDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = DailyReminder
    template_name = 'dashboard/reminder_confirm_delete.html'
    success_url = reverse_lazy('dashboard:reminders')
