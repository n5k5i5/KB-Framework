"""
Bellek önbellek (iskelet).
"""
class BellekOnbellek:
    def __init__(self): self._s = {}
    def set(self, k, v): self._s[k] = v; return True
    def get(self, k): return self._s.get(k)