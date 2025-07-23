import logging
from typing import Any, Optional, Dict, List, Union

_logger = logging.getLogger(__name__)


class ResponseGenerator:
    def __init__(self, status_code: int, message: str, logger_message: str, data: Optional[Union[Dict[str, Any], List[Any]]] = None,
                 error_details: str = None):
        self.status_code = status_code
        self.message = message
        self.data = data
        self.error_details = error_details
        self.logger_message = logger_message

    def success_response(self):
        _logger.info(self.logger_message)
        return {'response_code': self.status_code,
                'message': self.message,
                'statusFlag': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': self.data
                }

    def warning_response(self):
        _logger.warning(self.logger_message)
        return {'response_code': self.status_code,
                'message': self.message,
                'statusFlag': False,
                'status': 'WARNING',
                'errorDetails': None,
                'data': self.data
                }

    def failed_response(self, *args):
        _logger.error(self.logger_message)
        return {'response_code': self.status_code,
                'message': self.message,
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': self.error_details,
                'data': self.data}
