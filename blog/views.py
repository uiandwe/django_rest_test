from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView

from blog.models import Post


def blog_page(request):
    post_list = Post.objects.all()
    return HttpResponse("hello!!"+ post_list[0].title)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post


class blog_api(GenericAPIView, mixins.ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer


@api_view()
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Bookings API')
    return response.Response(generator.get_schema(request=request))
