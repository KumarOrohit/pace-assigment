# FUNCTION FUNCTIONALITIES :-
    # - Will have null check for mandatory params
def mandatory_param_check(data):

    # if empty request param
    if not data:
        return True

    # all null check values
    null_check_values_list = [None, 'null', 'None', '', ['']]

    check = any(item in null_check_values_list for item in data.values())

    return check


# FUNCTION FUNCTIONALITIES :-
    # - Basic response structure
def basic_response_dict(message, error, data):

    response = {
        "message": message,
        "error": error,
        "data": data
    }

    return response