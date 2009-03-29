from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

class HasOwner(object):
    """
    If a model's objects are potentially "owned" by a user (or multiple users),
    the model's class should inherit from this class and implement is_owned_by.
    """
    def is_owned_by(self, user):
        """
        Abstract method for determining if a given user owns a given object.
        """
        klass = self.__class__.__name__
        raise NotImplementedError, "method not overridden for class " + klass

    @classmethod
    def get_mine(klass, user, *args, **kargs):
        """
        Utility function to check for existance and ownership of an object and
        return it or raise either a 404 or PermissionDenied error.
        """
        object = get_object_or_404(klass, *args, **kargs)
        if not object.is_owned_by(user):
            raise PermissionDenied
        return object
