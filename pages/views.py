from django.shortcuts import redirect, render
from .forms import ContactForm


def homePage(request):
    context = {
        'title': 'Pagina inicial',
        'texto': 'Inicial'
    }
    return render(request, 'index.html', context)


def about_page(request):
    context = {
        'title': 'Pagina sobre',
        'texto': 'Sobre'
    }
    return render(request, 'about_page.html', context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': 'Pagina de contato',
        'texto': 'Contato',
        'form': contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        return redirect('pages:index')
    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get('Nome_Completo'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('Mensagem'))   
    return render(request, 'contact_page.html', context)

    

