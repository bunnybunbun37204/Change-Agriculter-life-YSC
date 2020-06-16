from django.shortcuts import render
from django.http import HttpResponse
from .models import Data
# Create your views here.
def hello(request):
    return render(request,'index.html')
def foropen(request):
    return render(request,'foropen.html')
def foropen2(request):
    return render(request,'foropen2.html')
def foropen3(request):
    return render(request,'foropen3.html')
def form(request):
    return render(request,'form.html')
def form1_1(request):
    return render(request,'form1_1.html')
def form2(request):
    return render(request,'form2.html')
def form2_1(request):
    return render(request,'form2_1.html')
def form3(request):
    return render(request,'form3.html')
def form3_1(request):
    return render(request,'form3_1.html')
def form4(request):
    return render(request,'form4.html')
def select(request):
    return render(request,'select.html')
def addBlog(request):
    nitrogen=int(request.GET['num1'])
    potasium=int(request.GET['num3'])
    phosphorus=int(request.GET['num2'])
    kilogram = int(request.GET['num4'])
    area = kilogram
    age = int(request.GET['num5'])
    if age in range(0,3):
        kilogram=round(kilogram*70*150/1000)
        active_Phosphorus = round(kilogram*phosphorus/46,2)
        nitrogen_Phos = round(18*active_Phosphorus/kilogram,2)
        nitrogen_nothave= round(nitrogen-nitrogen_Phos,2)
        Urea = round(kilogram*nitrogen_nothave/46,2)
        Mop = round(kilogram*potasium/60,2)
    elif age in range(3,7) :
        kilogram=round(kilogram*70*500/1000)
        active_Phosphorus = round(kilogram*phosphorus/46,2)
        nitrogen_Phos = round(18*active_Phosphorus/kilogram,2)
        nitrogen_nothave= round(nitrogen-nitrogen_Phos,2)
        Urea = round(kilogram*nitrogen_nothave/46,2)
        Mop = round(((kilogram*potasium/60)),2)
    elif age in range(7,16):
        kilogram=round(kilogram*70*700/1000)
        active_Phosphorus = round(kilogram*phosphorus/46,2)
        nitrogen_Phos = round(18*active_Phosphorus/kilogram,2)
        nitrogen_nothave= round(nitrogen-nitrogen_Phos,2)
        Urea = round(kilogram*nitrogen_nothave/46,2)
        Mop = round(((kilogram*potasium/60)),2)
    elif age in range(16,100):
        kilogram=round(kilogram*70)
        active_Phosphorus = round(kilogram*phosphorus/46,2)
        nitrogen_Phos = round(18*active_Phosphorus/kilogram,2)
        nitrogen_nothave= round(nitrogen-nitrogen_Phos,2)
        Urea = round(kilogram*nitrogen_nothave/46,2)
        Mop = round(((kilogram*potasium/60)),2)
    else:
        kilogram=0
        active_Phosphorus = 0
        nitrogen_Phos = 0
        nitrogen_nothave= 0
        Urea = 0
        Mop = 0
    total = round(Urea+active_Phosphorus+Mop,2)
    element = round(kilogram-total,2)
    result = total+element
    cost_Urea = round(Urea*11.9,2)
    cost_DAP = round(active_Phosphorus*17.7,2)
    cost_MOP = round(Mop*10,2)
    cost_Total = round(cost_DAP+cost_Urea+cost_MOP,2)
    return render(request,'result.html',
    {'urea':Urea,
    'dap': active_Phosphorus,
    'mop': Mop,
    'total':result,
    'element':element,
    'cost_Urea':cost_Urea,
    'cost_DAP':cost_DAP,
    'cost_MOP':cost_MOP,
    'cost_Total':cost_Total
    })
def addBlog1_1(request):
    nitrogen=int(request.GET['num1'])
    potasium=int(request.GET['num3'])
    phosphorus=int(request.GET['num2'])
    kilogram = int(request.GET['num4'])
    age = int(request.GET['num5'])
    if age in range(0,3):
        kilogram=round(kilogram*70*150/1000)
        active_Phosphorus = round(kilogram*phosphorus/46,2)
        nitrogen_Phos = round(18*active_Phosphorus/kilogram,2)
        nitrogen_nothave= round(nitrogen-nitrogen_Phos,2)
        Urea = round(kilogram*nitrogen_nothave/21,2)
        Mop = round(kilogram*potasium/60,2)
    elif age in range(3,7) :
        kilogram=round(kilogram*70*500/1000)
        active_Phosphorus = round(kilogram*phosphorus/46,2)
        nitrogen_Phos = round(18*active_Phosphorus/kilogram,2)
        nitrogen_nothave= round(nitrogen-nitrogen_Phos,2)
        Urea = round(kilogram*nitrogen_nothave/21,2)
        Mop = round(((kilogram*potasium/60)),2)
    elif age in range(7,16):
        kilogram=round(kilogram*70*700/1000)
        active_Phosphorus = round(kilogram*phosphorus/46,2)
        nitrogen_Phos = round(18*active_Phosphorus/kilogram,2)
        nitrogen_nothave= round(nitrogen-nitrogen_Phos,2)
        Urea = round(kilogram*nitrogen_nothave/21,2)
        Mop = round(((kilogram*potasium/60)),2)
    elif age in range(16,100):
        kilogram=round(kilogram*70)
        active_Phosphorus = round(kilogram*phosphorus/46,2)
        nitrogen_Phos = round(18*active_Phosphorus/kilogram,2)
        nitrogen_nothave= round(nitrogen-nitrogen_Phos,2)
        Urea = round(kilogram*nitrogen_nothave/21,2)
        Mop = round(((kilogram*potasium/60)),2)
    else:
        kilogram=0
        active_Phosphorus = 0
        nitrogen_Phos = 0
        nitrogen_nothave= 0
        Urea = 0
        Mop = 0
    total = round(Urea+active_Phosphorus+Mop,2)
    element = round(kilogram-total,2)
    result = round(total+element,2)
    cost_Urea = round(Urea*7,2)
    cost_DAP = round(active_Phosphorus*17.7,2)
    cost_MOP = round(Mop*10,2)
    cost_Total = round(cost_DAP+cost_Urea+cost_MOP,2)
    return render(request,'result.html',
    {'urea':Urea,
    'dap': active_Phosphorus,
    'mop': Mop,
    'total':result,
    'element':element,
    'cost_Urea':cost_Urea,
    'cost_DAP':cost_DAP,
    'cost_MOP':cost_MOP,
    'cost_Total':cost_Total
    })
def addBlog2(request):
    area=int(request.GET['num1'])
    age=int(request.GET['num2'])
    if age in range(0,2):
        Kilo = round(area*0.3*22,2)
        Nitrogen = 20
        Phosphorus = 11
        Potasium = 11
        Urea = round((0.34*Kilo),2)
        DAP = round((0.24 *Kilo),2)
        MOP = round(0.18 *Kilo,2)
        MgO = 0
        total = round(Kilo,2)
    elif age in range(2,3):
        Kilo = round(area*22,2)
        Nitrogen = 14
        Phosphorus = 9
        Potasium = 20
        Urea = round(0.11*Kilo,2)
        DAP = round(0.10*Kilo,2)
        MOP = round((0.23+0.5)*Kilo,2)
        MgO = round(0.01*Kilo,2) 
        total = Kilo*1
    elif age in range(3,4):
        Kilo = round(area*22,2)
        Nitrogen = 14
        Phosphorus = 9
        Potasium = 20
        Urea = round(0.18*Kilo,2)
        DAP = round(0.16*Kilo,2)
        MOP = ((1.17)*Kilo)
        MgO = round(0.016*Kilo,2) 
        total = round(Kilo*1.6,2)
    elif age in range(4,5):
        Kilo = round(area*22,2)
        Nitrogen = 14
        Phosphorus = 9
        Potasium = 20
        Urea = round(0.34*Kilo,2)
        DAP = round(0.29*Kilo,2)
        MOP = round(((2)*Kilo),2)
        MgO = round(0.03*Kilo,2) 
        total = Kilo*3
    elif age in range(5,6):
        Kilo = round(area*22,2)
        Nitrogen = 14
        Phosphorus = 9
        Potasium = 20
        Urea = round(0.46*Kilo,2)
        DAP = round(0.39*Kilo,2)
        MOP = round((2.67)*Kilo,2)
        MgO = round(0.04*Kilo,2) 
        total = Kilo*4
    elif age in range(6,30):
        Kilo = round(area*22,2)
        Nitrogen = 14
        Phosphorus = 14
        Potasium = 21
        Urea = round(0.37*Kilo,2)
        DAP = round(0.61*Kilo,2)
        MOP = round((2.20)*Kilo,2)
        MgO = round(0.04*Kilo,2) 
        total = round(Kilo*3.5,2)
    result = round(total-(Urea+DAP+MOP+MgO),2)
    total=round((Urea+DAP+MOP+MgO+result),2)
    cost_Urea = round(Urea*11.9,2)
    cost_DAP = round(DAP*17.7,2)
    cost_MOP = round(MOP*10,2)
    cost_Mgo = round(MgO*8.9,2)
    cost_Total = round(cost_DAP+cost_Urea+cost_MOP+cost_Mgo,2)
    return render(request,'result2.html',{
        'Nitrogen':Nitrogen,
        'Phosphorus':Phosphorus,
        'Potasium':Potasium,
        'Urea':Urea,
        'DAP':DAP,
        'MOP': MOP,
        'MgO': MgO,
        'total': total,
        'element':result,
        'cost_Urea':cost_Urea,
        'cost_DAP':cost_DAP,
        'cost_MOP':cost_MOP,
        'cost_Mgo':cost_Mgo,
        'cost_Total':cost_Total
        })
def addBlog2_1(request):
    area=int(request.GET['num1'])
    age=int(request.GET['num2'])
    if age in range(0,2):
        Kilo = round(area*0.3*22,2)
        Nitrogen = 20
        Phosphorus = 11
        Potasium = 11
        Urea = round((0.75*Kilo),2)
        DAP = round((0.24 *Kilo),2)
        MOP = round(0.18 *Kilo,2)
        MgO = 0
        total = round(Kilo,2)
    elif age in range(2,3):
        Kilo = round(area*22,2)
        Nitrogen = 14
        Phosphorus = 9
        Potasium = 20
        Urea = round(0.25*Kilo,2)
        DAP = round(0.10*Kilo,2)
        MOP = round((0.23+0.5)*Kilo,2)
        MgO = round(0.01*Kilo,2) 
        total = Kilo*1
    elif age in range(3,4):
        Kilo = round(area*22,2)
        Nitrogen = 14
        Phosphorus = 9
        Potasium = 20
        Urea = round(0.40*Kilo,2)
        DAP = round(0.16*Kilo,2)
        MOP = ((1.17)*Kilo)
        MgO = round(0.016*Kilo,2) 
        total = round(Kilo*1.6,2)
    elif age in range(4,5):
        Kilo = round(area*22,2)
        Nitrogen = 14
        Phosphorus = 9
        Potasium = 20
        Urea = round(0.75*Kilo,2)
        DAP = round(0.29*Kilo,2)
        MOP = round(((2)*Kilo),2)
        MgO = round(0.03*Kilo,2) 
        total = Kilo*3
    elif age in range(5,6):
        Kilo = round(area*22,2)
        Nitrogen = 14
        Phosphorus = 9
        Potasium = 20
        Urea = round(1*Kilo,2)
        DAP = round(0.39*Kilo,2)
        MOP = round((2.67)*Kilo,2)
        MgO = round(0.04*Kilo,2) 
        total = Kilo*4
    elif age in range(6,30):
        Kilo = round(area*22,2)
        Nitrogen = 14
        Phosphorus = 14
        Potasium = 21
        Urea = round(0.81*Kilo,2)
        DAP = round(0.61*Kilo,2)
        MOP = round((2.20)*Kilo,2)
        MgO = round(0.04*Kilo,2) 
        total = round(Kilo*3.5,2)
    result = round(total-(Urea+DAP+MOP+MgO),2)
    total=round(Urea+DAP+MOP+MgO+result,2)
    cost_Urea = round(Urea*7,2)
    cost_DAP = round(DAP*17.7,2)
    cost_MOP = round(MOP*10,2)
    cost_Mgo = round(MgO*8.9,2)
    cost_Total = round(cost_DAP+cost_Urea+cost_MOP+cost_Mgo,2)
    return render(request,'result2.html',{
        'Nitrogen':Nitrogen,
        'Phosphorus':Phosphorus,
        'Potasium':Potasium,
        'Urea':Urea,
        'DAP':DAP,
        'MOP': MOP,
        'MgO': MgO,
        'total': total,
        'element':result,
        'cost_Urea':cost_Urea,
        'cost_DAP':cost_DAP,
        'cost_MOP':cost_MOP,
        'cost_Mgo':cost_Mgo,
        'cost_Total':cost_Total
        })
def addCustom(request):
    nitrogen=int(request.GET['num1'])
    potasium=int(request.GET['num3'])
    phosphorus=int(request.GET['num2'])
    kilogram = int(request.GET['num4'])
    active_Phosphorus = round(kilogram*phosphorus/46,2)
    nitrogen_Phos = round(18*active_Phosphorus/kilogram,2)
    nitrogen_nothave= round(nitrogen-nitrogen_Phos,2)
    Urea = round(kilogram*nitrogen_nothave/46,2)
    Mop = round(kilogram*potasium/60,2)
    total = round(Urea+active_Phosphorus+Mop,2)
    element = round(kilogram-total,2)
    result = total+element
    cost_Urea = round(Urea*11.9,2)
    cost_DAP = round(active_Phosphorus*17.7,2)
    cost_MOP = round(Mop*10,2)
    cost_Total = round(cost_DAP+cost_Urea+cost_MOP,2)
    return render(request,'result.html',
    {'urea':Urea,
    'dap': active_Phosphorus,
    'mop': Mop,
    'total':result,
    'element':element,
    'cost_Urea':cost_Urea,
    'cost_DAP':cost_DAP,
    'cost_MOP':cost_MOP,
    'cost_Total':cost_Total
     })
def addCustom2(request):
    nitrogen=int(request.GET['num1'])
    potasium=int(request.GET['num3'])
    phosphorus=int(request.GET['num2'])
    kilogram = int(request.GET['num4'])
    active_Phosphorus = round(kilogram*phosphorus/46,2)
    nitrogen_Phos = round(18*active_Phosphorus/kilogram,2)
    nitrogen_nothave= round(nitrogen-nitrogen_Phos,2)
    Urea = round(kilogram*nitrogen_nothave/21,2)
    Mop = round(kilogram*potasium/60,2)
    total = round(Urea+active_Phosphorus+Mop,2)
    element = round(kilogram-total,2)
    result = total+element
    cost_Urea = round(Urea*7,2)
    cost_DAP = round(active_Phosphorus*17.7,2)
    cost_MOP = round(Mop*10,2)
    cost_Total = round(cost_DAP+cost_Urea+cost_MOP,2)
    return render(request,'result.html',
    {'urea':Urea,
    'dap': active_Phosphorus,
    'mop': Mop,
    'total':result,
    'element':element,
    'cost_Urea':cost_Urea,
    'cost_DAP':cost_DAP,
    'cost_MOP':cost_MOP,
    'cost_Total':cost_Total
     })
