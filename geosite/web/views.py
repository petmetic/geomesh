from django.shortcuts import render, get_object_or_404
from django.utils import timezone
# from .models import Report
from django.shortcuts import redirect

from .forms import ReportForm


def index(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            pass
            # core app logic send data to txtcoordinates
        return redirect("report < ID >")
    else:
        form = ReportForm()
    return render(request, 'web/index.html', {"form": form})


def report(request, uuid):
    report_object = get_object_or_404(Report, uuid=uuid)
    return render(request, 'web/report.html', {'report': report_object})


def download(request, uuid):
    report = get_object_or_404(Report, uuid=uuid)
    return render(report.output_file, {'download': download})
