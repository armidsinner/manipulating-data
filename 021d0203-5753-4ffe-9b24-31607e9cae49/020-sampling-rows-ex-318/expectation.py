

Ex().multi(
    check_correct(
        check_object('fam_lt_1k_pac').has_equal_value(),
        multi(
            has_equal_ast(code="(census['region'] == 'UFO')",
                          incorrect_msg="Правильно ли вы включили фильтр для строк с регионом, "
                                        "равным `UFO`?"),

            has_equal_ast(code="(census['family_members'] < 1000)",
                          incorrect_msg="Правильно ли вы включили фильтр для строк с "
                                        "`family_members` менее 1000?"),
            has_equal_ast(
                code="(census['family_members'] < 1000) & (census['region'] == 'UFO')",
                incorrect_msg="Вы заключили каждое условие в круглые скобки и "
                              "использовали оператор логическое и `&` для их объединения?")
        ),

    ),

    check_function('print').check_args(0).has_equal_value(),

)


success_msg(
    """ Превосходно! Использование квадратных скобок плюс логические условия 
        часто является наиболее эффективным способом определения интересуемых строк данных."""
)
