from django.contrib import admin
from django.urls import path, include
from django.urls.converters import PathConverter
from frontend.views import IndexView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from myapp import views


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'Client', views.ClientViewSet)
router.register(r'Doctor', views.DoctorViewSet)
router.register(r'Vendor', views.VendorViewSet)
router.register(r'Provider', views.ProviderViewSet)
router.register(r'Service', views.ServiceViewSet)
router.register(r'Mascot', views.MascotViewSet)
router.register(r'Product', views.ProductViewSet)
router.register(r'Office', views.OfficeViewSet)
router.register(r'Cite', views.CiteViewSet)
router.register(r'Sale', views.SaleViewSet)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

