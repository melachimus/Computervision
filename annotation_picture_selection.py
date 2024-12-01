import os
import random
import shutil

def select_random_images(source_dir, dest_dir, sample_size):
    """
    Wählt eine zufällige Stichprobe von Bildern aus einem Verzeichnis aus und kopiert sie in einen neuen Ordner.

    :param source_dir: Pfad zum Quellverzeichnis mit den Bildern
    :param dest_dir: Pfad zum Zielverzeichnis, in das die ausgewählten Bilder kopiert werden
    :param sample_size: Anzahl der zufällig auszuwählenden Bilder
    """
    os.makedirs(dest_dir, exist_ok=True)
    all_files = os.listdir(source_dir)
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
    image_files = [file for file in all_files if os.path.splitext(file)[1].lower() in image_extensions]
    
    if sample_size > len(image_files):
        print(f"Warnung: Die Stichprobe ({sample_size}) ist größer als die Anzahl der verfügbaren Bilder ({len(image_files)}).")
        sample_size = len(image_files)
    selected_files = random.sample(image_files, sample_size)
    for file in selected_files:
        src_path = os.path.join(source_dir, file)
        dest_path = os.path.join(dest_dir, file)
        shutil.copy(src_path, dest_path)
    
    print(f"{len(selected_files)} Bilder wurden erfolgreich nach '{dest_dir}' kopiert.")

source_directory = r"C:\Users\anohl\OneDrive\Dokumente\A_Uni_stuff\Albstadt\Semester 2\Computer_vision\Aufgaben\Data\BSD\N"
destination_directory = r"C:\Users\anohl\OneDrive\Dokumente\A_Uni_stuff\Albstadt\Semester 2\Computer_vision\Aufgaben\Data\BSD\N_annotate"
sample_size_bsd = 200
select_random_images(source_directory, destination_directory, sample_size_bsd)

source_directory = r"C:\Users\anohl\OneDrive\Dokumente\A_Uni_stuff\Albstadt\Semester 2\Computer_vision\Aufgaben\Data\BSD\P"
destination_directory = r"C:\Users\anohl\OneDrive\Dokumente\A_Uni_stuff\Albstadt\Semester 2\Computer_vision\Aufgaben\Data\BSD\P_annotate"
sample_size_bsd = 200
select_random_images(source_directory, destination_directory, sample_size_bsd)

source_directory = r"C:\Users\anohl\OneDrive\Dokumente\A_Uni_stuff\Albstadt\Semester 2\Computer_vision\Aufgaben\Data\NEU_Input\train\crazing"
destination_directory = r"C:\Users\anohl\OneDrive\Dokumente\A_Uni_stuff\Albstadt\Semester 2\Computer_vision\Aufgaben\Data\NEU_Input\train\crazing_annotate"
sample_size_surface = 50
select_random_images(source_directory, destination_directory, sample_size_surface)

source_directory = r"C:\Users\anohl\OneDrive\Dokumente\A_Uni_stuff\Albstadt\Semester 2\Computer_vision\Aufgaben\Data\NEU_Input\train\inclusion"
destination_directory = r"C:\Users\anohl\OneDrive\Dokumente\A_Uni_stuff\Albstadt\Semester 2\Computer_vision\Aufgaben\Data\NEU_Input\train\inclusion_annotate"
sample_size_surface = 50
select_random_images(source_directory, destination_directory, sample_size_surface)

source_directory = r"C:\Users\anohl\OneDrive\Dokumente\A_Uni_stuff\Albstadt\Semester 2\Computer_vision\Aufgaben\Data\NEU_Input\train\patches"
destination_directory = r"C:\Users\anohl\OneDrive\Dokumente\A_Uni_stuff\Albstadt\Semester 2\Computer_vision\Aufgaben\Data\NEU_Input\train\patches_annotate"
sample_size_surface = 50
select_random_images(source_directory, destination_directory, sample_size_surface)

source_directory = r"C:\Users\anohl\OneDrive\Dokumente\A_Uni_stuff\Albstadt\Semester 2\Computer_vision\Aufgaben\Data\NEU_Input\train\pitted_surface"
destination_directory = r"C:\Users\anohl\OneDrive\Dokumente\A_Uni_stuff\Albstadt\Semester 2\Computer_vision\Aufgaben\Data\NEU_Input\train\pitted_surface_annotate"
sample_size_surface = 50
select_random_images(source_directory, destination_directory, sample_size_surface)

source_directory = r"C:\Users\anohl\OneDrive\Dokumente\A_Uni_stuff\Albstadt\Semester 2\Computer_vision\Aufgaben\Data\NEU_Input\train\rolled-in_scale"
destination_directory = r"C:\Users\anohl\OneDrive\Dokumente\A_Uni_stuff\Albstadt\Semester 2\Computer_vision\Aufgaben\Data\NEU_Input\train\rolled-in_scale_annotate"
sample_size_surface = 50
select_random_images(source_directory, destination_directory, sample_size_surface)

source_directory = r"C:\Users\anohl\OneDrive\Dokumente\A_Uni_stuff\Albstadt\Semester 2\Computer_vision\Aufgaben\Data\NEU_Input\train\scratches"
destination_directory = r"C:\Users\anohl\OneDrive\Dokumente\A_Uni_stuff\Albstadt\Semester 2\Computer_vision\Aufgaben\Data\NEU_Input\train\scratches_annotate"
sample_size_surface = 50
select_random_images(source_directory, destination_directory, sample_size_surface)

