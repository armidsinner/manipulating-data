

Ex().multi(

    check_function(
        name='store_types.value_counts',
        index=0,
        signature=sig_from_obj('pandas.core.frame.DataFrame')
    ),
    check_object("store_counts"),
    check_function("print", 0).check_args(0).has_equal_value(),

    check_function(
        name='store_types.value_counts',
        index=1,
        signature=sig_from_obj('pandas.core.frame.DataFrame')
    ).check_args(0).has_equal_value(),
    check_object("store_props"),
    check_function("print", 1).check_args(0).has_equal_value(),

    check_function(
        name='store_depts.value_counts',
        index=0,
        signature=sig_from_obj('pandas.core.frame.DataFrame')
    ).check_args(0).has_equal_value(),
    check_object("dept_counts_sorted"),
    check_function("print", 2).check_args(0).has_equal_value(),

    check_function(
        name='store_depts.value_counts',
        index=1,
        signature=sig_from_obj('pandas.core.frame.DataFrame')
    ).check_args(0).has_equal_value(),
    check_object("dept_props_sorted"),
    check_function("print", 3).check_args(0).has_equal_value()

)


success_msg(
    "Отличный подсчет! Похоже, 43-й отдел существует только в двух магазинах."
)
