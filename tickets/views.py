from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .ticket import TicketForm
from .models import Ticket

# Create your views here.
def new_ticket(request):
    #ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user_id = request.user
            ticket.created_at = timezone.now()
            ticket.save()
            return redirect('ticket_list')
    else:
        form = TicketForm()
    return render(request, 'ticket/new_ticket.html', {'form': form})

# view the list of tickets
def ticket_list(request):
    tickets = Ticket.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    return render(request,'ticket/ticket_list.html', {'tickets': tickets})