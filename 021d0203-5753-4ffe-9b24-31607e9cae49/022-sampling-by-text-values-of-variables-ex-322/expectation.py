

Ex().multi(
    check_correct(
        check_object('szfo_skfo').has_equal_value(),
        multi(
            has_equal_ast(code="(census['region'] == 'SKFO')",
                          incorrect_msg="Правильно ли вы включили фильтр для строк с регионом, "
                                        "равным `SKFO`?"),

            has_equal_ast(code="(census['region'] == 'SZFO')",
                          incorrect_msg="Правильно ли вы включили фильтр для строк с регионом, "
                                        "равным `SZFO`?"),
            has_equal_ast(
                code="(census['region'] == 'SZFO') | (census['region'] == 'SKFO')",
                incorrect_msg="Вы заключили каждое условие в круглые скобки и "
                              "использовали оператор логическое или `|` ?")
        ),

    ),

    check_function('print').check_args(0).has_equal_value(),

)
