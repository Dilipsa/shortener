from .serializers import UrlSerializer, ShortUrlListSerializer
from url.models import UrlData
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,ListAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.status import HTTP_201_CREATED,HTTP_400_BAD_REQUEST
import random, string
from django.conf import settings

def get_short_code():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    # if the randomly generated short_id is used then generate next
    while True:
        short_id = ''.join(random.choice(char) for x in range(length))
        try:
            temp = UrlData.objects.get(slug=short_id)
        except:
            return short_id

class urlShortCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UrlSerializer(data=request.data)

        slug = get_short_code()
        url = request.data.get('url', None)

        if url.startswith("https://www."):
            initial = "https://www."
            url = url.replace("https://www.", "")
            print(url)

        elif url.startswith("https://"):
            initial = "https://www."
            url = url.replace("https://", "")
            print(url)
        
        elif url.startswith("http://www."):
            initial = "https://www."
            url = url.replace("http://www.", "")
            print(url)

        elif url.startswith("http://"):
            initial = "https://www."
            url = url.replace("http://", "")
            print(url)

        elif url.startswith("www."):
            initial = "www."
            url = url.replace("www.", "")
            print(url)

        len = url.find("/")
        domain = url[:len+1]

        data = UrlData.objects.all()
        url = initial+url
        d= UrlData.objects.filter(url=url)
        if d.exists():
            return Response({"message": "this url is already shotrened"}, status=HTTP_400_BAD_REQUEST)
            
        new_url = UrlData(url=url, slug=slug,domain=domain)
        new_url.save()
        obj = UrlData.objects.all()
        serializer = UrlSerializer(obj, many=True)
        return Response({"data":serializer.data}, status=HTTP_201_CREATED)
   
class AllUrl(APIView):
    def get(self, request, *args, **kwargs):
        obj = UrlData.objects.all()
        application_list = []
        new=[]
        for m in obj:
            obj = {}
            obj['domain'] = m.domain
            obj['slug'] = m.slug
            application_list.append(obj)
            
            new.append(obj['domain']+obj['slug'])

        return Response({"data":new})
        
class ShortenedUrlListView(APIView):
    def get(self, request, slug, *args, **kwargs):
        obj = UrlData.objects.all()
        try:
            l = [x for x in obj if x.slug==slug]
            short_url = l[0].domain+l[0].slug
            return Response(short_url)
        except:
            return Response({"error": "url does not exists"})
        
class UrlDeleteView(DestroyAPIView):
    serializer_class = ShortUrlListSerializer
    queryset = UrlData.objects.all()
    
class UrlDetailView(RetrieveAPIView):
    serializer_class = ShortUrlListSerializer
    queryset = UrlData.objects.all()

class RedirectView(APIView):
    def get(self, request, slug, *args, **kwargs):
        obj = UrlData.objects.get(slug=slug)
        serializer = UrlSerializer(obj)
        return Response({"data":serializer.data})