from datacenter.models import Mark
from datacenter.models import Schoolkid
from datacenter.models import Commendation
from datacenter.models import Lesson
from datacenter.models import Subject
from datacenter.models import Chastisement
from random import choice


def fix_marks(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.DoesNotExist:
        print("Ученик с таким именем не найдем")
        return
    except Schoolkid.MultipleObjectsReturned:
        print("Уточните имя")
        return
    min_good_mark = 4
    bad_marks = Mark.objects.filter(schoolkid=schoolkid,
                                    points__lt=min_good_mark)
    for mark in bad_marks:
        mark.points = 5
        mark.save()
    print("Оценки исправлены")


def delete_chastisement(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.DoesNotExist:
        print("Ученик с таким именем не найдем")
        return
    except Schoolkid.MultipleObjectsReturned:
        print("Уточните имя")
        return
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    for chastisement in chastisements:
        chastisement.delete()


def create_commendation(schoolkid_name, subject_name):
    possible_commends = ["Молодец!", "Отлично!",
                         "Хорошо!", "Очень хороший ответ!",
                         "Замечательно!", "Так держать!"]
    commend = choice(possible_commends)
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.DoesNotExist:
        print("Ученик с таким именем не найдем")
        return
    except Schoolkid.MultipleObjectsReturned:
        print("Уточните имя")
        return
    year = schoolkid.year_of_study
    letter = schoolkid.group_letter
    try:
        subject = Subject.objects.get(title=subject_name, year_of_study=year)
    except Subject.DoesNotExist:
        print("Такого предмета не найдено")
        return
    lessons = Lesson.objects.filter(subject=subject,
                                    year_of_study=year,
                                    group_letter=letter).order_by("date")
    last_lesson = lessons.last()
    Commendation.objects.create(text=commend, created=last_lesson.date,
                                schoolkid=schoolkid, subject=subject,
                                teacher=last_lesson.teacher)
