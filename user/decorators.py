from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from functools import wraps
from django.utils.decorators import available_attrs



def user_passes_test():
    """
    Decorator for views that checks that the user passes the given test,
    redirecting to the log-in page if necessary. The test should be a callable
    that takes the user object and returns True if the user passes.
    """

    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
             # Do some stuff
            if request.user.is_authenticated() and request.user.is_seller:
                return view_func(request, *args, **kwargs)
            else:
                messages.warning(request, "Access limited to designers")
                return HttpResponseRedirect(reverse('home'))
        return _wrapped_view
    return decorator


def designer_required(function=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test()
    if function:
        return actual_decorator(function)
    return actual_decorator