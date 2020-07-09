from django.conf.urls import url
from testapp.views import Home
from .views import BlogData
from .views import bloggTest
from .views import Contact,Product,Hello,AboutUs,HelloTemplate,ProductStatic,ProductDynamicOneRecord,Products,BlogData,bloggTest

urlpatterns = [

	 	url(r'^contact/',Contact),
    	url(r'^product/',Product),
    	url(r'^hello/',Hello),
    	url(r'^about/',AboutUs),
    	url(r'home/',Home),
    	url(r'^hellotemplate/',HelloTemplate),
    	url(r'^productstatic/',ProductStatic),
    	url(r'^productdynamic/',ProductDynamicOneRecord),
    	url(r'^products/',Products),
    	url(r'^blogdata/',BlogData),
        url(r'^bloggtest/',bloggTest),




]
