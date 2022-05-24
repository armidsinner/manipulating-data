

Ex().multi(

    check_object("sales_all").has_equal_value(),
    check_object("sales_A").has_equal_value(),
    check_object("sales_B").has_equal_value(),
    check_object("sales_C").has_equal_value(),
    check_object("sales_propn_by_type").has_equal_value(),
    check_function("print", 0).check_args(0).has_equal_value()

)


success_msg(
    """ Изумительная математика! Около 91% продаж произошло в магазинах типа A', 
        9% - в магазинах типа B, и нет записей о продажах для магазинов типа C. 
        Теперь посмотрите, можете ли вы выполнить этот расчет с помощью .groupby()."""
)
