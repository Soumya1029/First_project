import nltk
from nltk.metrics import edit_distance
from nltk.corpus import brown, words as nltk_words
from collections import defaultdict
import time
import re

# Download required NLTK resources
print("Downloading required NLTK resources...")
nltk.download('brown')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('words')

class EnhancedSpellChecker:
    def __init__(self):
        print("Initializing enhanced spell checker...")
        start_time = time.time()
        
        # Common misspellings dictionary
        self.common_misspellings = {
            # IE/EI rules
            'thier': 'their',
            'recieve': 'receive',
            'beleive': 'believe',
            'peice': 'piece',
            'yeild': 'yield',
            'feild': 'field',
            'feilds': 'fields',
            'acheive': 'achieve',
            'freind': 'friend',
            'wierd': 'weird',
            
            # Double consonants
            'occurr?ed': 'occurred',
            'begining': 'beginning',
            'comitted': 'committed',
            'occurence': 'occurrence',
            
            # Silent letters
            'goverment': 'government',
            'enviroment': 'environment',
            'buisness': 'business',
            
            # Common typos
            'seperate': 'separate',
            'definately': 'definitely',
            'publically': 'publicly',
            'occured': 'occurred',
            'untill': 'until',
            'ocupied': 'occupied',
            'accomodate': 'accommodate',
            'embarass': 'embarrass',
            'maintainance': 'maintenance',
            'persistant': 'persistent',
            'presense': 'presence',
            'priviledge': 'privilege',
            'procede': 'proceed',
            'truely': 'truly',
            'wether': 'whether'
        }
        
        # Spelling rules patterns
        self.spelling_rules = [
            # I before E except after C
            (r'(?<!c)ie', 'ei'),
            (r'cei', 'cie'),
            
            # Double consonant patterns
            (r'(\w)(\w)\1ing$', r'\1\2ing'),  # running -> runing
            
            # Silent E patterns
            (r'(\w)e(able|ible)$', r'\1\2'),  # liveable -> livable
            
            # Common suffix patterns
            (r'(\w)ly$', r'\1ly'),  # publically -> publicly
            (r'(\w)ally$', r'\1ally')  # basically -> basicaly
        ]
        
        # Load word sets from multiple sources
        self.word_freq = defaultdict(int)
        self.pos_words = defaultdict(set)
        self.common_words = set()
        
        # Process Brown corpus
        brown_words = brown.words()
        tagged_words = nltk.pos_tag(brown_words)
        
        # Load NLTK words
        extra_words = set(w.lower() for w in nltk_words.words())
        
        # Build frequency distributions
        print("Building word dictionaries...")
        for word, pos in tagged_words:
            word_lower = word.lower()
            self.word_freq[word_lower] += 1
            
            simple_pos = self._simplify_pos_tag(pos)
            if simple_pos:
                self.pos_words[simple_pos].add(word_lower)
            
            if self.word_freq[word_lower] > 10:
                self.common_words.add(word_lower)
        
        # Add NLTK words
        for word in extra_words:
            if word not in self.word_freq:
                self.word_freq[word] = 1
        
        # Add common misspellings corrections to word frequency
        for correct in self.common_misspellings.values():
            if correct not in self.word_freq:
                self.word_freq[correct] = 10
        
        self.correction_cache = {}
        
        print(f"Initialization completed in {time.time() - start_time:.2f} seconds")
    
    def _simplify_pos_tag(self, penn_tag):
        tag_mapping = {
            'NN': 'NOUN', 'NNS': 'NOUN', 'NNP': 'PROPN', 'NNPS': 'PROPN',
            'VB': 'VERB', 'VBD': 'VERB', 'VBG': 'VERB', 'VBN': 'VERB',
            'JJ': 'ADJ', 'JJR': 'ADJ', 'JJS': 'ADJ',
            'RB': 'ADV', 'RBR': 'ADV', 'RBS': 'ADV'
        }
        return tag_mapping.get(penn_tag, None)

    def _apply_spelling_rules(self, word):
        """Apply common spelling rules to suggest corrections"""
        word_lower = word.lower()
        
        # Check common misspellings first
        if word_lower in self.common_misspellings:
            return self.common_misspellings[word_lower]
        
        # Apply spelling rules
        for pattern, replacement in self.spelling_rules:
            if re.search(pattern, word_lower):
                suggestion = re.sub(pattern, replacement, word_lower)
                if suggestion in self.word_freq:
                    return suggestion
        
        return word

    def correct_word(self, word, pos_tag):
        # Check cache
        cache_key = (word.lower(), pos_tag)
        if cache_key in self.correction_cache:
            return self.correction_cache[cache_key]
        
        word_lower = word.lower()
        
        # Don't correct proper nouns, short words, or common words
        if pos_tag == 'PROPN' or len(word) < 2 or word_lower in self.common_words:
            return word
        
        # Check if it's a common misspelling
        corrected = self._apply_spelling_rules(word)
        if corrected != word:
            return corrected
        
        # If word exists with sufficient frequency, keep it
        if self.word_freq[word_lower] > 5:
            return word
        
        # Find closest match
        candidates = self.pos_words.get(pos_tag, set()) or self.word_freq.keys()
        best_word = word
        min_distance = float('inf')
        
        for candidate in candidates:
            if abs(len(candidate) - len(word_lower)) <= 2:
                distance = edit_distance(word_lower, candidate)
                if distance < min_distance and distance <= 2:
                    min_distance = distance
                    best_word = candidate
        
        # Preserve original capitalization
        if word[0].isupper():
            best_word = best_word.capitalize()
        
        # Cache result
        self.correction_cache[cache_key] = best_word
        return best_word

    def correct_sentence(self, sentence):
        try:
            words = nltk.word_tokenize(sentence)
            tagged_words = nltk.pos_tag(words)
            
            corrected_words = []
            for word, pos in tagged_words:
                if word.isalpha():
                    simple_pos = self._simplify_pos_tag(pos)
                    corrected_word = self.correct_word(word, simple_pos or 'NOUN')
                    corrected_words.append(corrected_word)
                else:
                    corrected_words.append(word)
            
            # Fix capitalization
            for i in range(len(corrected_words)):
                if i == 0 or (i > 0 and corrected_words[i-1].strip() in {'.', '?', '!'}):
                    corrected_words[i] = corrected_words[i].capitalize()
            
            return ' '.join(corrected_words)
            
        except Exception as e:
            print(f"Error processing sentence: {str(e)}")
            return sentence

    def correct_text_file(self, input_file, output_file, batch_size=100):
        try:
            print(f"Processing {input_file}...")
            start_time = time.time()
            
            with open(input_file, 'r', encoding='utf-8') as infile:
                lines = infile.readlines()
            
            corrected_lines = []
            total_lines = len(lines)
            
            for i in range(0, total_lines, batch_size):
                batch = lines[i:i+batch_size]
                corrected_batch = [self.correct_sentence(line.strip()) for line in batch]
                corrected_lines.extend(corrected_batch)
                
                progress = min(100, (i + batch_size) / total_lines * 100)
                print(f"Progress: {progress:.1f}%")
            
            with open(output_file, 'w', encoding='utf-8') as outfile:
                outfile.write('\n'.join(corrected_lines))
            
            print(f"Completed in {time.time() - start_time:.2f} seconds")
            print(f"Corrected text written to {output_file}")
            
        except FileNotFoundError:
            print(f"Error: Could not find input file {input_file}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        input_filename = 'spelledwrogn.txt'
        output_filename = 'notspelledwrong.txt'
        
        spell_checker = EnhancedSpellChecker()
        spell_checker.correct_text_file(input_filename, output_filename)
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")