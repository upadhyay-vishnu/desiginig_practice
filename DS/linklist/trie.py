class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_node = False


class Trie:
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def char_index(self, ch):
        return ord(ch) - ord('a')

    def get_char(self, num):
        return chr(num + int(ord('a')))

    def insert(self, key):
        ptr = self.root
        for _char in key:
            _index = self.char_index(_char)
            print(_char)
            if not ptr.children[_index]:
                ptr.children[_index] = self.get_node()
            ptr = ptr.children[_index]

        ptr.is_end_node = True

    def search(self, key):
        ptr = self.root
        for _char in key:
            _index = self.char_index(_char)
            if not ptr.children[_index]:
                return False
            ptr = ptr.children[_index]
        return True if ptr.is_end_node else False

    def is_starts_with(self, word, key):
        i = 0
        ptr = self.root
        _index = self.char_index(word[i])
        while i < len(key):
            if _index == self.char_index(key[i]) and ptr.children[_index]:
                ptr = ptr.children[_index]
                i += 1
                continue
            else:
                return False
        return True

    def display_all_chars(self, ptr):
        # print(ptr)
        for _index in range(26):
            if ptr.children[_index]:
                print(self.get_char(_index + 97), end='-')
                self.display(ptr.children[_index])
        return

    def has_child(self, root):
        for i in range(26):
            if root.children[i]:
                return True

    def display_util(self, root, visited, word):
        _index = 0
        while _index < 26:
            if root.children[_index]:
                word += chr(_index + 97)
                if not root.children[_index].is_end_node:
                    self.display_util(root.children[_index], visited, word)
                    word = word[0:len(word) - 1]
                else:
                    if word not in visited:
                        visited.append(word)
                    if self.has_child(root.children[_index]):
                        self.display_util(root.children[_index], visited, word)
                        word = word[0:len(word) - 1]
            _index += 1

    def display(self, ptr=None, word=''):
        ptr = ptr if ptr else self.root
        visited = []
        self.display_util(ptr, visited, word)
        # print(visited)
        for i in range(len(visited)):
            print(visited[i])

    def auto_complete(self, word):
        ptr = self.root
        for _ch in word:
            _index = self.char_index(_ch)
            if not ptr.children[_index]:
                return
            ptr = ptr.children[_index]
        self.display(ptr, word)

    def delete_word(self, ptr, word, start_idx):
        if ptr.is_end_node:
            return ptr
        _index = self.char_index(word[start_idx])
        if not ptr.children[_index]:
            self.delete_word()

    def delete_key(self, key, ptr):
        """
        search if key exists
        if key exists then it must has is_end_node at last char
        if yes and has child, then mark is_end_node True
        if yes and don't have child, then delete
        """
        for _ch in key:
            _index = self.char_index(_ch)
            if not ptr.children[_index]:
                print("Key doesn't exist")
                return
            ptr = ptr.children

        if self.has_child(ptr):
            ptr.is_end_node = False
        else:
            pass

    def lcp_util(self, root, word):
        i = 0
        while i < 26:

            if root.children[i]:
                word += self.get_char(i)
                if root.is_end_node:
                    return word
                # if self.has_child(root.children[i]):
                #     return word
                # else:
                self.lcp_util(root.children[i], word)
            i += 1
        return word

    def lcp(self):
        root = self.root
        word = self.lcp_util(root, '')
        return word


if __name__ == "__main__":
    # keys = ["the","a", "there","bye","any","by","their","answer"]
    keys = ["geeksforgeeks", "geeks", "geek", "geezer"]
    # keys = ["the"]
    t = Trie()
    for key in keys:
        t.insert(key)

    print("searching for the-->", t.search('the'))
    print("searching for the-->", t.search('therea'))
    # print("startswith ti -->", t.is_starts_with('the', 'ti'))

    t.display()
    print(t.lcp())
    # t.auto_complete("th")
    # t.delete_word("the")
