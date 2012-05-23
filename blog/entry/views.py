from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from entry.models import Post
from entry.forms import PostForm

def test_view(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			if request.user.is_authenticated():
				username = request.user
			else:
				username = 'Gast'
			new_post = Post(title = form.cleaned_data['title'],
			content = form.cleaned_data['content'])
			new_post.save()
			return render_to_response('entry/test.html', {'form': form, 				'username':username})
		else:
			return render_to_response('entry/test.html', {'form': form})
	else:
		form = PostForm()
	return render_to_response('entry/test.html', {'form': form,}) 

'''def test_view(request):
    template_data = {'new_post': None, 'user': None, 'error_title': None, 'error_content': None, 'place': None }
    if request.method == 'GET':
        render_to_response('entry/test.html')
    elif request.method == 'POST':
	if request.POST['title'] == '':
		template_data['error_title'] = ("Bitte Titel eingeben!")
		if request.POST['content'] == '':
			template_data['error_content'] = ("Bitte Inhalt eingeben!")
		elif len(request.POST['content']) < 5:
			template_data['error_content'] = ("Bitte mindestens 5 Zeichen im Inhalt eingeben!")
			place = Post(content = request.POST['content'])
			template_data['place'] = place
		else:
			place = Post(content = request.POST['content'])
			template_data['place'] = place
	elif request.POST['content'] == '':
		template_data['error_content'] = ("Bitte Inhalt eingeben!")
		place = Post(title = request.POST['title'])
		template_data['place'] = place
	elif len(request.POST['content']) < 5:
		template_data['error_content'] = ("Bitte mindestens 5 Zeichen im Inhalt eingeben!")
		place = Post(title = request.POST['title'], content = request.POST['content'])
		template_data['place'] = place
	else:
		if request.user.is_authenticated():
		    new_post = Post(title = request.POST['title'], content = request.POST['content'], user = request.user)
		    new_post.save()
		    template_data['new_post'] = new_post
		    template_data['user'] = request.user
		else:
		    new_post = Post(title = request.POST['title'], content = request.POST['content'], user = None)
		    new_post.save()
		    template_data['new_post'] = new_post
    return render_to_response('entry/test.html', template_data)'''


'''def detail(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    return render_to_response('entry/detail.html', {'post': p})'''

'''def new(request):
    if request.method == 'GET':
        render_to_response('entry/new.html')
    elif request.method == 'POST':
        new_post = Post(title = request.POST["title"], content = request.POST["content"], user = request.user)
        new_post.save()
    return render_to_response('entry/new.html')'''
