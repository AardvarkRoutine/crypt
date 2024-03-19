def crypt(string, shift):
    # Leerer String, um die verschlüsselte/entschlüsselte Nachricht zu speichern
    result = ""
    
    # Schleife durch jeden Buchstaben in der Eingabezeichenkette
    for char in string:
        if char.isalpha():  # Überprüft, ob der aktuelle Zeichen ein Buchstabe ist
            offset = ord('A') if char.isupper() else ord('a')  # Offset für Groß- und Kleinbuchstaben
            result += chr((ord(char) - offset + shift) % 26 + offset)  # Verschlüsselung/Entschlüsselung unter Berücksichtigung des Offsets
        else:
            result += char  # Fügt Nicht-Buchstaben unverändert hinzu
    return result


while True:
    # Eingabe der Nachricht, des Offsets und der Richtung (verschlüsseln oder entschlüsseln)
    prompt = str(input("Nachricht: "))
    prompt_offset = str(input("Offset: "))
    offset = 0
    prompt_direction = str(input("d for decrypt OR e for encrypt: "))

    if 'd' in prompt_direction:
        offset = int(prompt_offset)  # Offset für Entschlüsselung
    elif 'e' in prompt_direction:
        offset = -abs(int(prompt_offset))  # Offset für Verschlüsselung
    else:
        print("You fucked up!")  # Ausgabe, wenn die Eingabe ungültig ist
        exit()

    print(crypt(prompt, offset))  # Aufruf der Funktion zur Verschlüsselung/Entschlüsselung und Ausgabe des Ergebnisses
