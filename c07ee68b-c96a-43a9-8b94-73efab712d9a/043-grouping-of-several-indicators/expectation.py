

msg1 = "Проверьте свое определение `sales_stats`. Вы выбрали столбец `weekly_sales` " \
      "из DataFrame перед агрегированием?"
msg2 = "Проверьте свое определение unemp_fuel_stats. Выбрали ли вы правильные столбцы " \
       "из DataFrame перед агрегированием?"

Ex().multi(
    has_import("numpy", same_as=True),
    has_equal_ast(code="sales.groupby('type')['weekly_sales']", exact=False, incorrect_msg=msg1),
    check_function('sales.groupby', 0).check_args(0).has_equal_value(),
    check_function('sales.groupby.agg', 0, signature=False).check_args(0).has_equal_value(),
    check_object('sales_stats').has_equal_value(),
    check_function('print', 0).check_args(0).has_equal_value(),

    has_equal_ast(code="sales.groupby('type')[['unemployment', 'fuel_price_usd_per_l']]", exact=False, incorrect_msg=msg2),
    check_function('sales.groupby', 1).check_args(0).has_equal_value(),
    check_function('sales.groupby.agg', 1, signature=False).check_args(0).has_equal_value(),
    check_object('sales_stats').has_equal_value(),
    check_function('print', 0).check_args(0).has_equal_value()
)

success_msg(
    """ Потрясающая агрегация! Обратите внимание, что минимальный показатель weekly_sales 
        отрицательный, потому что в некоторых магазинах было больше возвратов, чем продаж."""
)
