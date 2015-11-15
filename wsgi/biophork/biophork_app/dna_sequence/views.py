from django.shortcuts import get_object_or_404, render, get_list_or_404
from biophork_app.dna_sequence.models import Contact

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import datetime

class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class QuizIndexView(generic.ListView):

    template_name = 'text_search/index.html'
    context_object_name = 'latest_poll_list'



class QuizScoreView(generic.DetailView):
    model = Contact
    template_name = 'questions/quiz_result.html'