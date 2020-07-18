import datetime
import math
import re
from django.utils.html import strip_tags


def symbols_quantity(html_string):
    word_string = strip_tags(html_string)
    matching_words = re.findall(r'\w+', word_string)
    count = len(matching_words)
    return count


def get_reading_time(html_string):
    count = symbols_quantity(html_string)
    read_time_min = math.ceil(count/100.0)
    return int(read_time_min)
