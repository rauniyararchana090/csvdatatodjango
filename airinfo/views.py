from django.shortcuts import render
import csv
import pandas as pd 


# Create your views here.

def display(request):
 
    
    csv_file = open('newinfo.csv', 'r')
    csv_reader = csv.reader(csv_file)

    info = []
    for line in csv_reader:
        next(csv_reader)

        row=[]
        for i in range(5):
            row.append(line[i])
        info.append(row)
    return render(request, 'info_display.html',  {'list': info})