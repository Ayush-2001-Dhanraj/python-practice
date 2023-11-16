import sys
from loadFile import load_strings
import random

names = load_strings(sys.argv[1])

search_names = ["Zuzana", "Aaren", "Nancie", "Elida", "Guy", "Ginger", "Ayush", "Jamey", "Amiee", "Lacresha", "Leonia", "Carina", "Renee", "Andrew", "Gina", "Deandra", "Desmond", "Magda", "Tawana Srivastava", "Tammi Todman", "Harley Mussell", "Iola Bordenet", "Edwardo Khela", "Myles Deanne", "Elden Dohrman", "Ira Hooghkirk", "Eileen Stigers", "Mariann Melena", "Maryrose Badura", "Ardelia Koffler", "Lacresha Kempker", "Charlyn Singley", "Lekisha Tawney", "Christena Botras", "Mike Blanchet", "Cathryn Hinkson", "Errol Shinkle", "Mavis Bhardwaj", "Sung Filipi", "Keiko Dedeke", "Lorelei Morrical", "Jimmie Lessin", "Adrianne Hercules", "Latrisha Haen", "Denny Friedeck", "Emmett Whitesell", "Sina Sauby", "Melony Engwer", "Alina Reichel", "Rosamond Shawe", "Elinore Benyard", "Sang Bouy", "Ed Aparo", "Sheri Wedding", "Sang Snellgrove", "Shaquana Sones", "Elvia Motamed", "Candice Lucey", "Sibyl Froeschle", "Ray Spratling", "Cody Mandeville", "Donita Cheatham", "Darren Later", "Johnnie Stivanson", "Enola Kohli", "Leann Muccia", "Carey Philps", "Suellen Tohonnie", "Evelynn Delucia", "Luz Kliment", "Lettie Jirjis", "Francene Klebe", "Margart Scholz", "Sarah Growden", "Glennis Gines", "Rachael Ojima", "Teofila Stample", "Narcisa Shanley", "Gene Lesnick", "Malena Applebaum", "Norma Tingey", "Marianela Mcmullen", "Rosalva Dosreis", "Dallas Heinzmann", "Sade Streitnatter", "Lea Pelzel", "Judith Zwahlen", "Hope Vacarro", "Annette Ayudan", "Irvin Cyree", "Scottie Levenstein", "Agustina", "Kira", "Fawn", "Jamal", "Karen", "Kit", "Steven", "Mary", "Alonso"]

for i in range(0, len(search_names)):
    index = search_names[i].find(' ')
    if index != -1:
        search_names[i] = search_names[i][:index]

def linear_search_names(search_space, search_item):
    for entry in search_item:
        for i in range(0, len(search_space)):
            if search_space[i] == entry:
                print(entry, i + 1)
                break

linear_search_names(names, search_names)