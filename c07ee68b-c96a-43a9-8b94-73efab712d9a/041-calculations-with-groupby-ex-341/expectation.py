

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

    check_function('sum').check_args(0),

    check_object("sales_by_type").has_equal_value(),
    check_object("sales_propn_by_type").has_equal_value(),
    check_function("print", 0).check_args(0).has_equal_value()
)
