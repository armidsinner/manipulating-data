

msg1 = "Вы указали две правильные пары страна/город, которые необходимо сохранить? Убедитесь, что у вас нет опечаток."
msg2 = "Правильно ли вы использовали подмножество `.loc[]` для фильтрации `temperature_ind`?"

Ex().multi(
    check_function('temperatures.set_index', 0, signature=False).check_args(0).has_equal_value(),
    check_object('temperatures_ind'),
    check_object('rows_to_keep').has_equal_value(msg1),
    check_function("print").multi(
        has_equal_ast(code="temperatures_ind.loc[rows_to_keep]", exact=False, incorrect_msg=msg2),
    ),
)


success_msg(
    """ Великолепная многоуровневая индексация! Многоуровневые индексы могут упростить 
        понимание вашего набора данных, когда одна категория вложена в другую категорию."""
)
