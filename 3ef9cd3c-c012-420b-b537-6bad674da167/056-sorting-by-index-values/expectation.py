

Ex().multi(


    check_function('temperatures_ind.sort_index', 0, signature=False).has_equal_value(),

    check_function("print", 0).check_args(0).has_equal_ast(),

    check_function('temperatures_ind.sort_index', 1, signature=False).multi(
        check_args(0).has_equal_value(),
    ).has_equal_value(),
    check_function("print", 1).check_args(0).has_equal_ast(),

    check_function('temperatures_ind.sort_index', 2, signature=False).multi(
        check_args(0).has_equal_value(),
        check_args(1).has_equal_value(),
    ).has_equal_value(),
    check_function("print", 2).check_args(0).has_equal_ast(),
)


success_msg(
    """ Разобрались! Сортировка значений индекса аналогична сортировке значений в столбцах, 
        используя .sort_index() вместо .sort_values()."""
)
