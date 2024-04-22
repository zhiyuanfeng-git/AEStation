from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from .forms import FansForm
from django.utils import timezone
from datetime import timedelta
import csv
from io import TextIOWrapper
from django.http import HttpResponse
from .utils import Time_format

# Create your views here.
MAX_FILE_SIZE = 5 * 1024 * 1024

class FansView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/fans.html'
    form_class = FansForm

    def _get_fans_count(self, user):
        fans_count = user.owners_fans.all().count()
        return fans_count
    
    def _get_last_fans_count(self, user, days):
        if not days or days < 1:
            return 0
        last_time = timezone.now() - timedelta(days=days)
        last_count = user.owners_fans.filter(date_joined__gte=last_time).count()
        return last_count

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['fans_count'] = self._get_fans_count(user)
        context['last_week_fans_count'] = self._get_last_fans_count(user, 7)
        return context
    
class FansUploadView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/fans_upload.html'

    @staticmethod
    def _check_csv_file(csv_file):
        ret = 0
        msg = None
        if not csv_file.name.endswith('.csv'):
            ret = -1
            msg = "Invalid file format. Please upload a CSV file."
        elif csv_file.size <= 0:
            ret = -2
            msg = f'The file {csv_file.name} is an empty file.'
        elif csv_file.size > MAX_FILE_SIZE:
            ret = -3
            msg = "File size exceeds the maximum limit of 5MB."

        return ret, msg
    
    def _parse_csv_file(self, user, csv_file):
        csv_data = TextIOWrapper(csv_file.file, encoding='utf-8')
        reader = csv.reader(csv_data)
        success_count = 0
        error_count = 0
        duplicate_count = 0
        for row in reader:
            if reader.line_num == 1:
                continue
            email = row[0]
            first_name = row[1]
            middle_name = row[2]
            last_name = row[3]
            try:
                validate_email(email)
            except ValidationError:
                error_count += 1
                continue
            try:
                user.owners_fans.create(email=email, first_name=first_name,middle_name=middle_name,last_name=last_name)
            except IntegrityError:
                duplicate_count += 1
            else:
                success_count += 1
        return "Processed!\nSuccessful count: %s\nDuplicate count: %s\nError count: %s" % (success_count, duplicate_count, error_count)

    def _handle_csv_file(self, user, csv_file):
        err_msg = None
        success_msg = None
        check_ret,check_msg = FansUploadView._check_csv_file(csv_file)
        if check_ret != 0:
            err_msg = check_msg
        else:
            success_msg = self._parse_csv_file(user, csv_file)

        return err_msg, success_msg

    def post(self, request, *args, **kwargs):
        retData = {}
        err_msg = None
        success_msg = None

        user = request.user
        csv_file = request.FILES['csv']
        csv_file = request.FILES['csv']
        if csv_file:
            err_msg,success_msg = self._handle_csv_file(user, csv_file)
            retData['err_msg'] = err_msg
            retData['success_msg'] = success_msg    
        
        retData = {'err_msg': err_msg, 'success_msg': success_msg}
        return render(request, self.template_name, retData)
    
class FansDownloadView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user = request.user
        email_name = user.email.split('@')[0]
        time_now = timezone.now()
        time_format = Time_format(time_now)
        file_name = "%s-%s.csv" % (email_name,time_format)
        response = HttpResponse(content_type='text/csv') 
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
  
        writer = csv.writer(response) 
        writer.writerow(['email', 'first_name', 'middle_name', 'last_name', 'date_joined']) 
  
        FansModel = user.owners_fans
        fans = FansModel.all() 
        for fan in fans: 
            date_joined = Time_format(fan.date_joined)
            writer.writerow([fan.email, fan.first_name, fan.middle_name, fan.last_name, date_joined]) 
  
        return response 