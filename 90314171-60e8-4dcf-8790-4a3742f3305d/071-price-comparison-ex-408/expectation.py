

Ex().multi(
    check_function("apples.hist", index=0, signature=False).has_equal_output(),
    check_function("apples.hist", index=0, signature=False).has_equal_ast(
        incorrect_msg="Правильно ли вы подбираете `apples` для типа `conventional`?"),

    check_function("apples.hist", index=1, signature=False).has_equal_output(),
    check_function("apples.hist", index=1, signature=False).has_equal_ast(
        incorrect_msg="Правильно ли вы подбираете `apples` для типа `organic`?"),

    check_function('matplotlib.pyplot.legend', 0, signature=False).multi(
        check_args(0).has_equal_value(),
    ),
    check_function('matplotlib.pyplot.show', 0, signature=False).has_equal_value(),
)
