from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework import status, filters

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import HelloSerializer, UserProfileSerializer
from .models import UserProfile
from .permissions import UpdateOwnProfile


class HelloApiView(APIView):
    """Test API View"""    
    serializer_class = HelloSerializer
    
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        apiview_features = [
            "somethings",
            "notherthings",
            "do not mather"
        ]
        
        return Response({"message": "Success", "data": apiview_features})
    
    def post(self, request):
        """Create a hello message with the name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response(
                {
                    "status": "Success", 
                    "message": message
                }
            )
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def patch(self, request, pk=None):
        """Handle entire object update"""
        return Response({'message': 'PATCH'})
    
    def put(self, request, pk=None):
        """Handle parcial update of an object"""
        return Response({'message': 'PUT'})
    
    def delete(self, request, pk=None):
        """Handle object delete"""
        return Response({'message': 'DELETE'})
    

class HelloViewSet(ViewSet):
    """Hello view set"""
    serializer_class = HelloSerializer
    
    def list(self, request):
        """Returns the view set list"""
        
        return Response({
            "status": "success",
            "data": {
                "message": "This is a ViewSet list"
            }
        })
    
    def create(self, request):
        """Create a new Hello message"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}!"
            return Response(
                {
                    "status": "success", 
                    "data": {
                        "message": message
                    }
                }
            )
        else:
            return Response(
            {
                "status": "error",
                "error": serializer.errors, 
            }, status=status.HTTP_400_BAD_REQUEST)
            
    def retrieve(self, request, pk=None):
        """Handle getting a single object by PK"""
        return Response({"http_method": "GET"})
    
    def update(self, request, pk=None):
        """Handle updating entire object"""
        return Response({"http_method": "PUT"})
    
    def partial_update(self, request, pk=None):
        """Handle updating a part of the object"""
        return Response({"http_method": "PATCH"})
    
    def destroy(self, request, pk=None):
        """Handle destroying the object"""
        return Response({"http_method": "DELETE"})
    

class UserProfileViewSet(ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name", "email",)
    
    
class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES