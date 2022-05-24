

Ex().multi(
    check_object("sales_1_1"),
    check_object("sales_1_1").check_keys("cum_weekly_sales").has_equal_value(),
    check_function(
        name='sales_1_1.sort_values',
        index=0,
        signature=sig_from_obj('pandas.core.frame.DataFrame')
    ).check_args(0).has_equal_value(),

    check_object("sales_1_1").check_keys("cum_max_sales").has_equal_value(),
    check_function(
        name='sales_1_1.cumsum',
        index=0,
        signature=sig_from_obj('pandas.core.frame.DataFrame')
    ),

    check_function(
        name='sales_1_1.cummax',
        index=0,
        signature=sig_from_obj('pandas.core.frame.DataFrame')
    ),
    check_function("print", 0).check_args(0).has_equal_value(),

)



success_msg(
    """ Вы добились успеха! Не все функции, которые вычисляют по столбцам, возвращают одно число. 
        Некоторые, например функции кумулятивной статистики, возвращают целый столбец."""
)
