import time
from tkinter import simpledialog
import pygame
import customtkinter
import tkinter as tk

chemin =".//repertoire_musique//"
# Créer une étiquette

series = []
timee=[]
i=0
newfenetre = tk.Tk()
newfenetre.title("WORKOUT INTERVAL TIMER")
def afficher(nbr_exo):
    global i,timee
    titre = customtkinter.CTkLabel(newfenetre, text="WORKOUT INTERVAL", font=("Helvetica", 40), text_color='Blue', width=50)
    titre.pack(pady=20)
    for i in range(1,nbr_exo+1):
        # Création du cadre pour l'exercice avec une bordure
        exercice_frame = customtkinter.CTkFrame(master=newfenetre, bg_color="blue")
        exercice_frame.pack(padx=10, pady=10, fill=tk.X)

        # Titre de l'exercice
        exercice_title = customtkinter.CTkLabel(exercice_frame, text=f"Serie {i}", text_color='Red')
        exercice_title.pack(side=tk.TOP, padx=5, pady=5)

        # Cadre pour les entrées des informations sur l'exercice
        champs_frame = customtkinter.CTkFrame(exercice_frame)
        champs_frame.pack(pady=5)

        series_label = customtkinter.CTkLabel(champs_frame, text=f"Combien d'exercice pour Serie {i} ? ")
        series_label.pack(side=tk.LEFT)
        series_entry = customtkinter.CTkEntry(champs_frame)
        series_entry.pack(side=tk.LEFT, padx=5)

        # Entrées pour les informations sur l'exercice
        exo_time_label = customtkinter.CTkLabel(champs_frame, text=f"Combien de secondes pour chaque Exercice ? ")
        exo_time_label.pack(side=tk.LEFT)
        exo_time_entry = customtkinter.CTkEntry(champs_frame)
        exo_time_entry.pack(side=tk.LEFT, padx=5)



        rest_label = customtkinter.CTkLabel(champs_frame,
                                            text=f"Combien de secondes de repos entre les exercices ? ")
        rest_label.pack(side=tk.LEFT)
        rest_entry = customtkinter.CTkEntry(champs_frame)
        rest_entry.pack(side=tk.LEFT, padx=5)

        series.append((exo_time_entry, rest_entry, series_entry))
        i += 1

        # Champ pour les secondes de repos entre les exercices
    exercise_rest_time_label = customtkinter.CTkLabel(master=newfenetre, text_color='BLACK',
                                                      text="Combien de secondes de repos entre les series ? ")
    exercise_rest_time_label.pack(side=tk.TOP, padx=5, pady=5)
    exercise_rest_time_entry = customtkinter.CTkEntry(master=newfenetre)
    exercise_rest_time_entry.pack(padx=5, pady=5)
    timee.append(exercise_rest_time_entry)
    lb = customtkinter.CTkLabel(master=newfenetre, text="",text_color='red',fg_color='lightgray')
    lb.pack(pady=5)
    lb1 = customtkinter.CTkLabel(master=newfenetre, text="",text_color='red')
    lb1.pack(pady=5)
    lb2 = customtkinter.CTkLabel(master=newfenetre, text="",text_color='red')
    lb2.pack(pady=5)
    lb3 = customtkinter.CTkLabel(master=newfenetre, text="", text_color='black')
    lb3.pack(pady=5)

    button_start = customtkinter.CTkButton(master=newfenetre, text="start", command=lambda: verify(lb, lb1, lb2,lb3))
    button_start.pack(pady=5)


def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)


def exercise_timer(e, r, s,lb1,lb2):
    global chemin
    if True:
        for se in range(s):
            text=f"Exercice {se + 1}:"
            lb1.configure(text=text)
            newfenetre.update()
            for t in range(int(e+1)):
                x=e-t
                lb2.configure(text=f"Temps restant dans l'Exercice : {x} secondes")
                newfenetre.update()
                time.sleep(1)

            if se != s - 1:
                for i in range(int(r+1)):
                    x=int(r)-i
                    lb2.configure(text=f"Repos de {x} secondes avant la prochaine Exercice.")
                    newfenetre.update()
                    time.sleep(1)
            play_sound(chemin+"repos.mp3")
    else:
        print("erreur")


def training_program(lb,lb1,lb2,lb3):
    global series,timee,chemin
    for idx, exercise in enumerate(series):
        lb.configure(text=f"Préparez-vous pour Serie {idx + 1}")
        newfenetre.update()
        time.sleep(1)  # Temps de préparation de 5 secondes
        play_sound(chemin+"Debut.mp3")
        exo = exercise[0].get()
        rest = exercise[1].get()
        ser = exercise[2].get() # Vérifie si la chaîne n'est pas vide
        e=int(exo)
        r = int(rest)
        s = int(ser)
        exercise_timer(e, r, s, lb1,lb2)
        timer_repos = timee[0].get()
        timer=int(timer_repos)
        if idx != len(series) - 1:
            for t in range(timer+1):
                x=timer-t
                lb3.configure(text=f"Repos de {x} secondes avant Serie suivant.")
                newfenetre.update()
                time.sleep(1)


        lb1.configure(text="")
        lb2.configure(text="")
        lb.configure(text="Entraînement terminé !")
        lb3.configure(text="")
        newfenetre.update()


def verify(lb,lb1,lb2,lb3):
    global timee
    test=timee[0].get()
    if(test.strip()):
        if(int(test)>0):
            training_program(lb,lb1,lb2,lb3)
        else:
            pass


def test():
    nbr_exo = simpledialog.askinteger("Nombre d'exercices", "Combien d'exercices voulez-vous faire ? ")
    afficher(nbr_exo)
newfenetre.after(1000,test)

# newfenetre.after(2000, test)
newfenetre.mainloop()

# if idx > len(series) - 1:
#     j = int(timee[0].get()) + 1
#     for ii in range(j):
#         x = j - ii
#         lb2.configure(f"Repos de {x} secondes avant Serie suivant.")
#         newfenetre.update()
#         time.sleep(1)

