

Ex().multi(
    has_import('pandas', same_as=True),
    check_function("print", 0).check_correct(
        has_equal_output(),
        check_args(0).has_equal_ast(
            incorrect_msg="Вы распечатали `.values` для `census` DataFrame?"),
    ),
    check_function("print", 1).check_correct(
        has_equal_output(),
        check_args(0).has_equal_ast(
            incorrect_msg="Вы распечатали `.columns` для `census` DataFrame?"),
    ),
    check_function("print", 2).check_correct(
        has_equal_output(),
        check_args(0).has_equal_ast(
            incorrect_msg="Вы распечатали `.index` для `census` DataFrame?"),
    ),
)


success_msg(
    """ Динамитное открытие DataFrame! DataFrame состоят из трех компонентов: 
        значений, индекса столбца и индекса строки."""
)
