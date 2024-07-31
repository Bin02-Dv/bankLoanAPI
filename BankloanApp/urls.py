from django.urls import path
from .views import AddApprovals, ApprovalView

urlpatterns = [
    path('send', AddApprovals.as_view()),
    path('view', ApprovalView.as_view())
]
