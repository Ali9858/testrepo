import time

# получаем 0 секунд от начала эпохи
epoch_seconds = 0.0

# преобразуем 0 секунд в человекочитаемую дату
epoch_time = time.gmtime(epoch_seconds)

print "Эпоха начинается с даты:"
print epoch_time
