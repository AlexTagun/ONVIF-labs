# ONVIF-labs

##Краткий обзор
Версия Python 2.7.15rc1
Тесты выколнялись на трех камерах:
42 (порт 80)
43 (порт 80)
53 (порт 2000)

##Подключение к камере и знакомство с возможностями/ограничениями PTZ
Файл с программой:
    GettingCamData.py

Коментарий:
Он выполняет все 3 пункта задания. Подключается к камере, выдает текущие координаты, показывает поддержку absolute move (True или False), a также значение фокуса и его поддержку его регулировки

##Absolute move: диагностика и перемещение
Файл с программой:
    task2.py

Коментарий:
Печатает текущие координаты, перемещается в позицию (0.1, 0.5), затем снова печетат координаты после перемещения

##Программа перемещения камеры в Continuous move
Файл с программой:
    task3.py

Коментарий:
Программа печатает текущую позицию камеры для удобства

##Программа ручного фокуса
