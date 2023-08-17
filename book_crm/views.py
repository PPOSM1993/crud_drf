from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(['GET'])
def index(request):
    
    return Response({"Example": "algo"})


#LIST DATA
@api_view(['GET'])
def CategoryList(request):
    query_set = Category.objects.all().order_by('id')
    serializer = CategorySerializer(query_set, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def LanguageList(request):
    query_set = Language.objects.all()
    serializer = LanguageSerializer(query_set, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def BindingList(request):
    query_set = Binding.objects.all()
    serializer = BindingSerializer(query_set, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def AuthorList(request):
    query_set = Author.objects.all()
    serializer = AuthorSerializer(query_set, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def FormatBookList(request):
    query_set = FormatBook.objects.all()
    serializer = FormatBookSerializer(query_set, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def GenderLiteraryList(request):
    query_set = GenderLiterary.objects.all()
    serializer = GenderLiterarySerializer(query_set, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def EditorialList(request):
    query_set = Editorial.objects.all()
    serializer = EditorialSerializer(query_set, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def BookList(request):
    query_set = Book.objects.all()
    serializer = BookSerializer(query_set, many=True)
    
    return Response(serializer.data)


#DETAILS DATA BY ID
@api_view(['GET'])
def CategoryDetail(request, pk):
    tasks = Category.objects.get(id=pk)
    serializer = CategorySerializer(tasks, many=False)
    
    return Response(serializer.data)

@api_view(['GET'])
def LanguageDetail(request, pk):
    tasks = Language.objects.get(id=pk)
    serializer = LanguageSerializer(tasks, many=False)
    
    return Response(serializer.data)

@api_view(['GET'])
def BindingDetail(request, pk):
    tasks = Binding.objects.get(id=pk)
    serializer = BindingSerializer(tasks, many=False)
    
    return Response(serializer.data)

@api_view(['GET'])
def AuthorDetail(request, pk):
    tasks = Author.objects.get(id=pk)
    serializer = AuthorSerializer(tasks, many=False)
    
    return Response(serializer.data)

@api_view(['GET'])
def BookDetail(request, pk):
    tasks = Book.objects.get(id=pk)
    serializer = BookSerializer(tasks, many=False)
    
    return Response(serializer.data)

@api_view(['GET'])
def EditorialDetail(request, pk):
    tasks = Editorial.objects.get(id=pk)
    serializer = EditorialSerializer(tasks, many=False)
    
    return Response(serializer.data)

@api_view(['GET'])
def GenderLiteraryDetail(request, pk):
    tasks = GenderLiterary.objects.get(id=pk)
    serializer = GenderLiterarySerializer(tasks, many=False)
    
    return Response(serializer.data)

@api_view(['GET'])
def FormatBookDetail(request, pk):
    tasks = FormatBook.objects.get(id=pk)
    serializer = FormatBookSerializer(tasks, many=False)
    
    return Response(serializer.data)


#CREATE DATA
@api_view(['GET', 'POST'])
def CreateCategory(request):
    data = request.data
    serializer = CategorySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success":"Category was created successfully."}, status=201)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def CreateLanguage(request):
    data = request.data
    serializer = LanguageSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success":"Category was created successfully."}, status=201)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def CreateBinding(request):
    data = request.data
    serializer = BindingSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success":"Category was created successfully."}, status=201)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def CreateAuthor(request):
    data = request.data
    serializer = Author(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success":"Category was created successfully."}, status=201)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def CreateGenderLiterary(request):
    data = request.data
    serializer = GenderLiterary(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success":"Category was created successfully."}, status=201)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def CreateFormatBook(request):
    data = request.data
    serializer = FormatBook(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success":"Category was created successfully."}, status=201)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def CreateEditorial(request):
    data = request.data
    serializer = Editorial(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success":"Category was created successfully."}, status=201)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def CreateBook(request):
    data = request.data
    serializer = BookSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success":"Category was created successfully."}, status=201)
    else:
        return Response(serializer.errors, status=400)


#UPDATE DATE BY ID
@api_view(['PUT'])
def UpdateCategory(request, pk):
    
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(instance=category, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def UpdateLanguage(request, pk):
    
    language = Category.objects.get(id=pk)
    serializer = CategorySerializer(instance=language, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def UpdateAuthor(request, pk):
    
    author = Author.objects.get(id=pk)
    serializer = AuthorSerializer(instance=author, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def UpdateBook(request, pk):
    
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=book, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def UpdateEditorial(request, pk):
    
    editorial = Editorial.objects.get(id=pk)
    serializer = EditorialSerializer(instance=editorial, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def UpdateBinding(request, pk):
    
    binding = Binding.objects.get(id=pk)
    serializer = BindingSerializer(instance=binding, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def UpdateGenderLiterary(request, pk):
    
    gender_literary = GenderLiterary.objects.get(id=pk)
    serializer = GenderLiterarySerializer(instance=gender_literary, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def UpdateFormatBook(request, pk):
    
    format_book = FormatBook.objects.get(id=pk)
    serializer = FormatBookSerializer(instance=format_book, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


#DELETE DATA BY ID
@api_view(['DELETE'])
def DeleteCategory(request, pk):
    try:
        category = Category.objects.get(id=pk)
        category.delete()
            
        return Response({"Success":"Category was deleted successfully."}, status=200)
    except Category.DoesNotExist:
        return Response({"Error": "The post does not exist"}, status=404)

@api_view(['DELETE'])
def DeleteLanguage(request, pk):
    try:
        language = Language.objects.get(id=pk)
        language.delete()
            
        return Response({"Success":"Language was deleted successfully."}, status=200)
    except Language.DoesNotExist:
        return Response({"Error": "Language does not exist"}, status=404)

@api_view(['DELETE'])
def DeleteBinding(request, pk):
    try:
        binding = Binding.objects.get(id=pk)
        binding.delete()
            
        return Response({"Success":"Language was deleted successfully."}, status=200)
    except Binding.DoesNotExist:
        return Response({"Error": "Language does not exist"}, status=404)

@api_view(['DELETE'])
def DeleteEditorial(request, pk):
    try:
        editorial = Editorial.objects.get(id=pk)
        editorial.delete()
            
        return Response({"Success":"Language was deleted successfully."}, status=200)
    except Editorial.DoesNotExist:
        return Response({"Error": "Language does not exist"}, status=404)

@api_view(['DELETE'])
def DeleteFormatBook(request, pk):
    try:
        format_book = FormatBook.objects.get(id=pk)
        format_book.delete()
            
        return Response({"Success":"Language was deleted successfully."}, status=200)
    except FormatBook.DoesNotExist:
        return Response({"Error": "Language does not exist"}, status=404)

@api_view(['DELETE'])
def DeleteAuthor(request, pk):
    try:
        author = Author.objects.get(id=pk)
        author.delete()
            
        return Response({"Success":"Language was deleted successfully."}, status=200)
    except Author.DoesNotExist:
        return Response({"Error": "Language does not exist"}, status=404)

@api_view(['DELETE'])
def DeleteGenderLiterary(request, pk):
    try:
        gender_literary = GenderLiterary.objects.get(id=pk)
        gender_literary.delete()
            
        return Response({"Success":"Language was deleted successfully."}, status=200)
    except GenderLiterary.DoesNotExist:
        return Response({"Error": "Language does not exist"}, status=404)

@api_view(['DELETE'])
def DeleteBook(request, pk):
    try:
        book = Book.objects.get(id=pk)
        book.delete()
            
        return Response({"Success":"Language was deleted successfully."}, status=200)
    except Book.DoesNotExist:
        return Response({"Error": "Language does not exist"}, status=404)