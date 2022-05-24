
Ex().multi(

    check_function('census.sort_values', signature="").check_args(0).has_equal_value(),
    check_object('census_ind').has_equal_value(),
    check_function('census_ind.head').has_equal_value(),
    check_function('print').check_args(0).has_equal_value(),

)
