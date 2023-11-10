import shutil
import os
import os.path
import paeiou

with open("pa_location.txt") as infile:
    pa_path = os.path.join(infile.readline(), "media/")

gen = "gen"

def main():
    if os.path.isdir(gen):
        shutil.rmtree(gen)

    shutil.copytree("export", gen, dirs_exist_ok=True)

    paeiou.paeiou( 
        mod_id = "com.pa.daedalus.experimentals", 
        paeiou_unit_path = "PAEIOU_units/", 
        unit_add_list = "unit_add_list.txt", 
        output_path = f"{gen}/",
        mod_prefix = "s17",
        server = True,
        client = False,
        pa_path = pa_path
    )

if __name__ == '__main__':
    main()
