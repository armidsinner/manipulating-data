

msg1 = "Проверьте первый вызов `print()`. Вы производите срез по 23-й строке (позиция индекса 22) и 2-му столбцу (позиция индекса 1)?"
msg2 = "Проверьте второй вызов `print()`. Вы производите срез первых 5 строк (позиции индекса от 0 до 5)?"
msg3 = "Проверьте третий вызов `print()`. Вы производите срез всех строк и столбцов 3 и 4 (позиции индекса 2-4)?"
msg4 = "Проверьте четвертый вызов `print()`. Вы производите срез первых 5 строк и столбцов 3 и 4?"

Ex().multi(
    check_function("print", 0).check_args(0).has_equal_value(msg1),
    check_function("print", 1).check_args(0).has_equal_value(msg2),
    check_function("print", 2).check_args(0).has_equal_value(msg3),
    check_function("print", 3).check_args(0).has_equal_value(msg4),

    # has_code(r"print\(temperatures\.iloc\[\s*\d+\s*,\s*\d+\]\)", not_typed_msg="bla"),
    # has_code(r"print\(\s*temperatures\.iloc\[\s*\:\s*\d+\s*\]\s*\)", not_typed_msg="bla")
)


success_msg(
    """ Отличное использование .iloc[]! Используйте .iloc[], 
        чтобы получить срез, используя номера строк или столбцов."""
)
