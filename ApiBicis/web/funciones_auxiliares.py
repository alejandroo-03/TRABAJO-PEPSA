
import json
import decimal
import html
import bleach

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)
        
def sanitize_input(user_input):
    escaped_input = html.escape(user_input)
    return bleach.clean(escaped_input)