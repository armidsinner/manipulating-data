

Ex().multi(

    check_function(
        name='sales.drop_duplicates',
        index=0,
        signature=sig_from_obj('pandas.core.frame.DataFrame')
    ).check_args(0).has_equal_value(),
    check_object("store_types"),
    check_function("print", 0).check_correct(
        check_args(0).has_equal_value(),
        check_function("store_types.head", signature=""),
    ),

    check_function(
        name='sales.drop_duplicates',
        index=1,
        signature=sig_from_obj('pandas.core.frame.DataFrame')
    ).check_args(0).has_equal_value(),
    check_object("store_depts"),
    check_function("print", 1).check_correct(
        check_args(0).has_equal_value(),
        check_function("store_depts.head", signature=""),
    ),

    check_function(
        name='sales.drop_duplicates',
        index=2,
        signature=sig_from_obj('pandas.core.frame.DataFrame')
    ).check_args(0).has_equal_value(),
    check_object("holiday_dates"),
    check_function("print", 2).check_args(0).has_equal_value()

)


success_msg(
    """ Ослепительное падение дубликатов! Праздничные недели соответствуют Суперкубку в феврале, 
        Дню труда в сентябре, Дню благодарения в ноябре и Рождеству в декабре. Теперь, 
        когда дубликаты удалены, пришло время провести некоторый подсчет."""
)
