from django.utils import timezone

def Time_format(time):
    time_format = time.strftime("%y-%m-%d %H-%M-%S")
    return time_format