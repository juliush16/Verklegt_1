from ui.main_ui import MainMenu
from Repo.AircraftTypeRepo import AirCraftTypeRepo as ATR

# MainMenu()

eitthvad = ATR()
x = eitthvad.get_aircraft()
for i in range(len(x)):
    print(x[i])