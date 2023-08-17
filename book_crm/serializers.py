from .models import *
from rest_framework.serializers import ModelSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class LanguageSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
        
class BindingSerializer(ModelSerializer):
    class Meta:
        model = Binding
        fields = '__all__'

class FormatBookSerializer(ModelSerializer):
    class Meta:
        model = FormatBook
        fields = '__all__'

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class EditorialSerializer(ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'

class GenderLiterarySerializer(ModelSerializer):
    class Meta:
        model = GenderLiterary
        fields = '__all__'

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'