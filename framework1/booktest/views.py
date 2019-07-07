from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
# /books/
from booktest.models import BookInfo
from booktest.serializers import BookinfoSerializer
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet

class BookInfoViewSet(ModelViewSet):
    #指明 视图要使用序列化器
    serializer_class = BookinfoSerializer
    # 指明视图使用的查询集
    queryset = BookInfo.objects.all()
    def latest(self,request):
        book = BookInfo.objects.latest('id')
        serializer = self.get_serializer(book)
        return Response(serializer.data)
    def read(self,request,pk):
        book=self.get_object()
        book.read=request.data.get('read')
        book.save()
        serializer = self.get_serializer()
        return Response(serializer.data)

    # def  get(self,request):
    #     # queryset=self.get_queryset()
    #     # # serializer = BookinfoSerializer(queryset, many=True)
    #     # serializer=self.get_serializer(queryset,many=True)
    #     return self.list(request)
    # def post(self,request):
    #     """
    #     新增一个图书数据
    #     :param request: request.data
    #     :return: serializer.data
    #     """
    #     #反序列化 -数据校验
    #     # serializer=BookinfoSerializer(data=request.data)
    #     # serializer = self.get_serializer(data=request.data)
    #     # serializer.is_valid(raise_exception=True)
    #     # serializer.save()
    #     return self.create(request)
# /books/(?P<pk>\d+)/
class BookDetailView(RetrieveUpdateDestroyAPIView,GenericAPIView):
    """
    获取修改 删除指定图书
    """
    serializer_class = BookinfoSerializer
    queryset = BookInfo.objects.all()

    # def get(self,request,pk):
    #     """
    #     获取制定图书
    #     :param request:
    #     :param pk:
    #     :return:
    #     """
    #     # try:
    #     #     book=BookInfo.objects.get(pk=pk)
    #     # except BookInfo.DoesNotExist:
    #     #     raise Http404
    #     # instance = self.get_object()
    #     # serializer = BookinfoSerializer(instance)
    #     return self.retrieve(request)
    # def put(self,request,pk):
    #     # try:
    #     #     book=BookInfo.objects.get(pk=pk)
    #     # except BookInfo.DoesNotExist:
    #     #     raise Http404
    #     # instance=self.get_object()
    #     # serializer = BookinfoSerializer(instance, request.data)
    #     # serializer.is_valid(raise_exception=True)
    #     # # 反序列化  数据保存save内部会调用序列化 器类的update方法
    #     # serializer.save()
    #     return self.update(request)
    # def delete(self,request,pk):
    #     """删除指定图书"""
    #     # try:
    #     #     book=BookInfo.objects.get(pk=pk)
    #     # except BookInfo.DoesNotExist:
    #     #     raise Http404
    #     # book.delete()
    #     return self.destroy(request)









