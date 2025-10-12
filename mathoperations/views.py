from django.shortcuts import render
from django.views.generic import View
from mathoperations.forms import ArithmeticForm

class AdditionView(View):

    def get(self,request,*args,**kwargs):
        
        form_instance = ArithmeticForm()

        return render(request,'addition.html',{'form':form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data = request.POST

        #Initialize the form with the data

        form_instance = ArithmeticForm(form_data)
        
        # Check if the form is valid

        if form_instance.is_valid():

            validated_data = form_instance.cleaned_data
            n1 = validated_data.get('num1')
            n2 = validated_data.get('num2') 
            result = int(n1) + int(n2)

            return render(request,'addition.html',{'form':form_instance,'output':result})
        else:

            return render(request,'addition.html',{'form':form_instance})
    

   
