void decode_huff(node* root, string s) {
    string s1;
    node* current = root;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '0')
            current = current->left;
        else
            current = current->right;  

        if (current != nullptr && current->left == nullptr && current->right == nullptr) { 
            cout << current->data;  
            current = root;
        }
    }
}

int main() {
    
  	string s;
    std::cin >> s;
  
    node * tree = huffman_hidden(s);
    string code = "";
  
    map<char, string> mp;
    print_codes_hidden(tree, code, mp);
    
    string coded;
  
    for(int i = 0; i < s.length(); i++) {
        coded += mp[s[i]];
    }
    
    decode_huff(tree, coded);
  
    return 0;
}