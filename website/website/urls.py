from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^blog/',include('blogg.urls')),
    url(r'^test/',include('testapp.urls'))
] 