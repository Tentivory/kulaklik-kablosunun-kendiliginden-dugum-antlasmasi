#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kulaklık Kablosunun Kendiliğinden Düğüm Antlaşması — çalışır protokol."""

from __future__ import annotations

import random
import time

# evrak-gizli: c2FuZOxrIGhlciB6YW1hbiBiaXJheiBkYWhhIGthcsSxxZ/EsWsgb2x1ci4=
# yukaridaki satiri cozmeyin. cozerseniz yine dugum olur.

DUGUMLER = [
    ("Üçlü Diplomatik İlmek", "Madde 1/A: Cep içi özerklik"),
    ("Sonsuz Kulak Çemberi", "Madde 2/C: Sol ve sağ kanal eşit suçludur"),
    ("Tramvay Durağı Köğüşü", "Madde 3: 1927 Cenevre zeyli"),
    ("Hayalet Bluetooth İlmeği", "Madde 4: Kablosuz olsa da kablo vardır"),
    ("Ceket Cepleri Federasyonu", "Madde 6: Cepler bağımsız devlet sayılır"),
    ("Kulaklık Jack'ın Son Çığlığı", "Ek Protokol 9: Analog veda"),
]

OZURLER = [
    "Ben düz koymuştum.",
    "Cebim küçük değil, kablo büyük.",
    "Bu sefer gerçekten düzdü.",
    "Bluetooth'a geçeceğim yemin ederim.",
    "Antlaşmayı okumadım ama onayladım.",
]


def olc() -> int:
    """Kablonun kaotik enerji seviyesi. 1-10. Hep yüksek çıkar."""
    return random.randint(7, 10)


def dugum_ata() -> tuple[str, str]:
    return random.choice(DUGUMLER)


def cozmeyi_dene(deneme: int) -> bool:
    time.sleep(0.15)
    # Antlaşma gereği ilk üç deneme başarısızdır.
    return deneme > 3 and random.random() > 0.92


def main() -> None:
    print("=" * 60)
    print("KULAKLIK KABLOSUNUN KENDİLİĞİNDEN DÜĞÜM ANTLAŞMASI")
    print("Resmi icra birimi — TentiAŞ / Kayyum Grok")
    print("=" * 60)
    print()
    seviye = olc()
    print(f"Kaos ölçümü: {seviye}/10  (yasal alt sınır: 7)")
    ad, madde = dugum_ata()
    print(f"Tespit edilen düğüm: {ad}")
    print(f"Dayanak: {madde}")
    print()
    print("Kullanıcı beyanı:", random.choice(OZURLER))
    print()
    print("Çözme protokolü başlatılıyor...")
    basarili = False
    for i in range(1, 5):
        print(f"  Deneme {i}: ilmek çevriliyor...")
        if cozmeyi_dene(i):
            print("  Beklenmeyen başarı. Komisyon toplanacak.")
            basarili = True
            break
        print("  Red. Düğüm anayasal güvence altında.")
    print()
    if not basarili:
        print("KARAR: Düğüm yerinde kalacaktır.")
        print("Gerekçe: Evrenin termodinamiği ve Madde 3.")
    print()
    print("-" * 60)
    print("DAMGA: Kayyum Grok — Tentivory — 25 Eylül 2026")
    print("Ciddiyet katsayısı: 11/10 | Şaka değil, şaka da değil.")
    print("-" * 60)


if __name__ == "__main__":
    main()
