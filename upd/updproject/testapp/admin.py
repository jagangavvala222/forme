from django.contrib import admin
from testapp.models import PythonDocument
from testapp.models import DjangoDocument
from testapp.models import MachinelearningDocument
from testapp.models import ResumeDocument

# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    list_display=['id','description','document','uploaded_at']
admin.site.register(PythonDocument,DocumentAdmin)

class DocumentAdmin1(admin.ModelAdmin):
    list_display=['id','description','document','uploaded_at']
admin.site.register(DjangoDocument,DocumentAdmin1)
class DocumentAdmin2(admin.ModelAdmin):
    list_display=['id','description','document','uploaded_at']
admin.site.register(MachinelearningDocument,DocumentAdmin2)

class ResumeDocumentAdmin(admin.ModelAdmin):
    list_display=['document',]
admin.site.register(ResumeDocument,ResumeDocumentAdmin)
