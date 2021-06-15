from re import A
from django.shortcuts import redirect, render
from django.http import request,HttpResponse,JsonResponse
from django.core.files.storage import FileSystemStorage
from .models import Resume
from .forms import resumeForm

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ResumeSerializers

from .resources import ResumeResources
# Create your views here.



def home(request):
    return render(request,'api/base.html')

def successUpload(request):
    return render(request,'api/successUpload.html')

def uploadResume(request):
    if request.method == 'POST':
        form = resumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('successUpload')
    else:
        form = resumeForm()
    return render(request,'api/uploadResume.html',{'form':form})

def viewResume(request):
    r = Resume.objects.all()
    return render(request,'api/viewResume.html',{'resumes':r})

@api_view(['GET'])
def getApi(request):
    r = Resume.objects.all()
    serial = ResumeSerializers(r,many = True)
    return Response(serial.data)


@api_view(['GET'])
def apiId(request,pk):
    r = Resume.objects.get(id = pk)
    serial = ResumeSerializers(r,many = False)
    return Response(serial.data)



def getXls(request):
    person_resource = ResumeResources()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response

'''
def getXls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Username', 'Resume' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    json = []
    #for r in Resume.objects.all():
    #    json.append({"phone": r.phone(), "email" :  r.email()})
    rows = Resume.objects.all().values_list('Name', 'resume')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response
'''