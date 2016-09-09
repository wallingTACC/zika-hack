from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from .forms import SubmissionForm
from .models import Submission

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request)
    context['submissions'] = Submission.objects.all()
    
    return HttpResponse(template.render(context))

def submission_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubmissionForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
           
            label = form.cleaned_data['label']
            lat = form.cleaned_data['lat']
            long = form.cleaned_data['long']
            datetime = form.cleaned_data['datetime']
            submission_file = form.cleaned_data['submission_file']
            
            Submission.objects.create(label=label, datetime=datetime, lat=lat, lng=long, submission_file=submission_file)
            
            # redirect to a new URL:
            return redirect('index')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SubmissionForm()

    return render(request, 'submission.html', {'form': form})

def submission_details(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    return render(request, 'submission_details.html', {'submission': submission})