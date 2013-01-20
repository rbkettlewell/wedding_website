from django.conf.urls import patterns, include, url
from emilyandblayne.views import enter, about_us, ceremony, guest_book, guest_info, honeymoon,\
    our_proposal, our_registries, photo_album, wedding_party
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'emilyandblayne.views.home', name='home'),
    # url(r'^emilyandblayne/', include('emilyandblayne.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$',  'emilyandblayne.views.enter'),
    url(r'^about-us/',  'emilyandblayne.views.about_us'),
    url(r'^ceremony/',  'emilyandblayne.views.ceremony'),
    url(r'^guest-book/',  'emilyandblayne.views.guest_book'),
    url(r'^guest-info/',  'emilyandblayne.views.guest_info'),
    url(r'^honeymoon/',  'emilyandblayne.views.honeymoon'),
    url(r'^our-proposal/',  'emilyandblayne.views.our_proposal'),
    url(r'^our-registries/',  'emilyandblayne.views.our_registries'),
    url(r'^photo-album/',  'emilyandblayne.views.photo_album'),
    url(r'^wedding-party/',  'emilyandblayne.views.wedding_party')
 )
