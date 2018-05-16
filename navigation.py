def menu():
while True():
print(
“Wählen Sie ein Bild aus”, 
“(1) Bild untersuchen”, 
“(2) Beenden”)
choice = int(input(“Auswahl”))
if choice == 2:
untersuche_Bild()
elif choice ==2:
sys.exit(0)
else:
print(“Bitte nur 1 oder 2 eingeben”)

