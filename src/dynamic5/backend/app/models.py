from django.contrib.postgres.fields import ArrayField
from django.db.models import CharField, Model, DateTimeField, IntegerField, ManyToManyField, ForeignKey, \
    FloatField, TextField, SET_NULL

class Person(Model):
    id = CharField(primary_key=True, max_length=255)
    name = CharField(max_length=255, blank=True, null=True)
    image = CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return '%s object <%s>' % (self.__class__.__name__, self.name)

class Book(Model):
    id = CharField(primary_key=True, max_length=255, )
    name = CharField(max_length=255, blank=True, null=True)
    authors = ManyToManyField(Person)
    publisher = CharField(max_length=255, blank=True, null=True)
    tags = ArrayField(CharField(max_length=255, null=True, blank=True), null=True, blank=True)
    url = CharField(max_length=255, blank=True, null=True)
    isbn = CharField(max_length=255, blank=True, null=True)
    cover = CharField(max_length=255, blank=True, null=True)
    page_number = IntegerField(blank=True, null=True)
    price = FloatField(blank=True, null=True)
    score = FloatField(blank=True, null=True)
    introduction = TextField(blank=True, null=True)
    catalog = TextField(blank=True, null=True)
    published_at = DateTimeField(blank=True, null=True)
    updated_at = DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return '%s object <%s>' % (self.__class__.__name__, self.name)
    
    class Meta:
        app_label = 'app'

class Comment(Model):
    id = CharField(primary_key=True, max_length=255)
    content = CharField(max_length=255, blank=True, null=True)
    book = ForeignKey(Book, null=True, blank=True, on_delete=SET_NULL)
    
    def __str__(self):
        return '%s object <%s>' % (self.__class__.__name__, self.pk)
