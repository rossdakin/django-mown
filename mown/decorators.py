def assert_my_object_exists(klass, key_param='pk', key_field='pk'):
    """
    Decorator for making sure that the object with the given key exists and
    belongs to request.user

    Required arguments:
     * klass: the model class of which the desired object is an instance

    Optional arguments:
     * key_param: the name of the view function parameter to use as a get() key
                  DEFAULT: 'pk'
     * key_field: the name of the model's attribute to which the key_param maps
                  DEFAULT: 'pk'

    Examples:

    @my_object_exists(Foo)
    def foo_details(request, pk):
        ...
    @my_object_exists(Bar, key_param='object_id', key_field='id')
    def edit_bar(request, baz=None, object_id):
        ...
    """
    def decorator(view_function):
        def wrapper(request, *args, **kwargs):
            key = kwargs[key_param]
            filter = { key_field: key }
            klass.get_mine(user=request.user, **filter)
            return view_function(request, *args, **kwargs)
        return wrapper
    return decorator
