import uuid
from django.db import models


class UserReport(models.Model):
    key_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    log = models.TextField(default='')
    input_file = models.FileField(upload_to='input')
    output_file = models.FileField(upload_to='output', blank=True, null=True)

