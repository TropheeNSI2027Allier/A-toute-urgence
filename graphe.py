carte = {
    "Hopital_Central": {"Place_Nord": 3, "Avenue_Sud": 4},
    "Place_Nord": {"Hopital_Central": 3, "Quartier_Industriel": 5, "Pont_Ouest": 2, "Pont_Est": 7},
    "Avenue_Sud": {"Hopital_Central": 4, "Pont_Ouest": 3, "Zone_Commerciale": 4},
    "Pont_Ouest": {"Place_Nord": 2, "Avenue_Sud": 3, "Rive_Gauche": 6},
    "Pont_Est": {"Rive_Droite": 5, "Place_Nord": 7},
    "Quartier_Industriel": {"Place_Nord": 5, "Rive_Gauche": 4},
    "Zone_Commerciale": {"Avenue_Sud": 4},
    "Rive_Gauche": {"Pont_Ouest": 6, "Quartier_Industriel": 4},
    "Rive_Droite": {"Pont_Est": 5}
}

if __name__ == "__main__":
    print("graphe ok")
