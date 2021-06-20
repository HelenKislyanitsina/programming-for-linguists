def __contains__(self, element) -> bool:
    for value in self.data.values():
        if element in value:
            return True
    return False

def __iter__(self):
    list_values = []
    for key, value in sorted(self.data.items(), reverse=True):
        list_values.extend(value)
    return iter(list_values)
