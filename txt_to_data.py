def unique_artists():
    f2 = open("artists_prolog.txt", 'w')
    with open("unique_artists.txt", encoding="utf8") as f:
        for i in f:
            listword = []
            word = i.split("<SEP>")
            # print(f"artist({word[3]}).")
            for a in word[3]:
                if a == " ":
                    a = "-"
                if a == "\n":
                    a = ""
                listword.append(a)
            
            new_word = "".join(listword)
            print(f"artist({new_word.lower()}).")
            f2.write(f"artist({new_word.lower()}). \n")
            listword.clear()
            



def artists_location():
    f2 = open("artists_location_prolog.txt", 'w')
    with open("artists_location.txt", encoding="utf8") as f:
        for i in f:
            listword = []
            word = i.split("<SEP>")
            # print(word[3], "-", word[4]) ## error charmap but pretty format eg. Protokoll - Boston, MA
            print(word[3], word[4]) ## no error but ugly format eg. b'Endless Blue' b'Santa Cruz\n'

            for a in word[3]:
                if a == " ":
                    a = "-"
                if a == "\n":
                    a = ""
                listword.append(a)
            
            listword.append(",")

            for a in word[4]:
                if a == " ":
                    a = ""
                if a == "\n":
                    a = ""
                listword.append(a)
            
            
            new_word = "".join(listword)
            print(f"artist-location({new_word.lower()}).")
            f2.write(f"artist-location({new_word.lower()}). \n")
            listword.clear()

def genre():
    with open("genre.txt", encoding="utf8") as f:
        for i in f:
            print(i)

# unique_artists()
artists_location()
# genre()