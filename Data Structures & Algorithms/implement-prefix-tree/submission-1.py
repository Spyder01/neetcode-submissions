class PrefixTree:

    def __init__(self):
        self.map = {}
        

    def insert(self, word: str) -> None:
        _map = self.map
        for char in word:
            if char not in _map:
                _map[char] = {}

            _map = _map[char] 
        
        _map['#'] = True


    def search(self, word: str) -> bool:
        _map = self.map

        for char in word:
            if char not in _map:
                return False
            
            _map = _map[char]
        
        return _map.get('#', False)
        

    def startsWith(self, prefix: str) -> bool:

        _map = self.map

        for char in prefix:
            if char not in _map:
                return False
            
            _map = _map[char]
        

        return True
        
        