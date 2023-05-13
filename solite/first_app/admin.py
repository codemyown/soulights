from django.contrib import admin
from .models.contact import Contact
from .models.blog import Blog
from .models.course import Course
from .models.review import Review
from .models.contact_us import ContactUs
from .models.plain import Plain

# Register your models here.


admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Course)
admin.site.register(Review)
admin.site.register(ContactUs)
admin.site.register(Plain)
