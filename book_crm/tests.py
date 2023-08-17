from django.test import TestCase
import request 


request = request.get('http://127.0.0.1:8000')

print(request.json())