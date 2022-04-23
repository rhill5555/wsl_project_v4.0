# Filename: error_handling.py
# This contains code for error handling
# And Formatting
########################################################################################################################
# 1 - Imports

########################################################################################################################
# 2 - Formatting

# Formats dividers for error messages
class ErrorMsgFormat(object):
    def __init__(self, error_dic_dict):

        for key in error_dict_div:
            setattr(self, key, error_dict_div[key])


# error_dict_div dictionary definition
if __name__ == "__main":

    # Creating the dictionary
    error_dict_div = {'input_error': ['Input Error', '=', 60],
                      'wipe_out_wav': ['Wipe Out', '~', 60]}

    div = ErrorMsgFormat(error_dict_div)

