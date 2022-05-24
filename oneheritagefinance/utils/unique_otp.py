import random
import string

from .unique_slug_generator import unique_slug_generator


def random_integer_generator(size=36, chars=string.digits):
    return "".join(random.choice(chars) for _ in range(size))


def unique_online_pin_generator(instance, new_pin=None):
    """
    This is for a Django project with a pin charfield
    """
    if new_pin is not None:
        pin = new_pin
    else:
        pin = random_integer_generator(size=4)

    Klass = instance.__class__
    # return Klass.objects.filter(user=instance.user, currency=instance.currency).update(
    #     pin=pin
    # )
    # return unique_online_pin_generator(
    #     instance,
    #     new_pin=pin
    # )
    return pin

def unique_acc_no(instance, new_acc_no=None):
    """
    This is for a Django project with an acc_no field
    """
    size = random.randint(7, 14)
    if new_acc_no is not None:
        acc_no = new_acc_no
    else:
        acc_no = "234{acno}".format(acno=random_integer_generator(size=size))

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(
        acc_no=acc_no, currency=instance.currency, user=instance.user
    ).exists()
    if qs_exists:
        return unique_acc_no(
            instance,
            new_acc_no="234{acno}".format(acno=random_integer_generator(size=size)),
        )
    return acc_no
