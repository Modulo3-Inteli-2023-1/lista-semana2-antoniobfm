#  Se achar necessario, faça import de outras bibliotecas

# Crie a função que será avaliada no exercício aqui
def conta_palavras_unicas(texto):
    # Remove pontuações, transforma tudo em letras minúsculas e depois separa as palavras
    palavras = ''.join([c if c.isalnum() or c.isspace() else ' ' for c in texto]).lower().split()
    
    # Usa um conjunto (set) para armazenar palavras únicas e retorna seu tamanho
    return len(set(palavras))

# Teste a sua função aqui (caso ache necessário)
