

Ex().multi(
    check_correct(
        check_df("census").check_keys("total").has_equal_value(),
        has_equal_ast(code="census['individuals'] + census['family_members']",
                      incorrect_msg="Вы создали столбец `total`, добавив столбцы `individuals` и `family_members`?")
    ),
    check_correct(
        check_df("census").check_keys("p_individuals").has_equal_value(),
        has_equal_ast(code="census['individuals'] / census['total']",
                      incorrect_msg="Вы правильно создали столбец p_individuals? Он должен содержать долю отдельных лиц в общей численности населения.")
    ),
    check_function("print").check_args(0).has_equal_value()

)


success_msg(
    """ Так держать! Если в вашем наборе данных нет точных столбцов, 
        которые вам нужны, вы часто можете создать свои собственные из того, что у вас есть."""
)
