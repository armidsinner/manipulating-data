

msg1 = "Вы указали срез Индия, Хайдарабад?"
msg2 = "Вы указали срез Ирак, Багдад?"
msg3 = "Использовали ли вы метод .loc[] для среза от Индия, Хайдарабад до Ирак, Багдад?"
msg4 = "Использовали ли вы метод .loc[] для среза столбцов от `date` до `avg_temp_c`?"
msg5 = "Вы правильно устанавливаете столбцы от date до avg_temp_c?"

Ex().multi(

    check_function("print", 0).multi(
        has_equal_ast(code="('Индия', 'Хайдарабад')", exact=False, incorrect_msg=msg1),
    ),
    check_function("print", 0).multi(
        has_equal_ast(code="('Ирак', 'Багдад')", exact=False, incorrect_msg=msg2),
    ),
    check_function("print", 0).multi(
        has_equal_ast(code="temperatures_srt.loc[('Индия', 'Хайдарабад'):('Ирак', 'Багдад')]", exact=False, incorrect_msg=msg3),
    ),
    check_function("print", 0).check_args(0).has_equal_ast(),

    check_function("print", 1).multi(
        has_equal_ast(code="temperatures_srt.loc[:, 'date':'avg_temp_c']",
                      exact=False, incorrect_msg=msg4),
    ),
    check_function("print", 1).check_args(0).has_equal_ast(),

    check_function("print", 2).multi(
        has_equal_ast(code="('Индия', 'Хайдарабад')", exact=False, incorrect_msg=msg1),
    ),
    check_function("print", 2).multi(
        has_equal_ast(code="('Ирак', 'Багдад')", exact=False, incorrect_msg=msg2),
    ),
    check_function("print", 2).multi(
        has_equal_ast(code="temperatures_srt.loc[('Индия', 'Хайдарабад'):('Ирак', 'Багдад'), 'date':'avg_temp_c']",
                      exact=False, incorrect_msg=msg5),
    ),
    check_function("print", 2).check_args(0).has_equal_ast(),
)


success_msg(
    """ Блестящая двунаправленная нарезка! 
        Нарезка с помощью .loc[] позволяет брать срез одновременно в обоих направлениях."""
)
