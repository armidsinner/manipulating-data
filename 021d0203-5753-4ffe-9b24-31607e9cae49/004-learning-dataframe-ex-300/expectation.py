
Ex().multi(
    check_function("print", 0).check_correct(
        check_args(0).has_equal_value(),
        check_function("census.head", signature=""),
    ).has_equal_value(),
    check_function("print", 1).check_correct(
        check_args(0).has_equal_value(),
        check_function("census.info", signature=""),
    ).has_equal_value()
)
