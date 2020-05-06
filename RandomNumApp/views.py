from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib import auth
#from .models import gameplay_info
# Create your views here.

import random
import requests


#Function to check the number is in range or not.
def is_valid_num(num):
    if 1 <= int(num) <= 1000:
        return True
    else:
        return False

def home(request):
    return render(request, template_name='html/RandomNumApp/home.html',)

#Function to Execute the Comparing Operations.
def RanNum(request):
    if not request.session.exists(request.session.session_key):
        num_guesses=0
        print('no session')
        number=random.randint(1,1000)
        request.session.create()
        request.session['number']=number
        request.session['num_guesses']=num_guesses
    else:
        number=request.session['number']
        num_guesses=request.session['num_guesses']
        if request.method=='POST':
            print('session')
            #Takes input from form as Integer
            guessNum = int(request.POST['guess'])
        # If the Guess is correct.      
            if guessNum == number:
                messages.info(request,str(number)+" is the Correct Answer!" + "\n Total number of Guesses:"+ str(num_guesses+1))
                if num_guesses <6:
                    messages.info(request, "Brilliant! Keep It Up!")
                elif num_guesses <12:
                    messages.info(request, "Good Performance!")
                else:
                    messages.info(request, "Better Late Than Never!")
                #Optional operation to take the data.
                #gameplay_info.objects.create(Random_Number=guessNum,Number_Guesses=num_guesses+1)
                #Resetting the Number of Guesses

                
                auth.logout(request)
                print('end of session')
                return render(request, template_name='html/RandomNumApp/exit.html')
            #For Incorrect Guesses.
            else:
                if not is_valid_num(guessNum):
                    messages.info(request, "Not in range!")
                elif guessNum > number:
                    messages.info(request, "Too High! Go Lower")
                else:
                    messages.info(request, "Too Low! Go Higher")
                #Incrementing the count by 1 by calling the function.
                num_guesses=request.session['num_guesses']
                num_guesses=num_guesses+1
                request.session['num_guesses']=num_guesses
                print(number)
                return redirect('/gamepage')

        else :
            return render(request, template_name='html/RandomNumApp/Ran.html')

    return render(request, template_name='html/RandomNumApp/Ran.html')





    

        
        



        


            
        