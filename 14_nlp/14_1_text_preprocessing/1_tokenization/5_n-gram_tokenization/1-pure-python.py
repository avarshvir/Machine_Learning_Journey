def generate_ngrams(text, n):
    words = text.split()
    return [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]

text = "Machine Learning is Powerful"
print(generate_ngrams(text, 2))
print("---------------------------")
print(generate_ngrams(text, 3))

"""
def generate_ngrams_detailed(text, n):
    print(f"Input: '{text}', n={n}")
    
    # Step 1: Split into words
    words = text.split()
    print(f"Step 1 - Words: {words}")
    # Output: ['I', 'love', 'python', 'programming']
    
    # Step 2: Initialize ngrams list
    ngrams = []
    
    # Step 3: Calculate iterations
    total_iterations = len(words) - n + 1
    print(f"Step 2 - Total iterations: {total_iterations}")
    # Output: 4 - 2 + 1 = 3
    
    # Step 4: Loop through each starting position
    for i in range(total_iterations):
        print(f"\nIteration {i}:")
        
        # Step 5: Get word window
        word_window = words[i:i+n]
        print(f"  Word window (words[{i}:{i+n}]): {word_window}")
        # Iteration 0: words[0:2] = ['I', 'love']
        # Iteration 1: words[1:3] = ['love', 'python'] 
        # Iteration 2: words[2:4] = ['python', 'programming']
        
        # Step 6: Join words
        ngram = ' '.join(word_window)
        print(f"  Joined ngram: '{ngram}'")
        # Iteration 0: 'I love'
        # Iteration 1: 'love python'
        # Iteration 2: 'python programming'
        
        # Step 7: Add to list
        ngrams.append(ngram)
        print(f"  Current ngrams: {ngrams}")
    
    # Step 8: Return result
    print(f"\nFinal ngrams: {ngrams}")
    return ngrams

# Test the function
text = "I love python programming"
result = generate_ngrams_detailed(text, 2)
"""