from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import DailyNotes
from .forms import DailyNotesForm
# Create your views here.


@login_required(login_url='accounts/login/')
def index(request):
    daily_notes = DailyNotes.objects.filter(user_owner=request.user)
    context = {'daily_notes': daily_notes}
    return render(request, 'main/index.html', context)


@login_required(login_url='accounts/login/')
def create_note(request):
    if request.method == 'POST':
        form = DailyNotesForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user_owner = request.user
            form.save()
            return redirect('main:index')
    context = {'form': DailyNotesForm}
    return render(request, 'main/create.html', context)


@login_required(login_url='accounts/login/')
def note_page(request, serial_id):
    daily_notes = DailyNotes.objects.filter(user_owner=request.user)
    this_note = DailyNotes.objects.filter(serial_number=serial_id).first()
    context = {'this_note': this_note, 'daily_notes': daily_notes}
    return render(request, 'main/note_page.html', context)
