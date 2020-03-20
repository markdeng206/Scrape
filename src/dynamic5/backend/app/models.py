from django.db.models import CharField, Model, DateTimeField, IntegerField, ManyToManyField, ForeignKey, \
    FloatField, TextField, SET_NULL

class Person(Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=255)
    image = CharField(max_length=255)

class Publisher(Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=255)

class Tag(Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=255)

class Book(Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=255)
    authors = ManyToManyField(Person)
    publisher = ForeignKey(Publisher, null=True, blank=True, on_delete=SET_NULL)
    tags = ManyToManyField(Tag)
    url = CharField(max_length=255, unique=True)
    isbn = CharField(max_length=255, unique=True)
    cover = CharField(max_length=255, blank=True, null=True)
    page_number = IntegerField(blank=True, null=True)
    price = FloatField(blank=True, null=True)
    score = FloatField(blank=True, null=True)
    introduction = TextField(blank=True, null=True)
    catalog = TextField(blank=True, null=True)
    published_at = DateTimeField(blank=True, null=True)
    updated_at = DateTimeField(auto_now=True, blank=True, null=True)
    
    class Meta:
        app_label = 'app'

class Comment(Model):
    id = IntegerField(primary_key=True)
    content = CharField(max_length=255)
    book = ForeignKey(Book, null=True, blank=True, on_delete=SET_NULL)
