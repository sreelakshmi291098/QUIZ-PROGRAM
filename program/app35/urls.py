from django.urls import path
from app35 import views

urlpatterns=[
    path("student_register",views.StudentRegisterAPIView.as_view(),name="student_register"),
    path("question_register",views.QuestionRegisterAPIView.as_view(),name="question_register"),
    path("login",views.LoginApiView.as_view(),name="login"),
    path("studentview",views.GetStudentApiView.as_view(),name="studentview"),
    path("questionview",views.GetQuestionApiView.as_view(),name="questionview"),
    path("singleview/<int:id>/",views.SingleStudentApiView.as_view(),name="singleview"),
    path("singlequestionview/<int:id>/",views.SingleQuestionApiView.as_view(),name="singlequestionview"),
    path("deletestudent/<int:id>/",views.DeleteStudentApiView.as_view(),name="deletestudent"),
    path("deletequestion/<int:id>/",views.DeleteQuestionApiView.as_view(),name="deletequestion"),
    path("updatestudent/<int:id>/",views.UpdateStudentApiView.as_view(),name="updatestudent"),
    path("updatequestion/<int:id>/",views.UpdateQuestionAptView.as_view(),name="updatequestion"),
    
]