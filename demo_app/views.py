from django.shortcuts import render
from django.views import View
from .models import DummyModel, User


# Create your views here.
class MigrationSuccessful(View):
    def get(self, request):
        user = User.objects.filter(username="test_user").first()

        if not user:
            user = User.objects.create_user(username="test_user", email="test_user@gmail.com", password="Test@12345")
            DummyModel.objects.create(user=user, description="Hello, I am first User")

        dummy_model = DummyModel.objects.filter(user=user).first()
        return render(request, 'demo_app/migration_successful.html', context={'user': user, 'dummy_model': dummy_model})
