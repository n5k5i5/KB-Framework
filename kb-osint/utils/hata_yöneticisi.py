"""
Hata yöneticisi (iskelet).
"""
class HataYoneticisi:
    def handle(self, e: Exception) -> str:
        return f"Hata: {e}"