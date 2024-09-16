def breakify(list):
    final_list = '<br>'.join(list)
    return final_list

lines = ["Haiku frogs in snow",
         "A limerick came from Nantucket",
         "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]
print(breakify(lines))
