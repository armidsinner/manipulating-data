

Ex().multi(
    check_correct(
        check_object('individuals').has_equal_value(),
        has_equal_ast(code="census['individuals']",
                      incorrect_msg="Правильно ли вы выбрали столбец `individuals`?")
    ),
    check_function('individuals.head').has_equal_value(),
    check_function('print').check_args(0).has_equal_value(),

)
