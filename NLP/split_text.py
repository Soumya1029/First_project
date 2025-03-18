def is_abbreviation(word):
    # Common abbreviations that end with a period
    abbreviations = {'mr.', 'mrs.', 'dr.', 'prof.', 'sr.', 'jr.', 'vs.', 'etc.', 'i.e.', 'e.g.'}
    # Check for initials pattern (like N.L.P.)
    if all(c == '.' or c.isupper() for c in word):
        return True
    return word.lower() in abbreviations

def split_into_sentences(text):
    sentences = []
    current_sentence = ""
    words = text.replace('\n', ' ').split(' ')
    
    i = 0
    while i < len(words):
        current_word = words[i].strip()
        
        if not current_word:  # Skip empty words
            i += 1
            continue
            
        current_sentence += current_word
        
        # Check if this word ends with a period
        if current_word.endswith('.'):
            # Check if it's not an abbreviation
            if not is_abbreviation(current_word):
                sentences.append(current_sentence.strip())
                current_sentence = ""
            else:
                current_sentence += " "
        # Check for other sentence endings
        elif current_word.endswith('!') or current_word.endswith('?'):
            sentences.append(current_sentence.strip())
            current_sentence = ""
        else:
            current_sentence += " "
        
        i += 1
    
    # Add any remaining text as a sentence
    if current_sentence.strip():
        sentences.append(current_sentence.strip())
    
    return sentences

# Read input file
input_filename = "sample.txt"  # Replace with your input file name
output_filename = "output.txt"  # Replace with your output file name

try:
    with open(input_filename, 'r') as file:
        text = file.read()
    
    # Get sentences
    sentences = split_into_sentences(text)
    
    # Write to output file
    with open(output_filename, 'w') as file:
        for sentence in sentences:
            file.write(sentence + '\n')
    
    print(f"Sentences have been written to {output_filename}")

except FileNotFoundError:
    print(f"Error: The file {input_filename} was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")