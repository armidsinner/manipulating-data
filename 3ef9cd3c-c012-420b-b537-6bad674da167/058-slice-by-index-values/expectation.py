

msg1 = "Использовали ли вы метод .loc[] для среза от Пакистан до Россия?"
msg2 = "Использовали ли вы метод .loc[] для среза от Лахоре до Москва?"
msg3 = "Вы указали срез Пакистан, Лахоре?"
msg4 = "Вы указали срез Россия, Москва?"
msg5 = "Использовали ли вы метод .loc[] для среза от Пакистан, Лахоре до Россия, Москва?"

Ex().multi(


    check_function('temperatures_ind.sort_index', 0, signature=False).has_equal_value(),
    check_object('temperatures_srt'),
    check_function("print", 0).multi(
        has_equal_ast(code="temperatures_srt.loc['Пакистан':'Россия']", exact=False, incorrect_msg=msg1),
    ),
    check_function("print", 0).check_args(0).has_equal_ast(),
    check_function("print", 1).multi(
        has_equal_ast(code="temperatures_srt.loc['Лахоре':'Москва']", exact=False, incorrect_msg=msg2),
    ),
    check_function("print", 1).check_args(0).has_equal_ast(),
    check_function("print", 2).multi(
        has_equal_ast(code="('Пакистан', 'Лахоре')", exact=False, incorrect_msg=msg3),
    ),
    check_function("print", 2).multi(
        has_equal_ast(code="('Россия', 'Москва')", exact=False, incorrect_msg=msg4),
    ),
    check_function("print", 2).multi(
        has_equal_ast(code="temperatures_srt.loc[('Пакистан', 'Лахоре'):('Россия', 'Москва')]", exact=False, incorrect_msg=msg5),
    ),
    check_function("print", 2).check_args(0).has_equal_ast(),
)



success_msg(
    """ Отличная работа! Объединение среза с .loc[] 
        обеспечивает краткий синтаксис для выборки."""
)
