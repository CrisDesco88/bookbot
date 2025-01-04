path_to_file = "books/frankenstein.txt"


def count_caracters(text):
  char_count = {}
  text = text.lower()
  for char in text:
    if char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1
  return char_count
      
def make_report(dict):
  list_dict = [{'char': k, 'num': v} for k,v in dict.items()]
  return list_dict
        
      
def main():
    with open(path_to_file) as f:
        file_contents = f.read()
    string = str(file_contents)    
    words = string.split() 
    conteo = len(words)
    result = count_caracters(file_contents)
    list = make_report(result)
    print(result)   
    print(conteo)
    print(list)
    
    
    
main()