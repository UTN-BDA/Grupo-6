from dataclasses import dataclass


@dataclass
class ResponseMessage:
    """
    ResponseMessage is a class that represents a response message
    """
    message: str
    status_code: int
    data: dict = None


@dataclass(init=False)
class ResponseBuilder:
    # cambio de nombre de atributos por sobrescritura sobre los métodos
    _message: str
    _status_code: int
    _data: dict = None

    def add_message(self, message: str):
        self._message = message  # cambio
        return self
    
    def add_status_code(self, status_code: int):
        self._status_code = status_code  # cambio
        return self
    
    def add_data(self, data: dict):
        self._data = data  # cambio
        return self
    
    def build(self):
        return ResponseMessage(
            # cambio
            message=self._message, 
            status_code=self._status_code,
            data=self._data
        )