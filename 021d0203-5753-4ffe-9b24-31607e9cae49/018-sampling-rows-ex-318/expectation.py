

Ex().multi(
    check_correct(
        check_object('ind_gt_10k').has_equal_value(),
        has_equal_ast(code="census[census['individuals'] > 10000]",
                      incorrect_msg="Правильно ли вы отфильтровали `census`, чтобы включить "
                                    "только строки с `individuals`, превышающим 10000?")
    ),

    check_function('print').check_args(0).has_equal_value(),

)
