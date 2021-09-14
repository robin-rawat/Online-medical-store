from django.db.models.query_utils import select_related_descend
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic.edit import FormView
import csv
from .models import Medicine
from .forms import QueryInputForm

class QueryResponseView(FormView):
    template_name = 'form.html'
    form_class = QueryInputForm
    def form_valid(self,form):
        query = form.cleaned_data.get('query_text')
        #considering input contains multiple words, splitting input into separate words
        qb = tuple(query.split())
        qs=list()
        #iterating through each word in input query for search
        for i in qb:
            #Limiting word length to 3 and more, ignoring small word matches like [i, am]
            if len(i) > 2:
                qs += Medicine.objects.filter(sku_name__icontains=i)
        context={
            'queryset':qs
        }
        return render(self.request, 'content.html', context)

def med_details(request, pk):
    qs = get_object_or_404(Medicine, pk=pk)
    context = {'queryset':qs}
    return render(request,'detail.html', context)

def load_data(request):
    # a list for object creation tracking 
    created=[]
    with open('meddata.csv') as f:
        reader = csv.reader(f)
        #skipping first line of headers
        next(reader)
        for row in reader:
            _, c = Medicine.objects.get_or_create(
                sku_id = row[0] if row[0]!='-' else None,
                product_id = row[1] if row[1]!='-' else None,
                sku_name=row[2] if row[2]!='-' else None,
                price = row[3] if row[3]!='-' else None,
                manufacturer_name = row[4] if row[4]!='-' else None,
                salt_name = row[5] if row[5]!='-' else None,
                drug_form = row[6] if row[6]!='-' else None,
                pack_size = row[7] if row[7]!='-' else None,
                strength = row[8] if row[8]!='-' else None,
                product_banned = row[9] if row[9]!='-' else None,
                unit = row[10] if row[10]!='-' else None,
                price_per_unit = row[11] if row[11]!='-' else None)
            #capturing the status of object creation
            created.append(c)
        #for tracking purpose
        print(created)

    return HttpResponse("Data is loaded to database successfully!")
