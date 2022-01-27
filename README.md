# Функции для работы с бд в shell

Функции для работы с бд [электронного дневника](https://github.com/devmanorg/e-diary/tree/master) в shell.
В коментариях перед каждой из функций указаны команды для импорта нужных классов и функций сторонних библиотек

## Описание Функций

- fix_marks - получает на вход имя ученика и исправляет все его плохие оценки на 5ки. Требует импорта классов:
  ```
  from datacenter.models import Mark
  from datacenter.models import Schoolkid
  ```
&nbsp;

- delete_chastisement - получает на вход имя ученика и удаляет все его замечания. Требует импорта классов:

  ```
  from datacenter.models import Chastisement
  from datacenter.models import Schoolkid
  ```

&nbsp;

  - create_commendation - получает на вход имя ученика с предметом и добавляет к последнему уроку по этому предмету похвалу с одним из возможных текстов. Требует импорта классов и функции:

  ```
  from datacenter.models import Commendation
  from datacenter.models import Schoolkid
  from datacenter.models import Lesson
  from datacenter.models import Subject
  from random import choice
  ```


## Цели проекта

Код написан в целях тренировки работы с shell
