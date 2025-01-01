from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import SampleModel
from .serializers import SampleSerializer
from django.urls import path
from rest_framework.views import APIView
from rest_framework.response import Response

# View
class SampleModelAPIView(APIView):
    def get(self, request):
        samples = SampleModel.objects.all()
        serializer = SampleSerializer(samples, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SampleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# URL Configuration for Testing
urlpatterns = [
    path('api/samples/', SampleModelAPIView.as_view(), name='sample-list'),
]

# Test Case
class SampleModelAPITestCase(APITestCase):
    def setUp(self):
        # Create test data
        self.sample1 = SampleModel.objects.create(
            name="Sample 1", description="Description for Sample 1"
        )
        self.sample2 = SampleModel.objects.create(
            name="Sample 2", description="Description for Sample 2"
        )
        self.sample_list_url = '/api/samples/'  # Direct URL path

    def test_get_samples(self):
        response = self.client.get(self.sample_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'Sample 1')

    def test_create_sample(self):
        data = {
            "name": "Sample 3",
            "description": "Description for Sample 3"
        }
        response = self.client.post(self.sample_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SampleModel.objects.count(), 3)
        self.assertEqual(SampleModel.objects.last().name, "Sample 3")
