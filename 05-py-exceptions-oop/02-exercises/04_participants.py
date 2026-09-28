#Bruk with og encoding="utf-8" i alle filoppgavene. Gjenbruk filsti-oppsettet fra innledningen. Bruk egne
#øvingsfiler.
#Oppgave 3.1 Deltakerliste
#Opprett attendees.txt i data-mappen med fire navn, ett per linje. Les filen og legg navnene i en liste. Bruk
#strip() og hopp over tomme linjer.
#Skriv ut navnene og antall deltakere. Håndter FileNotFoundError med en melding som forteller hvilken fil
#programmet forsøkte å lese. Skriv antallet bare når lesingen lykkes.
#Test med filen på plass, med et filnavn som ikke finnes, og med en tom fil. En tom fil skal gi 0 deltakere, ikke en
#melding om manglende fil.

from pathlib import Path

data_folder = Path(__file__).parent.parent / "03-data"
path = data_folder / "attendees.txt"


try:
    with path.open(encoding="utf-8") as file:

        attendees = []

        for line in file:
            name = line.strip()

            if name:
                attendees.append(name)

        print(attendees)
        print(f"Antall deltakere i listen: {len(attendees)}")

except FileNotFoundError:
    print(f"Fant ikke filen: {path}")
