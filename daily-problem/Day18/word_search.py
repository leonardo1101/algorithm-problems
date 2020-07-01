class TrieNode:
  def __init__(self):
    self.children = [None] * 26
    self.end_word = False

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    word_size = len(word)
    node = self.root

    for i in range(word_size):
      index = ord(word[i]) - ord('A')
      if not node.children[index]:
        node.children[index] = TrieNode()
      node = node.children[index]
    node.end_word = True

  def word_exists(self, word):
    word_size = len(word)
    node = self.root

    for i in range(word_size):
      index = ord(word[i]) - ord('A')
      if not node.children[index]:
        return False
      node = node.children[index]

    return node.end_word

def word_search(matrix, word):
  rows = len(matrix)
  columns = len(matrix[0])
  trie = Trie()

  for i in range(rows):
    word_row = "".join(matrix[i])
    trie.insert(word_row)

    word_column = [matrix[j][i] for j in range(columns)]
    trie.insert(word_column)

  return trie.word_exists(word)    

  
matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]
print word_search(matrix, 'FOAM')
