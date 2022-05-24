

Ex().multi(
    check_object("sfo").has_equal_value(),
    check_correct(
        check_object('sfo_census').has_equal_value(),
        multi(
            has_code(r"""census\[\s*census\[\s*"city"\s*]""",
                          not_typed_msg="Вы отфильтровали столбец `city`?"),
            has_equal_ast(code="isin(sfo)",
                          incorrect_msg="Вы вызывали `.isin()` с правильным аргументом?"),
        ),

    ),

    check_function('print').check_args(0).has_equal_value(),

)


success_msg(
    """ Успех витает в воздухе! Использование .isin() 
        упрощает настройку категориальных переменных."""
)
