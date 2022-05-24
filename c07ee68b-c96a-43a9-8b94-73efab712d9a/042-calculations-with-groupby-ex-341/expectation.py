

Ex().multi(
    check_function(
        name='sales.groupby',
        index=0,
        signature=sig_from_obj('pandas.core.frame.DataFrame')
    ).check_args(0).has_equal_value(),

    check_function(
        name='sales.groupby.sum',
        index=0,
        signature=sig_from_obj('pandas.core.frame.DataFrame')
    ),
    check_object("sales_by_type").has_equal_ast(),

    check_function(
        name='sales.groupby',
        index=1,
        signature=sig_from_obj('pandas.core.frame.DataFrame')
    ).check_args(0).has_equal_value(),

    check_function(
        name='sales.groupby.sum',
        index=1,
        signature=sig_from_obj('pandas.core.frame.DataFrame')
    ),
    check_object("sales_by_type_is_holiday").has_equal_ast(),
    check_object("sales_by_type").has_equal_value(),
    check_object("sales_by_type_is_holiday").has_equal_value(),
    check_function("print", 0).check_args(0).has_equal_value()
)

success_msg(
    """ Отличная группировка! Вы смогли выполнить те же вычисления, 
        что и в предыдущем упражнении, написав при этом гораздо меньше кода. """
)
