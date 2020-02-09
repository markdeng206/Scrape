from django.db.models import CharField, Model, DateTimeField, AutoField


class News(Model):
    id = AutoField(primary_key=True)
    title = CharField(max_length=255)
    code = CharField(max_length=255, blank=True, null=True)
    url = CharField(max_length=255, unique=True)
    source = CharField(max_length=255, blank=True, null=True)
    domain = CharField(max_length=255, blank=True, null=True)
    website = CharField(max_length=255, blank=True, null=True)
    thumb = CharField(max_length=255, blank=True, null=True)
    published_at = DateTimeField(null=True, blank=True)
    updated_at = DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        app_label = 'app'
