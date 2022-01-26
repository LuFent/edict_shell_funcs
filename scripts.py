"""
from datacenter.models import Mark
from datacenter.models import Schoolkid
"""
def fix_marks(schoolkid):
    min_good_mark = 4
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=min_good_mark)
    for mark in bad_marks:
        mark.points = 5
        mark.save()


"""
from datacenter.models import Chastisement
from datacenter.models import Schoolkid
"""
def delete_chastisement(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    for chastisement in chastisements:
        chastisement.delete()


"""
from datacenter.models import Commendation
from datacenter.models import Schoolkid
from datacenter.models import Lesson
from datacenter.models import Subject
from random import choice
"""
def create_commendation(schoolkid_name, subject_name):
    possible_commends = ["Молодец!", "Отлично!", "Хорошо!", "Очень хороший ответ!", "Замечательно!", "Так держать!"]
    commend = choice(possible_commends)
    schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    year = schoolkid.year_of_study
    letter = schoolkid.group_letter
    subject = Subject.objects.get(title=subject_name, year_of_study=year)
    lessons = Lesson.objects.filter(subject=subject,  year_of_study=year, group_letter=letter).order_by("date")
    last_lesson = lessons.last()
    Commendation.objects.create(text=commend, created=last_lesson.date, schoolkid=schoolkid, subject=subject,
                                teacher=some_lesson.teacher)
