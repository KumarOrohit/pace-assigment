from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .utils import mandatory_param_check, basic_response_dict
from rest_framework.response import Response
from rest_framework import status
from.models import WebScrapData
from .serializers import WebScrapDataSerializer


class WebScrapView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    response = {
        "message": '',
        "error": '',
        "data": []
    }

    def post(self, request):
        scrap = request.data

        for data in scrap:
            name = data.get('name')
            price = data.get('price')
            h1 = data.get('h1')
            h24 = data.get('h24')
            d7 = data.get('d7')
            market_cap = data.get('market_cap')
            volume_24h = data.get('volume_24h')
            circulating_supply = data.get('circulating_supply')

            if not data:
                response = basic_response_dict("Please send the mandatory params", "Invalid params.", None)

                return Response(response, status=status.HTTP_400_BAD_REQUEST)

            check = mandatory_param_check(data)

            if check:
                response = basic_response_dict("Please send the mandatory params", "Invalid params.", None)

                return Response(response, status=status.HTTP_400_BAD_REQUEST)

            obj, created = WebScrapData.objects.update_or_create(
                name=name,
                defaults={'price': price,
                          'h1': h1,
                          'h24': h24,
                          'd7': d7,
                          'market_cap': market_cap,
                          'volume_24h': volume_24h,
                          'circulating_supply': circulating_supply},
            )

        response = basic_response_dict("Scrap data updated.", None, None)
        return Response(response, status=status.HTTP_200_OK)

    def get(self, request):
        scrap_data_list = WebScrapData.objects.all()

        if not scrap_data_list:
            response = basic_response_dict("No scrap data available.", None, None)

            return Response(response, status=status.HTTP_200_OK)
        serializer = WebScrapDataSerializer(scrap_data_list, many=True)
        response = basic_response_dict("Scrap data list.", None, serializer.data)
        return Response(response, status=status.HTTP_200_OK)


