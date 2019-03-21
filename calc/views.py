from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.
def index(request):
    if request.method == 'POST':
        try:
            x1 = float(request.POST['x1'])
            x2 = float(request.POST['x2'])
        except ValueError:
            result = "Non-float number inputted, please input float number"
        else:
            operation = {
                'add': x1 + x2,
                'substract': x1 - x2,
                'multiple': x1 * x2,
                'division': x1 / x2,
            }
            btn = request.POST['btn']
            result = operation.get(btn)
        # return redirect(reverse('result', kwargs={'res':result}))
        template = 'calc/result.html'
        return render(request, template, {'result': result, 'x1': x1, 'x2': x2, 'btn': btn})

    template = 'calc/index.html'
    return render(request, template)