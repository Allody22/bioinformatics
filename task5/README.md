# Домашнее задание 5. Предсказание и парное выравнивание структур белков


## 1. Общая информация

**Мой инструмент 1 фолдинга белков:** RoseTTAFold2 (https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/RoseTTAFold2.ipynb)  
**Мой инструмент 2 фолдинга белков:** AlphaFold2 (https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb)
**Моя последовательность:** MKGMLTGPVTILNWSWPREDITHEEQTKQLALAIRDEVLDLEAAGIKIIQIDEAALREKLPLRKSDWHAKYLDWAIPAFRLVHSAVKPTTQIHTHMCYSE  
**Мой инструмент парного выравнения:** jCE (в списке Alignment Method)  

## 2. Работа в google collab

Файлы ipynb расположены в папке colab.  
Самое главное на этом шаге поставить в коллабе правильную среду выполнения:
1) Среда выполнения
2) сменить среду выполнения
3) ставить вариант с GPU, иначе придётся ждать миллион лет.

## 3. Предсказания
Все результаты для каждого из этих инструментов находят в соответствующих папках в task5 (этой папке).  
То есть для AlphaFold2 идёт папка alphaFold2, а для RoseTTAFold2 идёт roseTTAFold2 со всеми файлами, которые мне выдали программы.  
Главные pdb файлы можно найти в папке pairwise - их я и буду использовать для выравнивания.

## 4. Полная выдача программы
Результаты работы RCSB с моими файлами находятся в папке pairwise/result.  
Туда я также приложил скриншот самого интерфейса.  
Можно даже [ссылку](https://www.rcsb.org/alignment?request-body=eJylkc1u2zAQhN%2BFZ8uiLMsudctzFAGxEpeWUP5lSTVODb97l06AHnoIgpwkzVDLb2Zv4mVDehPjTcRU1hhyfSUsGwWdkc0wozZQQIyFNrzvxBxDwWup53w0KEaRYKXXNaPYCY9liaZ6AXz15qomIP4qSI%2FpF0jaw1Xn9Q%2Bf6OXuocSEYQ0XzQ9whYmGd52vwpCZ7J8j9%2BxZgovHUD7G%2FNgJ8tnoshDmJTpm6BmHr%2BFculpiVOrO%2FJlzzJwPGebnTWzkGHMpJeWxbbeM1GzJRTB7mvO0j3Rpf3etia%2Bhiu3QyYNSp66REqE5SjM1akDZDFb1cJrMyaipJXvg8tBILaVOhGY%2FzavlImwkD1yd8P5d%2BGjp%2Fx%2BSmdjO6HCua6m9QX7zeuUc4klwkC%2Bj93juVHfGxho7N0cDXTPJ89T0R2XOJ%2BzR4rEtmAtDzLbXWyB0cEWjCcIvFjsNLi1gud2DTsXrun%2Bnhwc6%2B%2FKzmN8b%2Fmklz3W9dnWPzT7f%2FwKGEPqW&response-body=eJzVVNtu2zgQ%2FRc9S%2FaQFEXSb0btjQ3Lu44tJCiKQqBF2hFWF1eXtEGQf%2B9QTpr0gu62eaoEAeJczswZHvLey6tD7U3uvb7PjTfxtKFg7YEGmQUThBHIQCvgwT4SYPcEnyjyfK%2FtdNe3GP%2Fmn%2FUmnidz78H3SttpB6WL%2FFiVturSsjYWg046bz7mrcXEFz7b3dSuZGZdcmPbvugQ8t09ojd91vVoGpZ9U2DYTded2sl43Le2CfpTUWszarJ2P6qb4%2FiWjE39sXLGMYA1hmT7QEmKFBSSUcBEANIAtyIEpcNxc6Bpa62BFCA9NdaM9ll%2BwAYPdVPqDuuV5dmQt%2Bk%2Br3Rz502wLet7lS4dqe8RTmbvRmMLm3V5XQ2jaO%2FKdBjs1Ht48H%2BZi1AMMnwCajUJQtyAQFEpA3oAbQ7GgMqycWfbDpvIDiztq8YW%2BpM1aaOrf9FIUl2cbvShLgxNT105bEmR8qF19MMv835dtf%2Bc0Xv%2FefvTL2oZdNDYI6Y4Tbz7Osv39vaINT4MBnJe5pWxn7wJ%2BF5hq2N3gw4AhH9FLvbWIdP2PKunXogPj%2B8P%2F7AijIgikrMQqAgV5yHzAxgpRpWUoZIgqaI0dDYGIQfBInQB2hRzGKNQSMkIoRGNFCJIF0kkIhIhFAVKeIhRkksZcZQHEwQEdy0EzhpFUlAmWQSEcTpUIcAlUzzkknPKuXA1COJx4BApwdhjMgIrhAylYkiAAPYtRkIIRjnFq4EwgV3TEQcmwxCrRkgvikIk7baxL8tBPnigs%2FrpMN%2FqokcZYUGJ07w7OUlt17uZ507Hk%2FOLp83LvNBN3t0FA4bn9FGhLqoUAXPT29RdLu15gwbx2A%2B9rbJvtfNkRsz16mIdJxebq2QZ%2F329u95s57NlspjPL5PVZTyNp8vtbH4Vz%2BL5dHqxXC2Xl8sZ%2Fsbb%2BSrexNvVbna9mK7exrPr6XIz%2FWsbXy1206vVJkkul4tksX7zdjf3%2FBdq%2FX3BuZn8oZ2%2FSgDkWQCP7INnJbwMxCOBIv2JXH6KmRuUxzeIeC6f%2B0rW%2F0N2zjPcc%2B4ePHsdU%2BfB7yzJIRUH9JjgVll9axt9tC9CUcAPnwGjCVfU&encoded=true) сгенерировать, но сайт написал, что она скоро сгорит.  

## 5 и 6. Визуализация и видео
RCSB позволяет сделать сразу видео, в папке pairwise/result лежит файл rcsb_render.mp4  
Также геометрическая модель в бинарном формате в той же папке molstar-model.glb  
И изображение molstar-image.png  
Вообще этот в интерфейсе можно просто выбирать элемент, а затем цвет, который мы хотим к нему применить, у меня вот автоматически выставился синий и оранжевый.

## 7. Выводы
RCSB пишет выводы по таким критериям:
1) RMSD = 0.48 (root-mean-square deviation).  
Это показывает, насколько сильно различаются структуры.  
Моё значение указывает на то, что различие между структурами минимально. Это очень хорошая степень совпадения.
2) TM-score = 0.98 (Template Modeling score)  
Это метрика, которая оценивает степень схожести двух структур. Чем ближе к 1, тем больше совпадений в топологии.  
В моём случае значение очень-очень близкое к 1, то есть структура очень похожа на другую
3) Identity 100%  
Полное сходство между предсказаниями.

Выравнивание отлично сработало и выдало очень качественные значения.