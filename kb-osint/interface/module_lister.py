# -*- coding: utf-8 -*-
"""
Module lister and filter.
"""
from typing import Dict, Any, Optional, List, Tuple
from interface.formatter import Formatter


def _meta(module: Any) -> Dict[str, Any]:
    return module if isinstance(module, dict) else {}


class ModuleLister:
    def list(self, modules: Dict[str, Any], detail_level: str = "normal") -> None:
        if not modules:
            print(Formatter.error("No modules loaded! / Hiç modül yüklenmemiş!"))
            return

        print(Formatter.title("KB-OSINT MODULE LIST / MODÜL LİSTESİ"))
        print(Formatter.info(f"Total {len(modules)} modules loaded / Toplam {len(modules)} modül yüklü"))
        print("-" * 80)

        for i, name in enumerate(sorted(modules.keys()), 1):
            self._single_module_info(i, name, modules[name], detail_level)

    def filter(
        self,
        modules: Dict[str, Any],
        category: Optional[str] = None,
        status: Optional[bool] = None,
        search_text: Optional[str] = None,
    ) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        search = (search_text or "").lower()

        for name, module in modules.items():
            meta = _meta(module)
            cat = meta.get("kategori")
            active = meta.get("aktif", True)
            description = meta.get("aciklama", "")

            if category and cat != category:
                continue
            if status is not None and active != status:
                continue

            if search:
                if (search not in name.lower()) and (search not in description.lower()):
                    continue

            result[name] = module

        return result

    def by_category(self, modules: Dict[str, Any]) -> Dict[str, List[Tuple[str, Any]]]:
        categories: Dict[str, List[Tuple[str, Any]]] = {}
        for name, module in modules.items():
            meta = _meta(module)
            category = meta.get("kategori", "diger")
            categories.setdefault(category, []).append((name, module))
        return categories

    def _single_module_info(self, idx: int, name: str, module: Any, detail_level: str) -> None:
        meta = _meta(module)
        print(f"{idx:2d}. {Formatter.highlight(name)}")
        print(f"     {Formatter.info('Description / Açıklama:')} {meta.get('aciklama', 'No description / Açıklama yok')}")
        print(f"     {Formatter.info('Version / Versiyon:')} {meta.get('versiyon', '1.0.0')}")
        print(f"     {Formatter.info('Category / Kategori:')} {meta.get('kategori', 'general / genel')}")
        print(f"     {Formatter.info('Author / Yazar:')} {meta.get('yazar', 'Unknown / Bilinmiyor')}")

        if detail_level == "detayli":
            api_req = ", ".join(meta.get("api_gereksinimleri", [])) or "None / Yok"
            deps = ", ".join(meta.get("bagimliliklar", [])) or "None / Yok"
            security = meta.get("guvenlik_seviyesi", "medium / orta")
            is_active = meta.get("aktif", True)
            status_text = "🟢 Active / Aktif" if is_active else "🔴 Inactive / Pasif"

            print(f"     {Formatter.info('API Requirements / API Gereksinimleri:')} {api_req}")
            print(f"     {Formatter.info('Dependencies / Bağımlılıklar:')} {deps}")
            print(f"     {Formatter.info('Security Level / Güvenlik Seviyesi:')} {security}")
            print(f"     {Formatter.info('Status / Durum:')} {status_text}")

        print()