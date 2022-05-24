
Ex().multi(

    check_function('census.sort_values').multi(
        check_args(0).has_equal_value(),
        check_args(1).has_equal_value(),
    ),
    check_object('census_reg_fam').has_equal_value(),
    check_function('census_reg_fam.head').has_equal_value(),
    check_function('print').check_args(0).has_equal_value(),

)



success_msg(
    """ Молодец! Использование .sort_values() и .head() образуют мощную пару."""
)
