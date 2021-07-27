from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accounapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form): # 검증이 완료되면 할당 서버의 유저
        form.instance.user = self.request.user
        return super().form_valid(form)