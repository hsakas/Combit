from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from .forms import JobUploadForm
from .models import Category, Job

@login_required
def upload_job(request):

    if request.method == 'POST':

        form = JobUploadForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.status = 'open'
            job.user = request.user
            job.save()
            message = "Job posted successfully!!"
            return HttpResponseRedirect('/', {'message': message})
        else:
            message = "Unable to upload job! Retry"
            return HttpResponseRedirect('/', {'message': message})
    else:
        form = JobUploadForm()
        return render(request, 'job/upload.html', {'form': form})


def jobs_by_category():

    category = Category.objects().get(slug=slug)
    jobs = Job.objects.filter(category=category)
    return render(request, 'job/by_category.html', {'jobs': jobs})