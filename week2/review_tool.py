import pickle
from trie_netflix import TrieNode, Trie

with open("titles.pkl", "rb") as file:
    titles = pickle.load(file)
    
usr_input = input("Enter a movie title: ")
res = titles.query(usr_input)
print(res)

