from django.core.files import File
from django.http import HttpResponse, FileResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import ReportForm
from django.urls import reverse
from .models import UserReport
from .utils import txt2coordinates


def index(request):
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            userreport = form.save()
            output_file, log = txt2coordinates(userreport.input_file.path)
            userreport.output_file = File(output_file, name="output.txt")
            userreport.log = '\n'.join(log)
            userreport.save()
            output_file.close()

            return redirect(reverse('report', kwargs={'uuid': userreport.key_uuid}))
    else:
        form = ReportForm()
    return render(request, 'web/index.html', {"form": form})


def report(request, uuid):
    report_object = get_object_or_404(UserReport, key_uuid=uuid)
    return render(request, 'web/report.html', {'report': report_object})


def download(request, uuid):
    userreport = get_object_or_404(UserReport, key_uuid=uuid)
    return FileResponse(open(userreport.output_file.path, 'rb'), as_attachment=True, filename="converted-points.txt")
