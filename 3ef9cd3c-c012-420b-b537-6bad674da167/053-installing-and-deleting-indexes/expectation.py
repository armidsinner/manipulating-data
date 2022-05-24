

Ex().multi(
    check_function("print", 0).check_args(0).has_equal_ast(),

    check_function('temperatures.set_index', 0, signature=False).multi(
        check_args(0).has_equal_value(),
    ).has_equal_value(),

    check_object("temperatures_ind").has_equal_ast(),
    check_function("print", 1).check_args(0).has_equal_ast(),

    check_function("print", 2).check_correct(
        check_args(0).has_equal_value(),
        check_function("temperatures_ind.reset_index", signature=False),
    ),
    check_function("print", 3).check_correct(
        check_args(0).has_equal_value(),
        check_function("temperatures_ind.reset_index", signature=False).check_args(0).has_equal_value(),
    )
)


success_msg(
    """ Невероятно! Установка индекса позволяет использовать более сжатый 
        код для создания выборки строк с помощью .loc[]."""
)
