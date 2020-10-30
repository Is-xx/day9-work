from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Book
from app.serializers import BookModelSerializer


class BookAPIView(APIView):
    def get(self, requset, *args, **kwargs):
        book_id = kwargs.get('id')
        if book_id:
            book = Book.objects.get(pk=book_id, is_delete=False)
            data = BookModelSerializer(book).data
            return Response({
                'status': 200,
                'message': '查询单个图书成功',
                'result': data,
            })
        else:
            book_object_all = Book.objects.filter(is_delete=False)
            book_ser = BookModelSerializer(book_object_all, many=True).data
            return Response({
                'status': 200,
                'message': '查询所有图书成功',
                'result': book_ser,
            })

    def post(self, request, *args, **kwargs):
        request_data = request.data
        if isinstance(request_data, dict):
            flag = False
        elif isinstance(request_data, list):
            flag = True
        else:
            return Response({
                "status": 400,
                "message": "参数格式有误",
            })
        serializer = BookModelSerializer(data=request_data, many=flag)
        serializer.is_valid(raise_exception=True)
        book_obj = serializer.save()
        return Response({
            "status": 200,
            "message": "添加图书成功",
            "results": BookModelSerializer(book_obj, many=flag).data,
        })

    def delete(self, request, *args, **kwargs):
        book_id = kwargs.get('id')
        if book_id:
            ids = [book_id]
        else:
            ids = request.data.get('ids')
        response = Book.objects.filter(pk__in=ids, is_delete=False).update(is_delete=True)
        if response:
            return Response({
                "status": 200,
                "message": '删除成功'
            })
        return Response({
            "status": 400,
            "message": '删除失败或者图书存在'
        })

    def put(self, request, *args, **kwargs):
        request_data = request.data
        book_id = kwargs.get('id')
        try:
            book_obj = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({
                "status": 400,
                "message": '图书不存在'
            })
        serializer = BookModelSerializer(data=request_data, instance=book_obj)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "status": 200,
            "message": '修改成功',
            "results": BookModelSerializer(book_obj).data
        })

    def patch(self, request, *args, **kwargs):
        request_data = request.data
        book_id = kwargs.get('id')
        try:
            book_obj = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({
                "status": 400,
                "message": '图书不存在'
            })
        serializer = BookModelSerializer(data=request_data, instance=book_obj, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "status": 200,
            "message": '修改成功',
            "results": BookModelSerializer(book_obj).data
        })
