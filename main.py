###Tokenization du vocabulaire :

vocabulary = open("dico.text","r",encoding="utf-8").read()


### on va creer une liste de mots:
tokenization_vocabulary = vocabulary.split(" ")


###tokenize
f = open("dico.text","r",encoding="utf-8")
text_string = f.read()



def clean_text(string,special_character,replacement_string):
  cleaned_string = text_string

  for string in special_character:
    cleaned_string = cleaned_string.replace(string,replacement_string)
  cleaned_string = cleaned_string.lower()
  return(cleaned_string) 

clean_characters = ["Ã©",]
replacement ="é"
cleaned_text= clean_text(text_string,clean_characters,replacement)

print(cleaned_text)