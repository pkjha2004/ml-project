import sys
import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Finding the traceback
    file_name = exc_tb.tb_frame.f_code.co_filename## (to remember)
    # Using format() instead of f-string
    error_message = "Error occurred in python script name [{}] line number [{}] error message [{}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message  # Ensure return statement is present

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Corrected super() call
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message



if __name__ =="__main__":
  try:
    a = 1/0
  except Exception as e:
    logging.info("Divide by Zero error")
    raise CustomException(e,sys)


   

