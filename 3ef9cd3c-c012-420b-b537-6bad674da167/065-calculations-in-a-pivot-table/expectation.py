

Ex().multi(
    check_function('temp_by_country_city_vs_year.mean', 0, signature=False).has_equal_value(),
    check_function('print', 0).check_args(0).has_equal_value(),
    check_object("mean_temp_by_year"),

    check_function('temp_by_country_city_vs_year.mean', 1, signature=False).check_args(0).has_equal_value(),
    check_function('print', 1).check_args(0).has_equal_value(),
    check_object("mean_temp_by_city"),
)


success_msg(
    """ Классный расчет! При средней температуре чуть выше нуля 
        Харбин славится своим фестивалем ледяных скульптур."""
)
