'''
Output formatter for the other resource classes.
'''
import json

class Formatter ():
    def __init__ (self, success=True, status_code=400, data=[]):
        self.data = data
        self.success = success
        self.status_code = status_code
        self.data = data

    def __str__(self) -> str:
        output = {
            'success': "ok" if self.success else "no",
            'code': self.status_code,
            'length': len(self.data),
            'data': self.data
        }
        return json.dumps(output)

    def print(self):
        output = {
            'success': "ok" if self.success else "no",
            'code': self.status_code,
            'length': len(self.data),
            'data': self.data
        }
        return output
