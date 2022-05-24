

msg1 = "Правильно ли вы вычислили `max` столбца `date`?"
msg2 = "Правильно ли вы вычислили `min` столбца `date`?"

Ex().multi(
    check_function("print", 0).check_correct(
        check_args(0).has_equal_value(),
        check_args(0).has_equal_ast(code="sales['date'].max()", incorrect_msg=msg1)
    ),
    check_function("print", 1).check_correct(
        check_args(0).has_equal_value(),
        check_args(0).has_equal_ast(code="sales['date'].min()", incorrect_msg=msg2)
    ),
)


success_msg(
    """ Супер подведение итогов! Взятие минимального и максимального значений столбца дат удобно 
        для определения того, какой период времени охватывают ваши данные. В данном случае имеются 
        данные за период с февраля 2020 года по октябрь 2022 года."""
)
