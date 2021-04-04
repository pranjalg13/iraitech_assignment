from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.
# index function
def home(request):
    return render(request,'index.html')

# Question1
def iterative(x,n):
    ans = 0
    for i in range(n):
        ans = ans + (1/(x**i))
    return ans
# Api
class SeriesAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data = request.data
        x = request.data['x']
        n = request.data['n']
        ans = iterative(x,n)
        return Response({'data': ans}, status=status)
