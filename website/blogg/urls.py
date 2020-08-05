from django.conf.urls import url
from testapp.views import Home
from .views import BlogData
from .views import bloggTest
from .views import Contact,Product,Hello,AboutUs,HelloTemplate,ProductStatic,ProductDynamicOneRecord,Products,BlogData,bloggTest,Contact,Thanks,StudentInsert,BlogPost,Home,AboutUs

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
        url(r'^contact12345/',Contact,name='contact'),
        url(r'^thanks/',Thanks,name='thankyou'),
        url(r'^studentinsert/',StudentInsert),
        url(r'^blogpostabc/',BlogPost,name='postblog'),
        url(r'^$',Home,name='home'),
        url(r'^aboutus/',AboutUs,name='aboutus'),
        


]
