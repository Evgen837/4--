# -*- coding: utf-8 -*-

# # Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно.
# # Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.
#
# def sum_range(start, end):
#     if start > end:
#         start, end = end, start
#     return sum(range(start, end+1))
#
# print(sum_range(2, 10))



# # Создайте функцию three_args(), которая принимает 1, 2 или 3 строго ключевых параметра.
# # В результате ее работы на печать в консоль выводятся значения переданных переменных, но только если они не равны None.
# # Получим, например, следующее сообщение: «Переданы аргументы: var1 = 2, var3 = 10».
#
# def three_args(*, var1, var2=None, var3=None):
#     arguments = ', '.join([f'{arg[0]} = {str(arg[1])}' for arg in locals().items() if arg[1] is not None])
#     print(f'Переданы аргументы: {arguments}')
#
# three_args(var1=21)
# three_args(var1='Python', var3=3)
# three_args(var1='Python', var2=3, var3=9)



# # показать текущее время с сообщением.
# from datetime import datetime
# from time import sleep
#
# def time_now(msg, *, dt=None):
#     dt = dt or datetime.now()
#     print(msg, dt)
# #тесты
# time_now('Сейчас такое время: ')
# sleep(1)
# time_now('Прошла секунда: ')
# sleep(1)
# time_now('Задам-ка другую дату: ', dt='2022-01-11 11:00:10')





# # 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# # Функция должна принимать параметры:
# # - точка начала рисования,
# # - угол рисования,
# # - длина ветвей,
# # Отклонение ветвей от угла рисования принять 30 градусов,
#
# # 2 )Сделать draw_branches рекурсивной
# # - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# # - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
# #   с углом рисования равным углу ветви,
# #   длиной ветви меньшей чем длина ветви с коэффициентом 0.75
#
# # 3) первоначальный вызов:
# # root_point = get_point(300, 30)
# # draw_bunches(start_point=root_point, angle=90, length=100)
#
# import simple_draw as sd
#
# def branch(point, angle, length, width):
#     if length < 2:
#         return
#
#     if length < 10:
#         width = 1
#     elif length < 70:
#         width = 3
#     else:
#         width = 5
#
#     if length < 10:
#         color = sd.COLOR_BLUE
#     else:
#         color = sd.COLOR_DARK_BLUE
#
#     vector = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
#     vector.draw(color=color)
#     point_2 = vector.end_point
#     angle_2 = angle - 27
#     length_2 = length * .72
#     branch(point=point_2, angle=angle_2, length=length_2, width=width)
#     angle_3 = angle + 27
#     branch(point=point_2, angle=angle_3, length=length_2, width=width)
#
# sd.pause()










