from django.shortcuts import render

def index_page(requsts):
    return render(requsts, 'title.html')