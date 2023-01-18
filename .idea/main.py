import os
import csv

# TODO:Try To Understand Option 7
def deletePassenger(passengerToDelete):
    listPassengers = []
    deleted = False
    with open("passengers.csv", 'r') as csv_file:
        reader = csv.reader(csv_file)
        for passenger in reader:
            if(len(passenger) != 0):
                if( passengerToDelete[0].upper() == passenger[0].upper() and passengerToDelete[1] == passenger[1]):
                    deleted = True
                else:
                    listPassengers.append(passenger)

    # indexToDelete = 'N'
    # if(len(listPassengersToDelete)>1):
    #     print("\nPlusieurs Passagers Ont été Trouvés.\nVeuillez Choisir Un Passager")
    #     for passenger in listPassengersToDelete:
    #         print(passenger)
    #     indexToDelete = input("\n[A Pour Tous Supprimer]\n[Pour Une Suppression Multiple, Un Chiffre Suivi D'un Espace]: ").split(' ')
    #     if(indexToDelete.__contains__('A')):
    #         listPassengersToDelete.clear()
    #         print("Tous Les Passagers On Etés Supprimés")
    #     else:
    #         for index in indexToDelete:
    #             listPassengersToDelete.pop(int(index)-1)
    #     listPassengers.extend(listPassengersToDelete)
    with open("passengers.csv", 'w') as csv_file:
        writer = csv.writer(csv_file)
        for passenger in listPassengers:
            writer.writerow(passenger)
    return deleted


def takeBusData():
    bus["busId"] = input("Entrer L'id du Bus :")
    bus["lieuDeDepart"] = input("Entrer le Lieu De Depart: ").upper()
    bus["lieuArrive"] = input("Entrer le Lieu De D'arrivé: ").upper()
    bus["placesMax"] = input("Entrer le Nombre De Places Max: ")
    bus["poidMax"] = input("Entrer le Poid Max: ")
    busArr = [bus["busId"], bus["lieuDeDepart"], bus["lieuArrive"], bus["placesMax"], bus["poidMax"]]
    createBus(busArr)

def editPassenger(passengerToModify, busId):
    listPassengers = []
    edited = False
    with open("passengers.csv", 'r') as csv_file:
        reader = csv.reader(csv_file)
        for passenger in reader:
            if(len(passenger) != 0):
                if( passengerToModify[0].upper() == passenger[0].upper() and
                        passengerToModify[1] == passenger[1]):
                    edited = True
                    passenger[1] = busId
                listPassengers.append(passenger)
    # indexToModify = 'N'
    # if(len(listPassengersToModify)>1):
    #     print("\nPlusieurs Passagers Ont Eté Trouvés.\nVeuillez Choisir Un Passager")
    #     index = 1
    #     for passenger in listPassengersToModify:
    #         print(f"{index}. {passenger}")
    #         index+=1
    #     indexToModify = input("\n[\"A\" Pour Tous Les Modifier]\n[Pour Une Modification Multiple, Un Chiffre Suivi D'un Espace]: ").split(' ')
    #     if(indexToModify.__contains__('A')):
    #         listPassengersToModify.clear()
    #         print("Tous Les Passagers On Etés Modifié")
    #     else:
    #         for index in indexToModify:
    #             listPassengersToModify.pop(int(index)-1)
    #     listPassengers.extend(listPassengersToModify)
    with open("passengers.csv", 'w') as csv_file:
        writer = csv.writer(csv_file)
        for passenger in listPassengers:
            writer.writerow(passenger)
    return edited

def getAllBuses():
    with open("bus.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        listBuses = []
        for bus in reader:
            if(len(bus) != 0):
                listBuses.append(bus)
    if(len(listBuses) != 0): return listBuses
    else: return None

def takePassengerData():
    passengerName = input("Entrer Le Nom Du Passager(Q pour annuler) : ").upper()
    if(passengerName == 'Q'):
        return
    passengerLogageWeight = input("Entrer Le Poid des Bagages Du Passager(en Kg): ")
    givePassengerABus = input("Entrer Le Numéro De Bus\n(N Pour Ne Pas Donner): ")
    listBusIds = []
    for bus in getAllBuses():
        listBusIds.append(bus[0])
    while(not listBusIds.__contains__(givePassengerABus) and givePassengerABus != 'N'):
        givePassengerABus = input("L'id Du Bus N'est Pas Valide Veuillez Choisir Un Valid\n(N Pour Ne Pas Donner): ")
    if(givePassengerABus != 'N'):
        passengerBusId = givePassengerABus
    else:
        passengerBusId = 0
    passenger = [passengerName, passengerBusId, passengerLogageWeight]
    createPassenger(passenger)

def showMenu():
    print('''
    =========================BIENVENUE A PyPassenger===========================
    1. Créer Des Bus 
    2. Créer Un Passager
    3. Ajouter Un Passager A Un Bus
    4. Le Nombre de Places Restantes Dans Un Bus
    5. Le Nombre de Kg Reservé Pour Un Bus
    6. Retirer Un Passager D'un
    8. Afficher La Liste De Passagers D'un Bus
    9. Liste De Tous Le Passagers
    10. Verifier La Validité D'un Passager
    
    "Q" pour Sortir\n
    ''')


def createPassenger(passenger):
    with open("passengers.csv", 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(passenger)


def createBus(bus):
    with open("bus.csv", 'r0') as csv_file:
        reader = csv.reader(csv_file)
        busIds = []
        for busId in reader:
            if(len(busId) != 0):
                busIds.append(busId[0])
        while(busIds.__contains__(bus[0])):
            bus[0] = input("L'id Du Bus Choisi N'est Pas Valide Veuillez Choisir Un Autre: ")
    with open("bus.csv", 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(bus)

def getBusWithId(id):
    with open("bus.csv") as csv_file:
        reader = csv.reader(csv_file)
        currentBus = bus.copy()
        for row in reader:
            if(len(row)>0 and id == row[0]):
                currentBus["idBus"] = row[0]
                currentBus["lieuDepart"] = row[1].upper()
                currentBus["lieuArrive"] = row[2].upper()
                currentBus["placesMax"] = row[3]
                currentBus["poidMax"] = row[4]
                break
        return currentBus

def getBus(id, index):
    with open("bus.csv", 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if(len(row) > 0 and id == row[0]):
                targetValue = row[index]
                return int(targetValue)
        return None

def getNumberPassengersInBus(id):
    with open("passengers.csv", 'r') as csv_file:
        reader = csv.reader(csv_file)
        passengers = []
        for passenger in reader:
            if(len(passenger)>=1 and id == passenger[1]):
                passengers.append(passenger)
    return passengers

def getPassengersInBus(id):
    with open("passengers.csv", 'r') as csv_file:
        reader = csv.reader(csv_file)
        listPassengers = []
        if(id.upper() == 'a'.upper()):
            for row in reader:
                if(len(row) != 0):
                    listPassengers.append(row)
        else:
            for row in reader:
                if(len(row)>=1 and id == row[1]):
                    listPassengers.append(row)
    if(len(listPassengers) == 0):
        return None
    else:
        return listPassengers

def clear_screen():
    os.system('cls')

bus = {
    "idBus" : 0,
    "lieuDepart" : "null",
    "lieuArrive" : "null",
    "placesMax" : 0
}

if __name__ == "__main__":
    quit = False
    while quit != True:
            showMenu()
            optionMenu = input("Veuillez Choisir : ")
            # clear_screen()
            if(optionMenu == '1'):
                takeBusData()
                print("Bus Créer Avec Success")
                # clear_screen()

            elif(optionMenu == '2'):
                takePassengerData()
                print("Passager Créer Avec Success")
                # clear_screen()

            elif(optionMenu == '3' or optionMenu == '6'):
                print('''
                1. Choisir De La Liste Des Passagers
                "P" (Precedent)\n
                ''')
                option = input("Veuillez Choisir : ")
                if(option == '1'):
                    print("\n=====List De Passagers=====")
                    index = 1
                    listPassengers = getPassengersInBus('a')
                    for passenger in listPassengers:
                        if(len(passenger) != 0):
                            print(f'{index}. {passenger}')
                            index+=1
                    passengerIndex = int(input("Choisir Le Passager: "))
                    if(optionMenu == '3'):
                        newBusId = input(f"Ajouter {listPassengers[passengerIndex-1][0]} dans le bus N°... : ")
                        print(f'chosen passenger = {listPassengers[passengerIndex-1]} index = {passengerIndex}')
                        if(editPassenger(listPassengers[passengerIndex-1], newBusId)):
                            print("Modifé Avec Success")
                        else:
                            print("N'a Pas Pu Etre Modifié")
                    elif(optionMenu == '6'):
                        if(deletePassenger(listPassengers[passengerIndex-1])):
                            print("supprimé Avec Success")
                        else:
                            print("N'a as Pu Etre Suppimé.\nLe Nom du Passager n'existe Pas")
                elif(option == 'P'): continue
                clear_screen()

            elif(optionMenu == '4' or optionMenu =='5'):
                busId = input("Entrer l'id du bus :")
                if(optionMenu == '4'):
                    targetValue = getBus(busId,3)
                    if(targetValue):
                        print("\nLe nombre de places restantes est : {}".format(targetValue - len(getNumberPassengersInBus(busId))))
                        continue
                elif(optionMenu == '5'):
                    targetValue = getBus(busId, 4)
                    if(targetValue):
                        passengerLogageWeight = 0
                        for passenger in getNumberPassengersInBus(busId):
                            passengerLogageWeight += int(passenger[2])
                        print("\nLe Nombre de Kilos Reservés est de {}Kg".format(targetValue-passengerLogageWeight))
                        continue
                print("Désolé Cet Id de Bus N'existe pas")

            elif(optionMenu == '8'):
                busId = input("Entrer L'id Du Bus: ")
                passengers = getPassengersInBus(busId)
                if(passengers):
                    print("\nLa Liste Des Passagers Sur Le Bus N° {}\n{}".format(busId, passengers))
                else:
                    print("Désolé Cet Id de Bus N'existe pas")

            elif(optionMenu == '9'):
                print("\nLa Liste De Tous Les Passagers")
                passengers = getPassengersInBus('a')
                if(passengers):
                    index = 1
                    for passenger in passengers:
                        if(len(passenger) > 0):
                            print(f'{index} {passenger}')
                            index += 1
                else:
                    print("Désolé Cet Id de Bus N'existe pas")
            elif(optionMenu == '10'):
                passengerName = input("Entrer Le Nom Du Passager A Vérifier: ").upper()
                busId = input("Entrer L'id Du Bus: ")
                passengers = getPassengersInBus(busId)
                if(passengers):
                    passExists = False
                    for passenger in passengers:
                        if(passenger[0].upper() == passengerName):
                            passExists = True
                            print(f'\nDetails Of Bus.\n{getBusWithId(busId)}')
                            break
                    if(not passExists): print(f"\nIl N'existe Aucun Passager du Nom {passengerName} Dans La Flotte N°{busId}")
                else:
                    print("Désolé Cet Id de Bus N'existe pas")
            else:
                print("Saving And Exiting...")
                quit = True


