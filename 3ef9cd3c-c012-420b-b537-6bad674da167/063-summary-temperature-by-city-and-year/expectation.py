

msg = "Используете ли вы `.dt.year` для доступа к компоненту year столбца `date`?"

Ex().multi(
    check_function('temperatures.pivot_table', signature=False).multi(
        check_args(0).has_equal_ast(),
        check_args(1).has_equal_ast(),
        check_args(2).has_equal_ast(),
    ),
    has_equal_ast(code="temperatures['date'].dt.year", incorrect_msg=msg),
    has_equal_value(name="temperatures['year']"),
    check_object("temp_by_country_city_vs_year"),
    check_function("print", 0).check_args(0).has_equal_value(),
)


success_msg(
    """Мощный поворот! Теперь у вас есть сводная таблица, давайте поработаем с ней."""
)
