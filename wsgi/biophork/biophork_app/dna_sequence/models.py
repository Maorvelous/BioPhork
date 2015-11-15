from django.db import models
from django.core.urlresolvers import reverse
import datetime
import json

class Contact(models.Model):

    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,
    )
    email = models.EmailField()
    password = models.CharField(max_length=50)
    score = models.IntegerField(default=0)
    rank = models.IntegerField(default=-25)
    previous_score = models.IntegerField(default=0)
    best_score = models.IntegerField(default=0)
    numberOfAskedQuestion = models.IntegerField(default=0)
    running = models.BooleanField(default=False)


    def __str__(self):

        return ' '.join([
            self.first_name,
            self.last_name,
        ])

    def get_absolute_url(self):
        return reverse('contacts-view', kwargs={'pk': self.id})

    def get_scoreset(self):
        score_set = ScoreStatistics.objects.filter(user = self.id)
        #val = val + "{\"id\":" + str(score.id) +",\"score\":"+ str(score.score) + ",\"date\":"+ str(score.execution_date) +"},"
        val = '['
        #val =''
        for score in score_set[0:len(score_set)-1]:
                val = val + "{ id: \'"+ str(score.id) +"\', score:\'"+ str(score.score) +"\', date: \'"+ str(score.execution_date) +"\'},"
        val = val + "{ id: \'"+ str(score_set[len(score_set)-1].id) +"\', score:\'"+ str(score_set[len(score_set)-1].score) +"\', date: \'"+ str(score_set[len(score_set)-1].execution_date) +"\'}]"

        val = json.dumps(val)
        return ''.join([
            val,
        ])

    def get_scoresetJson(self):
        to_json = {
        "key1": "value1",
        "key2": "value2"
        }

        val = [{ "date": "2015-05-01 05:28:23", "score": 0 }, { "date": "2015-05-05 05:28:23", "score": 1 },{ "date": "2015-05-10 05:28:23", "score": 2 }, { "date": "2015-05-15 05:28:23", "score": 3 } ]
        #val = [{ date: 2015-05-01 05:28:23, score: 0 }, { date: 2015-05-05 05:28:23, score: 1 },{ date: 2015-05-10 05:28:23, score: 2 }, { date: 2015-05-15 05:28:23, score: 3 } ]

        val = json.dumps(val)

        return to_json

    def get_scoreset_extra(self):
        #val = val + "{ id: \'"+ str(score_set[len(score_set)-1].id) +"\', score:\'"+ str(score_set[len(score_set)-1].score) +"\', date: \'"+ str(score_set[len(score_set)-1].execution_date), +"\', wrong_answers: \'"+ str(score_set[len(score_set)-1].wrong_answers) +"\'}]"
        score_set = ScoreStatistics.objects.filter(user = self.id)
        #val = val + "{\"id\":" + str(score.id) +",\"score\":"+ str(score.score) + ",\"date\":"+ str(score.execution_date) +"},"
        val = '['
        #val =''
        for score in score_set[0:len(score_set)-1]:
                val = val + "{ id: \'"+ str(score.id) +"\', score:\'"+ str(score.score) +"\', date: \'"+ str(score.execution_date) +"\', wrong_answers: \'"+ str(score_set[len(score_set)-1].wrong_answers) +"\'}"
        val = val + "{ id: \'"+ str(score_set[len(score_set)-1].id) +"\', score:\'"+ str(score_set[len(score_set)-1].score) +"\', date: \'"+ str(score_set[len(score_set)-1].execution_date) +"\', wrong_answers: \'"+ str(score_set[len(score_set)-1].wrong_answers) +"\'}]"

        val = json.dumps(val)
        return ''.join([
            val,
        ])

class Address(models.Model):

    contact = models.ForeignKey(Contact)
    address_type = models.CharField(
        max_length=10,
    )

    address = models.CharField(
        max_length=255,
    )

    def __str__(self):

        return ' '.join([
            self.city,
            self.state,
        ])

    def get_absolute_url(self):
        return reverse('contacts-view', kwargs={'pk': self.id})

    city = models.CharField(
        max_length=255,
    )
    state = models.CharField(
        max_length=2,
    )
    postal_code = models.CharField(
        max_length=20,
    )

    class Meta:
        unique_together = ('contact', 'address_type',)

class Poll(models.Model):

    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self): # Python 3: def __str__(self):
        return self.question

    def was_published_recently(self):
        now = datetime.datetime.now()
        return now - datetime.timedelta(days=1) <= self.pub_date < now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Option(models.Model):
    poll = models.ForeignKey(Poll)
    option_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self): # Python 3: def __str__(self):
        return self.option_text


class Question(models.Model):
    #scores = models.ManyToManyField(Contact)
    pub_date = models.DateTimeField('date published',auto_now_add=True, blank=True)
    question_type = models.CharField(
        max_length=30,
    )

    content =  models.CharField(
        max_length=255,
    )

    question = models.CharField(max_length=200)

    def __unicode__(self): # Python 3: def __str__(self):
        return self.question

    def was_published_recently(self):
        now = datetime.datetime.now()
        return now - datetime.timedelta(days=1) <= self.pub_date < now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def get_absolute_url(self):
        return reverse('questions-view', kwargs={'pk': self.id})

    def get_next(self):
        return reverse('questions-view', kwargs={'pk': (self.id + 1)})

    answer =  models.PositiveSmallIntegerField(default=0)

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    results = models.IntegerField(default=0)

    def __unicode__(self):
        return ' '.join([self.choice_text])

class ScoreStatistics(models.Model):
    user = models.ForeignKey(Contact)
    execution_date = models.DateTimeField('date published',auto_now_add=True, blank=True)
    score = models.IntegerField(default=0)
    wrong_answers = models.CharField(max_length=20000)

    def __unicode__(self): # Python 3: def __str__(self):
        return self.user

    def __str__(self):

        return ' '.join([
            self.execution_date,
            self.score,
            self.wrong_answers
        ])

    @classmethod
    def create(cls, user):
        score = cls(user=user)
        # do something with the book
        return score