from django.shortcuts import render, redirect
import random
import datetime

# Create your views here.
def index(request):
	if 'activity' not in request.session:
		request.session['activity'] = ""
	if 'gold' not in request.session:
		request.session['gold'] = 0 
	return render(request, "ninja_gold_app/index.html")


def process_money(request):
	if request.POST['building'] == 'farm':
		money = random.randrange(10,20)
		request.session['gold'] += money #farm: 10-20 gold
		request.session['activity'] += "Earned "+ str(money)+ " gold from " + request.POST['building'] + "! " + "("+ str(datetime.datetime.now())+")"
	if request.POST['building'] == 'cave':
		money = random.randrange(5,10)
		request.session['gold'] += money #cave: 5-10 gold
		request.session['activity'] += "Earned "+ str(money)+ " gold from " + request.POST['building'] + "! " + "("+ str(datetime.datetime.now())+")"
	if request.POST['building'] == 'house':
		money = random.randrange(2,5)
		request.session['gold'] += money #house: 2-5 gold
		request.session['activity'] += "Earned "+ str(money)+ " gold from " + request.POST['building'] + "! " + "("+ str(datetime.datetime.now())+")"
	if request.POST['building'] == 'casino':
		money = random.randrange(-50,50)
		request.session['gold'] += money #casino: takes or earns 0-50 gold
		request.session['activity'] += "Earned "+ str(money)+ " gold from " + request.POST['building'] + "! " + "("+ str(datetime.datetime.now())+")"
	return redirect('/') 
	

def clear(request):
	request.session.flush()
	return redirect('/') 