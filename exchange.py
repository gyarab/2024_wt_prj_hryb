import httpx # type: ignore
import os

def mena() -> float:
    url = httpx.get("https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt")
    for line in url.text.split("\n"):
        if "|EUR|" in line:
            return float(line.split("|")[-1].replace(",", "."))
    
def jeCislem(text: str) -> bool:
    return text.isdigit()

def precistVstup(text: str) -> str:
    return input(f"{text}\n-> ")

def smazat() -> None:
    os.system("cls")
    print("Směnárna\n")

def vypocitatVymenu(smer: str, kurz: float) -> bool:
    if smer not in ("0", "1"):
        return False
    while True:
        smazat()
        penize = precistVstup("Zadejte částku v CZK:" if smer == "0" else "Zadej částku v EUR:")
        if not jeCislem(penize):
            continue
        penize = float(penize)
        result = penize / kurz if smer == "0" else penize * kurz
        print(f"V {'EUR' if smer == '0' else 'CZK'}: {result}")
        return True

def main() -> None:
    kurz = mena()
    while True:
        smazat()
        smer = precistVstup("0 = CZK -> EUR\n1 = EUR -> CZK")
        if not vypocitatVymenu(smer, kurz):
            continue
        if precistVstup("\n0 = konec programu\ncokoliv = nový převod") == "0":
            break

if __name__ == "__main__":
    main()
