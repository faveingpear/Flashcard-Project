from json import JSONEncoder

class MyJsonEncoder(JSONEncoder):
    def default(self, obj):
        return obj.to_json()