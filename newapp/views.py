from django.shortcuts import render
from .models import joint
from .forms import JointForm
from django.http import JsonResponse


def index(request):
    return render(request, 'layouts/index.html')

def wl(request):
    return render(request, 'layouts/wl1.html')

def temp_foo():
    pass


def autocomplete(request):
    if 'term' in request.GET:
        print(request)
        title_query = request.GET.get('term')
        titles = joint.objects.filter(title__istartswith=title_query).values_list('title', flat=True).distinct()
        data = list(set(titles))
        return JsonResponse(data, safe=False)


def splitting_requests(request):
    print(str(request).replace("<WSGIRequest: GET '/splitting_req?", '').replace("'", '').replace(">", '').split('/'))
    query_list = str(request).replace("<WSGIRequest: GET '/splitting_req?", '').replace("'", '').replace(">", '').split('/')
    table = joint.objects.filter(title__istartswith=query_list[0]).values_list('line', flat=True).distinct()
    context = {
        'joints': table,
        'title': 'Список стыков'
    }
    print(len(set(list(table))))
    # return render(request, 'layouts/table_joints_query.html', context)

    return JsonResponse({'result': list(set(list(table)))})


def autocomplete_line(request):
    print(request)
    if 'term' in request.GET:
        line_query = request.GET.get('term')
        line = joint.objects.filter(line__istartswith=line_query).values_list('line', flat=True).distinct()
        data = list(set(line))
        return JsonResponse(data, safe=False)


def autofilling_table(request):
    print(str(request).replace("<WSGIRequest: GET '/filling_table?", '').replace("'", '').replace(">", '').split('/'))
    query_list = str(request).replace("<WSGIRequest: GET '/filling_table?", '').replace("'", '').replace(">", '').split('/')
    joints = joint.objects.filter(title__istartswith=query_list[0]).filter(line__istartswith=query_list[1])
    res = {'isometric': [], 'joint_number': [], 'date_weld': []}
    for i in joints:
        res['isometric'].append(i.isometric)
        res['joint_number'].append(i.locationweld + i.numberjoint)
        res['date_weld'].append(i.dateweld.strftime('%d.%m.%Y'))
    return JsonResponse(res, safe=False)



def create_joint(request):
    form = JointForm()
    data = {
        'form': form,
    }
    return render(request, 'layouts/create_joint.html', data)

def filling_table(request):
    print(request)
    request_query = request.GET.get('term')

    query_list_lines = joint.objects.filter(title=request_query).values_list('line', flat=True).distinct()
    print(list(query_list_lines))
    return JsonResponse({'result': set(list(query_list_lines))})




def mtr(request):
    return render(request, 'layouts/mtr_page.html')

def nk(request):
    return render(request, 'layouts/nk_page.html')

def summary(request):
    return render(request, 'layouts/summary_inf.html')







#
# @login_required(login_url="/login/")
# def index(request):
#     joints = joint.objects.filter(dateweld__range=["2022-01-01", "2023-01-01"])
#     context = {
#         'joints': joints,
#         'title': 'Список стыков'
#     }
#     html_template = loader.get_template('layouts/index.html')
#     return HttpResponse(html_template.render(context, request))









#
# @login_required(login_url="/login/")
def pages(request):
    pass
    # context = {}
    # # All resource paths end in .html.
    # # Pick out the html file name from the url. And load that template.
    # try:
    #
    #     load_template = request.path.split('/')[-1]
    #
    #     if load_template == 'admin':
    #         return HttpResponseRedirect(reverse('admin:index'))
    #     context['segment'] = load_template
    #
    #     html_template = loader.get_template('home/' + load_template)
    #     return HttpResponse(html_template.render(context, request))
    #
    # except template.TemplateDoesNotExist:
    #
    #     html_template = loader.get_template('home/page-404.html')
    #     return HttpResponse(html_template.render(context, request))
    #
    # except:
    #     html_template = loader.get_template('home/page-500.html')
    #     return HttpResponse(html_template.render(context, request))