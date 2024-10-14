from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import HelloSerializer


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