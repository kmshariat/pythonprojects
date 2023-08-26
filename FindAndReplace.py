def FindAndReplace(text, find_word, replace_word):
    
    """
    Parameters 

    text        : takes the main line or paragraph in which it will make the query.
    find_word   : the word which we are trying to replace
    replace_word: the word that will replace
    
    """
    return text.replace(find_word, replace_word)

if __name__ == "__main__":
    print(FindAndReplace("No matter how big a nation is, it is no stronger than its weakest people, and as long as you keep a person down, some part of you has to be down there to hold him down, so it means you cannot soar as you might otherwise.", "as", "are"))
