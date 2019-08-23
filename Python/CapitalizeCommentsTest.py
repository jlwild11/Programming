import re


def sentence_case(text):
    # Split into sentences. Therefore, find all text that ends
    # with punctuation followed by white space or end of string.
    sentences2 = re.findall('[^.!?]+[.!?](?:\s|\Z)', text)
 
    # Capitalize the first letter of each sentence
    sentences3 = [x[0].upper() + x[1:] for x in sentences2]
 
    # Combine sentences
    return ''.join(sentences3)
 
comment = 'hello world. i know you hear me! where are you'

def add_period(text):
    sentences = text + "."
    return sentences

print(comment)
print(add_period(comment))
print(sentence_case(comment))
new_comment = add_period(comment)
print(sentence_case(new_comment))


