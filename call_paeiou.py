import shutil
import os
import sys

def call_paeiou(gen_folder):
    paeiou_dir_in = "PAEIOU_directory.txt"
    if (os.path.isfile(paeiou_dir_in)):
        with open(paeiou_dir_in) as infile:
            paeiou_path = infile.readline()
    else:
        paeiou_path = input("PAEIOU path: ")
        with open(paeiou_dir_in, 'w+') as outfile:
            outfile.write(paeiou_path)
    sys.path.insert(1, paeiou_path)

    import paeiou

    paeiou.direct_function( False, 
                            True, 
                            0, 
                            0, 
                            "com.pa.daedalus.experimentals", 
                            "PAEIOU_units/", 
                            "unit_add_list.txt", 
                            f"{gen_folder}/",
                            "s17")

def main():
    gen = "gen"

    if os.path.isdir(gen):
        shutil.rmtree(gen)

    shutil.copytree("export", gen, dirs_exist_ok=True)
    call_paeiou(gen)

if __name__ == '__main__':
    main()
