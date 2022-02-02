import string
from typing import Union

from django.utils import timezone
from humanfriendly import format_timespan


class measure_time:
    """
    Class, used as a context manager, to measure the time spent within the context.

    After exiting this context, the object variable `total_seconds` contains the spent time in seconds.

    Typical usage:

    with measure_time() as t:
        do_something_lengthy()
    print(f'The operation took {t.total_seconds} seconds to complete')
    """

    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = timezone.now()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = timezone.now()

    def __str__(self) -> str:
        """
        Return the measured time in a human readable format

        Output under 24 hours: 0:01:30
        Output over 24 hours:  7 days, 10:13:56
        """

        return format_timespan(self.total_seconds, max_units=2)

    @property
    def total_seconds(self) -> float:
        """
        Return the time spent since entering the context manager in seconds
        """

        if self.start_time is None:
            raise ValueError('Not started yet')
        end_time = self.end_time or timezone.now()
        return (end_time - self.start_time).total_seconds()


def parse_float(number: Union[str, int, float]) -> float:
    """
    Convert the input string that represents a number to a Decimal with N decimal places

    >>> parse_float('€4.-')
    4.0
    """

    try:
        if isinstance(number, str):
            thousands_separator = ','
            decimal_separator = '.'
            if ',' in number:
                if '.' not in number or ('.' in number and number.index('.') < number.index(',')):
                    # When there are both thousands and decimal separators in use, we assume that
                    # the first one is the thousands separator and the second one the decimal separator
                    thousands_separator = '.'
                    decimal_separator = ','

            number = number.replace(thousands_separator, '')

            # If there are multiple decimal separators present, we assume they are actually a thousands separator
            if number.count(decimal_separator) > 1:
                number = number.replace(decimal_separator, '')

            # Ensure that the number passed to float() uses a period as decimal separator
            number = number.replace(decimal_separator, '.')

        try:
            number = float(number)
        except ValueError:
            # It could be that there are other characters around the decimal, e.g. currency symbols
            # First, strip all non-digit or separator characters from the string. We try again after
            # stripping all non-digit related characters. We cannot do this immediately, since the
            # original text might have been valid with these characters, e.g. 8.7E12 or -13.
            number = float(''.join(char for char in number if char in string.digits + '.'))

        return number

    except Exception as e:
        exception_class = type(e)
        msg = f"Cannot convert '{number}' to float"
        raise exception_class(msg) from e
