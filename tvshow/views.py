from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic

'''Чтение обьекта через формы CRUD'''


class TvshowView(generic.ListView):
    template_name = 'tvshow/films.html'
    queryset = models.TvShow.objects.all()

    def get_queryset(self):
        return models.TvShow.objects.all()


class TvshowDetail(generic.DetailView):
    template_name = 'tvshow/films_detail.html'

    def get_object(self, **kwargs):
        tvshow_id = self.kwargs.get("id")
        return get_object_or_404(models.TvShow, id=tvshow_id)


'''добавление объекта через формы CRUD'''


class CreateTvshowView(generic.CreateView):
    template_name = 'tvshow/crud/add_film.html'
    form_class = forms.TvshowForm
    queryset = models.TvShow.objects.all()
    success_url = '/tvshow/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateTvshowView, self).form_valid(form=form)


'''Удаление объкта из БД CRUD'''


class DeleteTvshowView(generic.DeleteView):
    template_name = 'tvshow/crud/confirm_delete.html'
    success_url = '/tvshow/'

    def get_object(self, **kwargs):
        tvshow_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=tvshow_id)


''' изменение объктов CRUD'''


class UpdateTvshowView(generic.UpdateView):
    template_name = 'tvshow/crud/update_films.html'
    form_class = forms.TvshowForm
    success_url = '/tvshow/'

    def get_object(self, **kwargs):
        tvshow_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=tvshow_id)

    def form_valid(self, form):
        return super(UpdateTvshowView, self).form_valid(form=form)


class Search(generic.ListView):
    template_name = "tvshow/films.html"
    context_context_object_name = "tvshow"
    paginate_by = 5

    def get_queryset(self):
        return models.TvShow.objects.filter(
            title__icontains=self.request.GET.get("q")
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context


class CreateFilmView(generic.CreateView):
    template_name = 'tvshow/Reviews.html'
    form_class = forms.FilmViewForm
    queryset = models.Reviews.objects.all()
    success_url = '/tvshow/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateFilmView, self).form_valid(form=form)




# def tvshow_view(request):
#     tvshow = models.TvShow.objects.all()
#     return render(request, 'tvshow/films.html',
#                   {'tvshow': tvshow})

# def tvshow_detail_view(request, id):
#     tvshow_id = get_object_or_404(models.TvShow, id=id)
#     return render(request, 'tvshow/films_detail.html',
#                   {'tvshow_id': tvshow_id})

# def create_tvshow_view(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.TvshowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Фильм успешно добавлена в БД")
#     else:
#         form = forms.TvshowForm()
#     return render(request, 'tvshow/crud/add_film.html',
#                   {"form": form})

# def delete_tvshow_view(request, id):
#     tvshow_id = get_object_or_404(models.TvShow, id=id)
#     tvshow_id.delete()
#     return HttpResponse("Фильм успешно удалена из БД")


#
# def update_tvshow_view(request, id):
#     tvshow_id = get_object_or_404(models.TvShow, id=id)
#     if request.method == "POST":
#         form = forms.TvshowForm(instance=tvshow_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Успешно изменено")
#     else:
#         form = forms.TvshowForm(instance=tvshow_id)
#
#     context = {
#         'form': form,
#         'tvshow_id': tvshow_id
#     }
#     return render(request, 'tvshow/crud/update_films.html', context)
