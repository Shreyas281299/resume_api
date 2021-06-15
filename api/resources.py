from .models import Resume
from import_export import resources,fields
from .doc_exc import get_info


class ResumeResources(resources.ModelResource):
    Phone = fields.Field()
    Email = fields.Field()

    def dehydrate_Phone(self, obj):
        return get_info(obj.resume)[1]

    def dehydrate_Email(self, obj):
        return get_info(obj.resume)[0]

    class Meta:
        model = Resume
        export_order = ('id','Name','resume', 'Phone', 'Email')