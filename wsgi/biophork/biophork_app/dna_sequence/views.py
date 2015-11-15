from django.shortcuts import get_object_or_404, render, get_list_or_404
from dna_sequence.models import Contact

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import simplejson

import forms
import datetime

class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class ListContactView(LoggedInMixin, generic.ListView):

    model = Contact
    template_name = 'contact_list.html'

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)

class IndexView(generic.ListView):

    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """
        Return the last five published polls (not including those set to be
        published in the future).
        """
        return Poll.objects.filter(pub_date__lte=datetime.datetime.now()).order_by('-pub_date')[:1]

class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any polls that aren't published yet.
        """
        return Poll.objects.filter(pub_date__lte=datetime.datetime.now())

class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

class CreateLoginView(generic.CreateView):
    model = Contact
    template_name = 'login.html'
    form_class = forms.LoginForm

    def get_success_url(self):
        return reverse('contacts-view')

    def get_context_data(self, **kwargs):

        context = super(CreateLoginView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-login',
                                    kwargs={'pk': self.get_object().id})
        return context

class ContactView(generic.DetailView):
    model = Contact
    template_name = 'contact.html'
    ScoreStatistics.objects.all().filter(user=1)

class CreateContactView(generic.CreateView):
    model = Contact
    template_name = 'edit_contact.html'
    form_class = forms.ContactForm

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):

        context = super(CreateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-new')
        return context

class UpdateContactView(generic.UpdateView):

    model = Contact
    template_name = 'edit_contact.html'
    form_class = forms.ContactForm

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):

        context = super(UpdateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-edit',
                                    kwargs={'pk': self.get_object().id})
        return context

class DeleteContactView(generic.DeleteView):

    model = Contact
    template_name = 'delete_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')

class ListAddressView(generic.ListView):

    model = Address
    template_name = 'address_list.html'

class CreateAddressView(generic.CreateView):

    model = Address
    template_name = 'edit_address.html'
    form_class = forms.AddressForm

    def get_success_url(self):
        return reverse('addresses-list')

    def get_context_data(self, **kwargs):

        context = super(CreateAddressView, self).get_context_data(**kwargs)
        context['action'] = reverse('addresses-new')

        return context

class UpdateAddressView(generic.UpdateView):

    model = Address
    template_name = 'edit_address.html'
    form_class = forms.AddressForm

    def get_success_url(self):
        return reverse('addresses-list')

    def get_context_data(self, **kwargs):

        context = super(UpdateAddressView, self).get_context_data(**kwargs)
        context['action'] = reverse('addresses-edit',
                                    kwargs={'pk': self.get_object().id})

        return context

class DeleteAddressView(generic.DeleteView):

    model = Address
    template_name = 'delete_address.html'

    def get_success_url(self):
        return reverse('addresses-list')

class AddressView(generic.DetailView):

    model = Address
    template_name = 'address.html'

class EditContactAddressView(generic.UpdateView):

    model = Contact
    template_name = 'edit_addresses.html'
    form_class = forms.AddressFormSet

    def get_success_url(self):

        # redirect to the Contact view.
        return self.get_object().get_absolute_url()

class ListQuestionView(generic.ListView):

    model = Question
    template_name = 'question_list.html'

class CreateQuestionView(generic.CreateView):

    model = Question
    template_name = 'edit_question.html'
    form_class = forms.QuestionForm

    def get_success_url(self):
        return reverse('questions-list')

    def get_context_data(self, **kwargs):

        context = super(CreateQuestionView, self).get_context_data(**kwargs)
        context['action'] = reverse('questions-new')
        return context

class UpdateQuestionView(generic.UpdateView):

    model = Question
    template_name = 'edit_question.html'
    form_class = forms.QuestionForm

    def get_success_url(self):
        return reverse('questions-list')

    def get_context_data(self, **kwargs):

        context = super(UpdateQuestionView, self).get_context_data(**kwargs)
        context['action'] = reverse('questions-edit',
                                    kwargs={'pk': self.get_object().id})
        return context

class DeleteQuestionView(generic.DeleteView):

    model = Question
    template_name = 'delete_question.html'

    def get_success_url(self):
        return reverse('questions-list')

class QuestionView( generic.DetailView):
    model = Question
    template_name = 'question.html'
    form_class = forms.QuestionRadioForm

class ListChoiceView(generic.ListView):
    model = Choice
    template_name = 'choice_list.html'

class CreateChoiceView(generic.CreateView):

    model = Choice
    template_name = 'edit_choice.html'
    form_class = forms.ChoiceForm

    def get_success_url(self):
        return reverse('choices-list')

    def get_context_data(self, **kwargs):

        context = super(CreateChoiceView, self).get_context_data(**kwargs)
        context['action'] = reverse('choices-new')

        return context

class UpdateChoiceView(generic.UpdateView):

    model = Choice
    template_name = 'edit_choice.html'
    form_class = forms.ChoiceForm

    def get_success_url(self):
        return reverse('choices-list')

    def get_context_data(self, **kwargs):

        context = super(UpdateChoiceView, self).get_context_data(**kwargs)
        context['action'] = reverse('choices-edit',
                                    kwargs={'pk': self.get_object().id})
        return context

class DeleteChoiceView(generic.DeleteView):

    model = Choice
    template_name = 'delete_choice.html'

    def get_success_url(self):
        return reverse('choices-list')

class ChoiceView(generic.DetailView):

    model = Choice
    template_name = 'question.html'

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    user = get_object_or_404(Contact, pk=1)
    try:
        selected_option = p.option_set.get(pk=request.POST['option'])
        user.score += 1;
        user.save()

    except (KeyError, Option.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
        'poll': p,
        'error_message': "You didn't select a option.",
    })
    else:
        selected_option.votes += 1
        selected_option.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(p.id,)))

class DialogIndexView(generic.ListView):

    template_name = 'questions/dialog.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """
        Return the last five published polls (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=datetime.datetime.now()).order_by('-pub_date')[:1]

class QuizIndexView(generic.ListView):

    template_name = 'questions/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """
        Return the last five published polls (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=datetime.datetime.now()).order_by('-pub_date')[:1]

class QuizListView(generic.ListView):

    template_name = 'questions/index2.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """
        Return the last five published polls (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=datetime.datetime.now()).order_by('-pub_date')[:5]

class QuizDetailView(generic.DetailView):
    model = Question
    template_name = 'questions/detail.html'
    def get_queryset(self):
        """
        Excludes any polls that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=datetime.datetime.now())

class QuizResultsView(generic.DetailView):
    model = Question
    template_name = 'questions/results.html'

def json_view(request, self):
    user = get_object_or_404(Contact, pk=self.request.user)
    statistics = get_list_or_404(ScoreStatistics, user=user.id)
    val = []
    for score in statistics[0:len(statistics)-1]:
        val.append({ 'id':  score.id , 'score': score.score , 'date': str(score.execution_date)})

    #val = val + "{ id: \'"+ str(statistics[len(statistics)-1].id) +"\', score:\'"+ str(statistics[len(statistics)-1].score) +"\', date: \'"+ str(statistics[len(statistics)-1].execution_date) +"\'}]"
    #val = [{ "date": "2015-05-01 05:28:23", "score": 0 }, { "date": "2015-05-05 05:28:23", "score": 1 },{ "date": "2015-05-10 05:28:23", "score": 2 }, { "date": "2015-05-15 05:28:23", "score": 3 } ]
    #val = user.get_scoresetJson
    return HttpResponse(simplejson.dumps(val), mimetype='application/json')

class QuizScoreView(generic.DetailView):
    model = Contact
    template_name = 'questions/quiz_result.html'

def answer(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    answeredQuestionList = get_list_or_404(ScoreStatistics, user=1)
    user = get_object_or_404(Contact, pk=1)
#
    user.running = True;#

    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
        n = int(question_id) + 1;
        user.numberOfAskedQuestion += 1
        user.save()

        if user.numberOfAskedQuestion == 1 :
            score = ScoreStatistics.create(user)
            score.save()
            user.previous_score = score.id
            user.save()

        if user.numberOfAskedQuestion == 10 :
            get_object_or_404(ScoreStatistics, pk = user.previous_score)
            #user.previous_score = user.score

            user.numberOfAskedQuestion = 0
            user.running = False

            score = get_object_or_404(ScoreStatistics, pk = user.previous_score)
            score.score = user.score

            user.previous_score = user.score
            user.score = 0
            user.save()
            score.save()
            return HttpResponseRedirect(reverse('quiz_score_view', args=(user.id,score.id)))

        if selected_choice.results == 1 :
            user.score += 1
            user.save()

            return render(request, 'questions/detail.html', {
            'question': get_object_or_404(Question, pk = n  ),
            'error_message': "Correct !!! :)",})

        else:
            score = get_object_or_404(ScoreStatistics, pk = user.previous_score)
            score.wrong_answers = score.wrong_answers + question_id + "; "
            #user.previous_score = score.id
            user.save()
            score.save()
            return render(request, 'questions/detail.html', {
            'question': get_object_or_404(Question, pk = n ),
            'error_message': "Wrong",
        })

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'questions/detail.html', {
        'question': p,
        'error_message': "You didn't select a choice, try your answer.",
    })
    else:

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('quiz_results', args=(p.id,)))