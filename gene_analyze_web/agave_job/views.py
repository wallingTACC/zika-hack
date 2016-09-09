from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from .forms import SubmissionForm
from .models import Submission

# Create your views here.

def index(request):
    template = loader.get_template('agave_job/index.html')
    context = RequestContext(request)
    context['submissions'] = Submission.objects.all()
    
    return HttpResponse(template.render(context))

def submission_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubmissionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
           
            label = form.cleaned_data['label']
            Submission.objects.create(label=label)
            
            # redirect to a new URL:
            return redirect('index')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SubmissionForm()

    return render(request, 'agave_job/submission.html', {'form': form})