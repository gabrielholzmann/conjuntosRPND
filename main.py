#Gabriel Holzmann Machado de Oliveira

""" Enunciado: Programa em Python no qual proporciona o resultado das operações de União(U), Interseção(I),
Diferença(D), Produto Cartesiano(C), por meio da leitura de um arquivo .txt contendo na primeira linha
a quantidade de operações, nas próximas a sequência de Operação, Conjunto 1 e Conjunto 2. """

def union(firstElement, secondElement):
  result = firstElement.copy();
    
  for i in secondElement:
    if(i not in result):
      result.append(i);
      
  return result;

def intersection(firstElement, secondElement):
  result = list();

  for i in firstElement:
    if i in secondElement:
      result.append(i);
      
  return result;

def difference(firstElement, secondElement):
  result = firstElement.copy();

  for i in secondElement:
    if i in firstElement:
      result.remove(i);

  return result;

def cartesian(firstElement, secondElement):
  result = list();

  for i in firstElement:
    for j in secondElement:
      #no element repetition
      string = f"({i},{j})";
      if string not in result:
        result.append(string);
  
  return result;

def formatText(text):
  formatedText = str(text);

  formatedText = formatedText.replace(" ", "");
  formatedText = formatedText.replace("'", "");
  formatedText = formatedText.replace("[", "{");
  formatedText = formatedText.replace("]", "}");

  return formatedText;

def main():
  while True:
    fileName = input("file name: ");
    try:
        file = open(fileName, "r");
        break;
    except IOError:
        print(f"COULD NOT OPEN FILE: {fileName}");

  numOperations = file.readline();
  
  for i in range (0, int(numOperations)):
    operation = file.readline().strip();
    firstElement = file.readline().strip().split(", ");
    secondElement = file.readline().strip().split(", ");

    result = list();
    operationText = "";

    if(operation == "U"):
      operationText = "União";
      result = union(firstElement, secondElement);
    elif(operation == "I"):
      operationText = "Interseção";
      result = intersection(firstElement, secondElement);
    elif(operation == "D"):
      operationText = "Diferença";
      result = difference(firstElement, secondElement);
    elif(operation == "C"):
      operationText = "Produto cartesiano";
      result = cartesian(firstElement, secondElement);

    #União: conjunto 1 {3,5,67,7}, conjunto 2 {1,2,3,4}. Resultado: {3,5,67,7,1,2,4} 
    print(f"{operationText}: conjunto 1 {formatText(firstElement)}, conjunto 2 {formatText(secondElement)}. Resultado: {formatText(result)}");

  file.close();

if __name__ == "__main__":
  main();
