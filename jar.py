class Jar:

    def __init__(self, capacity=12, cookie=0):

        self._cap = capacity
        if self._cap < 0:
            raise ValueError("Capacity cannot be negative")
        self._cookie = cookie

    def __str__(self): #return cookies
        return "🍪" * self._cookie
    
    def deposit(self, n): #add cookies to the jar
        if (n + self._cookie) > self._cap:
            raise ValueError("Exceeds jar's capacity")
        else:
            self._cookie += n
            return f"Added {n} cookies"
        ...
    def withdraw(self, n): #remove cookies from the jar
        if n > self._cookie:
            raise ValueError("Not enough cookies")
        else:
            self._cookie -= n
            return f"Removed {n} Cookies"

    @property
    def capacity(self): #tell jar's capacity
        return self._cap

    @property
    def size(self): #tell the actuall num of cookies in the jar
        return self._cookie

