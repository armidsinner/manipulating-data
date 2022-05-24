

Ex().multi(
    check_function('apples.plot', 0, signature=False).multi(
        check_args(0).has_equal_value(),
        check_args(1).has_equal_value(),
        check_args(2).has_equal_value(),
        check_args(3).has_equal_value(),
    ),


    check_function('matplotlib.pyplot.show', 0, signature=False).has_equal_value(),
)


success_msg(
    """ Супер! Похоже, что когда продается больше яблок, цены снижаются. Однако это не означает, 
        что меньшее количество продаж приводит к повышению цен - мы можем только сказать, 
        что они коррелируют друг с другом."""
)
