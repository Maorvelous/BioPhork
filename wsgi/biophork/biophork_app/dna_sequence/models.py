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

