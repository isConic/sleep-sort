import asyncio

def __adjust_sleep(t):
    """Modifier to scale down seconds

    Args:
        t: seconds of sleep

    Returns:
        An adjusted time for sleep sort.
        For example 5 seconds can easily become .0005 seconds.
    """
    return float(t) / float(10000)

async def __sleep(delay, f= __adjust_sleep):
    """Asychronous sleep function wrapper

    Args:
        delay: number of seconds intended for the sleep.
        f:     a function to modify delay amount.

    Returns:
        'delay' after having slept f(delay) seconds.
    """

    await asyncio.sleep(f(delay))
    return delay

async def __sleep_sort(values):
    """Sorts using asycio sleep function

    Args:
        values: list of ints or floats

    Returns:
        A list of ints or floats sorted from least to greatest.
    """
    snoozes = [__sleep(duration) for duration in values]

    woke_values = []
    for value in asyncio.as_completed(snoozes):
        woke_values.append(await value)

    return woke_values


def sleep_sort(list_of_values):
    """Sorts using asycio sleep function

    Args:
        list_of_values: list of ints or floats

    Returns:
        A list of ints or floats sorted from least to greatest.
    """
    return asyncio.run(__sleep_sort(list_of_values))