from django.shortcuts import render_to_response
from django.template import RequestContext

def enter(request):
    return render_to_response('wedding/enter.html',{},context_instance=RequestContext(request))

def about_us(request):
    return render_to_response('wedding/about-us.html',{},context_instance=RequestContext(request))

def ceremony(request):
    return render_to_response('wedding/ceremony.html',{},context_instance=RequestContext(request))

def guest_book(request):
    return render_to_response('wedding/guest-book.html',{},context_instance=RequestContext(request))

def guest_info(request):
    return render_to_response('wedding/guest-info.html',{},context_instance=RequestContext(request))

def honeymoon(request):
    return render_to_response('wedding/honeymoon.html',{},context_instance=RequestContext(request))

def our_proposal(request):
    return render_to_response('wedding/our-proposal.html',{},context_instance=RequestContext(request))

def our_registries(request):
    return render_to_response('wedding/our-registries.html',{},context_instance=RequestContext(request))

def photo_album(request):
    return render_to_response('wedding/photo-album.html',{},context_instance=RequestContext(request))

def wedding_party(request):
    return render_to_response('wedding/wedding-party.html',{},context_instance=RequestContext(request))
