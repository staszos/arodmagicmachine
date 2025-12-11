from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.



def layout(request):
    return render(request, 'main_donation_structure/base.html')

def main_donation_structure(request):
    return render(request, 'main_donation_structure/main_text.html')
def arod_main_FAQ(request):
    return render(request, 'main_donation_structure/arod_main_FAQ.html')

def arod_main_role_tariff(request):
    return render(request, 'main_donation_structure/arod_main_role_tariff.html')
def arod_main_mix_donat_1(request):
    return render(request, 'main_donation_structure/arod_main_mix_donat_1.html')
def arod_main_other_services(request):
    return render(request, 'main_donation_structure/arod_main_other_services.html')
def arod_main_race_donat(request):
    return render(request, 'main_donation_structure/arod_main_race_donat.html')
def arod_main_item_list_donat_1(request):
    return render(request, 'main_donation_structure/arod_main_item_list_donat_1.html')
def arod_main_team_list_donat_1(request):
    return render(request, 'main_donation_structure/arod_main_team_list_donat_1.html')
def arod_main_magic_list_donat_1(request):
    return render(request, 'main_donation_structure/arod_main_magic_list_donat_1.html')
def arod_main_begin(request):
    return render(request, 'main_donation_structure/arod_main_begin.html')





def GetInputValue(request):
  input_value = request.POST['quantity']
  return HttpResponse(input_value)



  