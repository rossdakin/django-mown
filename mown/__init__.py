"""
MOWN - Model OWNership

This app provides a class for models to inherit from if they have the notion
of ownership (e.g. a Book belongs to a user).

The path of ownership between user and object is entirely up to you; simply
override is_owned_by() in your model to define "ownership" however you want.

A class method get_mine() is provided to models inheriting from HasOwner.
This method is intended to replicate the behavior of the standard model manager
get() method, with two differences:
 * if the object does not exist, Http404 is raised
 * if the specified user does not own the object, PermissionDenied is raised

Also provided is a view decorator that has the same behavior as get_mine()
but takes a model class as a parameter. This is useful for ensuring that an
object is owned by the current user before a view is even run.
"""
