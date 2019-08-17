from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import TodoItem


class TodoList(ListView):
    model = TodoItem
    queryset = TodoItem.objects.all()


class TodoListComplete(ListView):
    model = TodoItem
    queryset = TodoItem.objects.filter(finished="True")
    template_name = 'item/todoitem_complete.html'


class TodoListIncomplete(ListView):
    model = TodoItem
    queryset = TodoItem.objects.filter(finished="False")
    template_name = 'item/todoitem_incomplete.html'


class TodoDetail(DetailView):
    model = TodoItem


class TodoCreate(CreateView):
    model = TodoItem
    fields = ['title', 'description', 'finished']
    
    def get_success_url(self):
        return reverse('todolist:todo_detail', kwargs={'pk': self.object.pk})


class TodoUpdate(UpdateView):
    model = TodoItem
    fields = ['finished']
    template_name = 'item/todoitem_confirm_finish.html'
    success_url = reverse_lazy('todolist:todo_all')


class TodoDelete(DeleteView):
    model = TodoItem
    success_url = reverse_lazy('todolist:todo_all')