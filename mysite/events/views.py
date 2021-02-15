from events.models import Event
from django.shortcuts import render

# Create your views here.
import calendar
from calendar import HTMLCalendar
from datetime import datetime



from django.views.generic import ListView, DetailView, TemplateView

class EventLV(TemplateView):
    template_name = 'events/events.html'
    # model = Event
    # context_object_name ='Event'

    def get_context_data(self,**kwargs):  
        context = super().get_context_data(**kwargs)
        context['object_list'] = Event.objects.all()

        year=datetime.now().year
        month=datetime.now().strftime('%B')
        month = month.capitalize()
        # Convert month from name to number
        month_number = list(calendar.month_name).index(month)
        month_number = int(month_number)

        # create a calendar
        cal = HTMLCalendar().formatmonth(
            year,
            month_number)
        # Get current year
        now =datetime.now()
        current_year = now.year

        # Get current time
        time =now.strftime('%I:%M:%S %p')  
        # context["year"]  = year

        context.update({
            "year":year,
            "month":month,
            "month_number":month_number,
            "cal": cal,
            "current_year":current_year,
            "time":time,
            })

        return context

    def home(self,request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    
        month = month.capitalize()
        # Convert month from name to number
        month_number = list(calendar.month_name).index(month)
        month_number = int(month_number)

        # create a calendar
        cal = HTMLCalendar().formatmonth(
            year,
            month_number)
        # Get current year
        now =datetime.now()
        current_year = now.year

        # Get current time
        time =now.strftime('%I:%M:%S %p')

        
        return render(request,
            'events/events.html',{
            "year":year,
            "month":month,
            "month_number":month_number,
            "cal": cal,
            "current_year":current_year,
            "time":time,
            })