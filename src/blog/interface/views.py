from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from ..application.usecases import PostService
from ..infrastructure.repositories_django import DjangoPostRepository

class ListCreatePostAPIView(APIView):

    serializer_class = PostSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = PostService(repo=DjangoPostRepository())

    def get(self, request, *args, **kwargs):
        try:
            query = self.service.get_posts()
            serializer = self.serializer_class(query, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request, *args, **kwrgs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.service.create(
                title=serializer.validated_data["title"],
                descriptoin=serializer.validated_data["description"]
            )
            
            return Response({"detail":"Post created."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)})

class UpdateDeleteRetrievePostAPIView(APIView):

    serializer_class = PostSerializer
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = PostService(repo=DjangoPostRepository())

    def get(self, request, *args, **kwargs):
        try:
            query = self.service.get_post(post_id=kwargs.get("id"))
            serializer = self.serializer_class(query)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.service.update(
                post_id=kwargs.get("id"),
                title=serializer.validated_data["title"],
                description=serializer.validated_data["description"]
            )

            return Response({"detail":"Post updated."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request, *args, **kwargs):
        try:
            self.service.delete(kwargs.get("id"))

            return Response({"detail":"Post deleted."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)})
