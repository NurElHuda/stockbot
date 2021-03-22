from rest_condition import And, Or
from rest_framework import exceptions, generics, permissions
from rest_framework.parsers import FileUploadParser, MultiPartParser

from app_src.api.models import Agent, Product, Manager
from app_src.api.permissions import IsAdminUser, IsAgentUser, IsManagerUser
from app_src.api.serializers import (
    AgentSerializer,
    ProductSerializer,
    ManagerSerializer,
)


class ProductList(generics.ListCreateAPIView):

    permission_classes = (
        And(permissions.IsAuthenticated, Or(IsManagerUser, IsAdminUser)),
    )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        And(permissions.IsAuthenticated, Or(IsManagerUser, IsAdminUser)),
    )
    queryset = Product.objects.all()
    lookup_url_kwarg = "product_id"

    def get_object(self):
        try:
            obj = Product.objects.get(pk=self.kwargs["product_id"])
        except Product.DoesNotExist:
            raise exceptions.NotFound(detail="Product not found")
        return obj

    serializer_class = ProductSerializer


# class ProductLogo(generics.RetrieveUpdateAPIView):
#     permission_classes = (Or(Or(IsAgentUser, IsManagerUser), IsAdminUser),)
#     lookup_url_kwarg = "product_id"

#     def get_object(self):
#         try:
#             product = Product.objects.get(pk=self.kwargs["product_id"])
#         except Product.DoesNotExist:
#             raise exceptions.NotFound(detail="Product not found")
#         return product

#     serializer_class = ProductLogoSerializer
#     parser_classes = [MultiPartParser, FileUploadParser]


# class ProductManagerList(generics.ListAPIView):

#     permission_classes = (
#         And(permissions.IsAuthenticated, Or(IsManagerUser, IsAdminUser)),
#     )
#     lookup_url_kwarg = "product_id"

#     def get_queryset(self):
#         return Manager.objects.filter(product__pk=self.kwargs["product_id"])

#     serializer_class = ManagerSerializer


# class ProductAgentList(generics.ListAPIView):

#     permission_classes = (
#         And(permissions.IsAuthenticated, Or(IsManagerUser, IsAdminUser)),
#     )
#     lookup_url_kwarg = "product_id"

#     def get_queryset(self):
#         return Agent.objects.filter(product__pk=self.kwargs["product_id"])

#     serializer_class = AgentSerializer


# class ProductTeacherList(generics.ListAPIView):

#     permission_classes = (
#         And(permissions.IsAuthenticated, Or(IsManagerUser, IsAdminUser)),
#     )
#     lookup_url_kwarg = "product_id"

#     def get_queryset(self):
#         return Teacher.objects.filter(product__pk=self.kwargs["product_id"])

#     serializer_class = TeacherSerializer


# class ProductStudentList(generics.ListAPIView):

#     permission_classes = (
#         And(permissions.IsAuthenticated, Or(IsManagerUser, IsAdminUser)),
#     )
#     lookup_url_kwarg = "product_id"

#     def get_queryset(self):
#         return Student.objects.filter(product__pk=self.kwargs["product_id"])

#     serializer_class = StudentSerializer


# class ProductSessionList(generics.ListAPIView):

#     permission_classes = (
#         And(permissions.IsAuthenticated, Or(IsManagerUser, IsAdminUser)),
#     )
#     lookup_url_kwarg = "product_id"

#     def get_queryset(self):
#         return Session.objects.filter(product__pk=self.kwargs["product_id"])

#     serializer_class = SessionSerializer


# class ProductCourseList(generics.ListAPIView):

#     permission_classes = (
#         And(permissions.IsAuthenticated, Or(IsManagerUser, IsAdminUser)),
#     )
#     lookup_url_kwarg = "product_id"

#     def get_queryset(self):
#         return Course.objects.filter(product__pk=self.kwargs["product_id"])

#     serializer_class = CourseSerializer
