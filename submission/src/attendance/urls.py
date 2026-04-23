from django.urls import path
from attendance.views import signup,login,create_batch, create_session, mark_attendance,get_attendance
urlpatterns=[
				path('signup/',signup),
				path('login/',login),
				path('batches/', create_batch),
    			path('sessions/', create_session),
    			path('attendance/mark/', mark_attendance),
    			path('sessions/<int:session_id>/attendance/', get_attendance),
			]