

Ex().multi(
    check_function('sales.pivot_table', 0, signature=False).multi(
        check_args(0).has_equal_value(),
        check_args(1).has_equal_value(),
        check_args(2).has_equal_value(),
    ).has_equal_value(),
    check_object('mean_sales_by_type_holiday').has_equal_value(),
    check_function('print', 0).check_args(0).has_equal_value(),
)


success_msg(
    """ Идеально! Сводные таблицы - это еще один способ сделать то же самое, 
        что и групповое обобщение."""
)
