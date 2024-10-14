from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """Test API View"""    
    
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        apiview_features = [
            "somethings",
            "notherthings",
            "do not mather"
        ]
        
        return Response({"message": "Success", "data": apiview_features})