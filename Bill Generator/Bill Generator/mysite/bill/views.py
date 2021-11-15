from django.shortcuts import render
from .models import  Bills
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method == "POST":
        pro_name= request.POST.get("pro_name","")
        pro_img= request.POST.get("pro_img","")
        pro_quantity= request.POST.get("pro_quantity","")
        pro_rate= request.POST.get("pro_rate","")
        bill = Bills(
            pro_name = pro_name,
            pro_img=pro_img,
            pro_quantity=pro_quantity,
            pro_rate=pro_rate,
        )
        bill.save()
    


    return render(request,'index.html')

def detail(request,id):
    de=Bills.objects.get(pk=id)
    
    template_path = 'detail.html'
    context = {'de': de}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="dowload.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    # return render(request,'detail.html',{'de':de})

def list(request):
    de = Bills.objects.all()
    return render(request,'list.html',{"de":de})