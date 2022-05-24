

Ex().multi(
    check_function('sales.pivot_table', 0, signature=False).multi(
        check_args(0).has_equal_value(),
        check_args(1).has_equal_value(),
        check_args(2).has_equal_value(),
        check_args(3).has_equal_value(),
        check_args(4).has_equal_value(),
    ).has_equal_value(),
    check_function('print', 0).check_args(0).has_equal_value(),
)


success_msg(
    """ Великолепное получение прибыли! Теперь вы вооружены навыками сводных таблиц, 
        которые могут помочь вам вычислять сводки на нескольких сгруппированных 
        уровнях в одной строке кода."""
)
