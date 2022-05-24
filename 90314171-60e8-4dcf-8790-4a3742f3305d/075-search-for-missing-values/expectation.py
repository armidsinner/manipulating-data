

Ex().multi(
    has_import("matplotlib.pyplot", same_as=True),
    check_function('apples_2016.isna', signature="").has_equal_value(),
    check_function('print', 0).has_equal_value(),

    check_function('apples_2016.isna.any', signature="").has_equal_value(),
    check_function('print', 1).has_equal_value(),

    check_function('apples_2016.isna.sum.plot', signature="").check_args(0).has_equal_value(),
    check_function('matplotlib.pyplot.show', 0, signature=False).has_equal_value(),
)


success_msg(
    """ Чудесное обнаружение недостающих значений! Похоже, что в столбцах small_sold, 
        large_sold и xl_sold отсутствуют значения."""
)
