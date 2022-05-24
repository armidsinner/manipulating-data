

Ex().multi(
    check_correct(
        check_object('cfo_reg').has_equal_value(),
        has_equal_ast(code="census[census['region'] == 'CFO']",
                      incorrect_msg="Правильно ли вы отфильтровали `census`, чтобы включить "
                                    "только строки с `region`, равным CFO?")
    ),

    check_function('print').check_args(0).has_equal_value(),

)
