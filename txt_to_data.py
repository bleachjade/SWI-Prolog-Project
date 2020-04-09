def unique_artists():
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
            listword.clear()

def artists_location():
    with open("artists_location.txt", encoding="utf8") as f:
        for i in f:
            word = i.split("<SEP>")
            # print(word[3], "-", word[4]) ## error charmap but pretty format eg. Protokoll - Boston, MA
            print(word[3].encode("utf8"), word[4].encode("utf8")) ## no error but ugly format eg. b'Endless Blue' b'Santa Cruz\n'

def genre():
    with open("genre.txt", encoding="utf8") as f:
        for i in f:
            print(i)

unique_artists()
# artists_location()
# genre()