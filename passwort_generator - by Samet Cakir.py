import random
import string


ROT    = "\033[91m"
GRUEN  = "\033[92m"
GELB   = "\033[93m"
BLAU   = "\033[94m"
LILA   = "\033[95m"
CYAN   = "\033[96m"
FETT   = "\033[1m"
RESET  = "\033[0m"


def zeige_header():
    print(f"""
{LILA}{FETT}╔══════════════════════════════════════════╗
║        🔐  PASSWORT-GENERATOR           ║
║        von Samet Hakan Cakir            ║
╚══════════════════════════════════════════╝{RESET}
""")


def bewerte_staerke(passwort):
    punkte = 0
    if len(passwort) >= 12:
        punkte += 1
    if any(z.isupper() for z in passwort):
        punkte += 1
    if any(z.islower() for z in passwort):
        punkte += 1
    if any(z.isdigit() for z in passwort):
        punkte += 1
    if any(z in string.punctuation for z in passwort):
        punkte += 1

    if punkte <= 2:
        return f"{ROT}Schwach{RESET}"
    elif punkte == 3:
        return f"{GELB}Mittel{RESET}"
    elif punkte == 4:
        return f"{CYAN}Stark{RESET}"
    else:
        return f"{GRUEN}Sehr stark{RESET}"


def generiere_passwort(laenge, gross, klein, zahlen, sonderzeichen):
    zeichenpool = ""
    pflichtzeichen = []

    if gross:
        zeichenpool += string.ascii_uppercase
        pflichtzeichen.append(random.choice(string.ascii_uppercase))
    if klein:
        zeichenpool += string.ascii_lowercase
        pflichtzeichen.append(random.choice(string.ascii_lowercase))
    if zahlen:
        zeichenpool += string.digits
        pflichtzeichen.append(random.choice(string.digits))
    if sonderzeichen:
        zeichenpool += string.punctuation
        pflichtzeichen.append(random.choice(string.punctuation))

    if not zeichenpool:
        return None

    restliche = [random.choice(zeichenpool) for _ in range(laenge - len(pflichtzeichen))]
    alle = pflichtzeichen + restliche
    random.shuffle(alle)
    return "".join(alle)


def ja_nein(frage):
    while True:
        antwort = input(f"{CYAN}{frage} (j/n): {RESET}").strip().lower()
        if antwort in ("j", "ja"):
            return True
        elif antwort in ("n", "nein"):
            return False
        print(f"{ROT}Bitte 'j' oder 'n' eingeben.{RESET}")


def main():
    zeige_header()

    while True:
        print(f"{FETT}── Einstellungen ──────────────────────────{RESET}")

        
        while True:
            try:
                laenge = int(input(f"{CYAN}Passwortlänge (8–64): {RESET}"))
                if 8 <= laenge <= 64:
                    break
                print(f"{ROT}Bitte eine Zahl zwischen 8 und 64 eingeben.{RESET}")
            except ValueError:
                print(f"{ROT}Ungültige Eingabe. Bitte eine Zahl eingeben.{RESET}")

        print()
        gross        = ja_nein("Großbuchstaben (A–Z)?")
        klein        = ja_nein("Kleinbuchstaben (a–z)?")
        zahlen       = ja_nein("Zahlen (0–9)?      ")
        sonderzeichen = ja_nein("Sonderzeichen (!@#)?")

        print()

        
        passwort = generiere_passwort(laenge, gross, klein, zahlen, sonderzeichen)

        if passwort is None:
            print(f"{ROT}Fehler: Mindestens eine Zeichenart muss ausgewählt sein!{RESET}\n")
        else:
            staerke = bewerte_staerke(passwort)
            print(f"{FETT}── Ergebnis ───────────────────────────────{RESET}")
            print(f"  Passwort : {GRUEN}{FETT}{passwort}{RESET}")
            print(f"  Länge    : {BLAU}{len(passwort)} Zeichen{RESET}")
            print(f"  Stärke   : {staerke}")
            print(f"{FETT}───────────────────────────────────────────{RESET}")
            print()

        
        if not ja_nein("Noch ein Passwort generieren?"):
            print(f"\n{LILA}{FETT}Tschüss! Bleib sicher. 🔐{RESET}\n")
            break
        print()

if __name__ == "__main__":
    main()
