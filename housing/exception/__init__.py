import os 
import sys


class HousingException(Exception):
    def __init__(self, error_message:Exception, error_detail:sys) -> None:
        super().__init__(error_message)
        self.error_message = HousingException.get_detailed_error_message(error_message=error_message,
                                                                        error_detail=error_detail)

    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_detail:sys) -> str:
        """
        error_message : object of Exception class
        error_detail : object of sys
        """
        _, _, exec_tb = error_detail.exc_info()
        lineNumber = exec_tb.tb_frame.f_lineno
        fileName = exec_tb.tb_frame.f_code.co_filename
        error_message = f"Error traced in [{fileName}] on line number: [{lineNumber}].Error message:{error_message}"
        return error_message
    
    def __str__(self) -> str:
        return self.error_message

    def __repr__(self) -> str:
        return HousingException.__name__.str()










