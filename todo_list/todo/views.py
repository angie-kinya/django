from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForm
from .models import Todo

def index(request):
    # Retrieve all Todo items, ordered by date
    item_list = Todo.objects.order_by("-date")
    
    # Handle form submission
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task added successfully!")  # Add a success message
            return redirect('todo')  # Redirect to the same page to clear the form

    # Create a blank form for GET requests
    form = TodoForm()

    # Context for the template
    page = {
        "forms": form,  # Pass the form object
        "list": item_list,  # Pass the list of todos
        "title": "TODO LIST",  # Pass the title
    }
    return render(request, 'todo/index.html', page)

from django.shortcuts import get_object_or_404

def remove(request, item_id):
    # Fetch the item or return a 404 if not found
    item = get_object_or_404(Todo, id=item_id)
    item.delete()
    messages.info(request, "Task removed successfully!")  # Display success message
    return redirect('todo')
