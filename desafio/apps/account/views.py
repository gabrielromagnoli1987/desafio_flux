from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render


from account.forms import UserForm


def register(request):
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():            
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect(reverse('home:home'))
        else:
            print user_form.errors    
    else:
        user_form = UserForm()
        
    return render(request, 'account/register.html', {'user_form': user_form})