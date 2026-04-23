from django.contrib import admin
from attendance.models import User,Batch,Session,Attendance
# Register your models here.
admin.site.register(User)
admin.site.register(Batch)
admin.site.register(Session)
admin.site.register(Attendance)