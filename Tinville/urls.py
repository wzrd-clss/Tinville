from custom_oscar.apps.customer.views import AddressChangeStatusView
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.base import RedirectView, TemplateView
from oscar.core.loading import get_class
from user.decorators import designer_required
from user.views import ajax_login, register, DesignerPaymentInfoView
from user.forms import LoginForm
from designer_shop.views import ShopListView

from oscar.app import application
# from oscar.app import application

admin.autodiscover()

basket_app = get_class('basket.app', 'application')
checkout_app = get_class('checkout.app', 'application')
customer_app = get_class('customer.app', 'application')

urlpatterns = patterns('django.contrib.flatpages.views',
    url(r'^about/$', 'flatpage',  kwargs={'url': '/about/'}, name='home_about'),
    url(r'^faq/$', 'flatpage', kwargs={'url': '/faq/'}, name='home_faq'),
    url(r'^policies/$', 'flatpage', kwargs={'url': '/policies/'}, name='home_policies'),
    url(r'^terms/$', 'flatpage', kwargs={'url': '/terms/'}, name='home_terms'),
)

urlpatterns += patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^cartdetail', TemplateView.as_view(template_name='cartdetail.html'), name='cartdetail'),
    url(r'^register$', 'user.views.register'),
    url(r'^packageStatus$', 'custom_oscar.apps.dashboard.orders.views.packageStatus'),
    url(r'^activate/(?P<activation_key>\w+)$', 'user.views.activation', name='activate-user'),
    url(r'^ajax_login$', ajax_login,
        {'template_name': 'login_form.html', 'authentication_form': LoginForm},
        name='ajax_logins'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^feedback/', include('django_basic_feedback.urls')),
    url(r'^cart/', include(basket_app.urls)),
    url(r'^checkout/', include(checkout_app.urls)),
    url(r'^shoplist', ShopListView.as_view(template_name='shoplist.html'), name='shoplist'),
    url(r'^accounts/register', 'user.views.register', name='register'),
    url(r'^accounts/payment_info', designer_required(DesignerPaymentInfoView.as_view()), name='designer-payment-info'),
    url(r'^accounts/addresses/(?P<pk>\d+)/'
                r'(?P<action>default_for_(billing|shipping|shop))/$',
                login_required(AddressChangeStatusView.as_view()),
                name='address-change-status'),
    url(r'^accounts/', include(customer_app.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # Jon M TODO We should change these ajax URL's to a different scheme that doesnt conflict with edit item
    url(r'^delete_item_to_cart$', 'basket.views.delete_item_to_cart'),
    url(r'^load_cart$', 'basket.views.load_cart'),
    url(r'^dashboard/', include(get_class('dashboard.app', 'application').urls)),
    #IMPORTANT!!! This route need to always be last since it consumes the entire namespace!
    url(r'^(?P<shop_slug>[\w-]+)/edit/$', 'designer_shop.views.shopeditor'),
    # url(r'^(?P<shop_slug>[\w-]+)/edit/ajax_about$', 'designer_shop.views.ajax_about'),
    url(r'^(?P<shop_slug>[\w-]+)/edit/ajax_color$', 'designer_shop.views.ajax_color'),
    url(r'^(?P<shop_slug>[\w-]+)/edit/(?P<item_slug>[\w-]+)$', 'designer_shop.views.shopeditor_with_item'),
    url(r'^(?P<shop_slug>[\w-]+)/(?P<item_slug>[\w-]+)/$', 'designer_shop.views.itemdetail'),
    url(r'^(?P<shop_slug>[\w-]+)/(?P<item_slug>[\w-]+)/getVariants$', 'designer_shop.views.get_variants_httpresponse'),
    url(r'^(?P<shop_slug>[\w-]+)/(?P<item_slug>[\w-]+)/getVariants/(?P<group_by>[\w-]+)$', 'designer_shop.views.get_variants_httpresponse'),
    url(r'^(?P<shop_slug>[\w-]+)/edit/(?P<item_slug>[\w-]+)/getVariants/(?P<group_by>[\w-]+)$', 'designer_shop.views.get_variants_httpresponse'),
    url(r'^(?P<shop_slug>[\w-]+)/getTypes/(?P<group_by>[\w-]+)$', 'designer_shop.views.get_types'),
    url(r'^(?P<shop_slug>[\w-]+)/edit/getTypes/(?P<group_by>[\w-]+)$', 'designer_shop.views.get_types'),
    url(r'^(?P<shop_slug>[\w-]+)/edit/delete_product/(?P<item_slug>[\w-]+)$', 'designer_shop.views.delete_product'),
    url(r'^(?P<shop_slug>[\w-]+)/(?P<item_slug>[\w-]+)/add_item_to_cart$', 'basket.views.add_item_to_cart'),
    url(r'^update_cart_item$', 'basket.views.update_cart_item'),
    url(r'^cart_total$', 'basket.views.cart_total'),
    url(r'^total_cart_items$', 'basket.views.total_cart_items'),
    url(r'^delete_item_to_cart$', 'basket.views.delete_item_to_cart'),
    url(r'^load_cart$', 'basket.views.load_cart'),
    #IMPORTANT!!! This route need to always be last since it consumes the entire namespace!
    url(r'^(?P<slug>[\w-]+)/$', 'designer_shop.views.shopper')
)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns() + [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
