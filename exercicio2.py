#  Se achar necessario, faça import de outras bibliotecas

# Crie a função que será avaliada no exercício aqui
def is_anagram(string1, string2):
    # Remove espaços e transforma tudo em letras minúsculas
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()
    
    # Retorna True se as strings ordenadas forem iguais
    return sorted(string1) == sorted(string2)

# Teste a sua função aqui (caso ache necessário)
