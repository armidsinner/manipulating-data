

Ex().multi(
    check_function('sales.pivot_table', 0, signature=False).multi(
        check_args(0).has_equal_value(),
        check_args(1).has_equal_value(),
        check_args(2).has_equal_value(),
        check_args(3).has_equal_value(),
    ).has_equal_value(),
    check_function('print', 0).check_args(0).has_equal_value(),
)
