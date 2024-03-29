def RabinKarpAlgorithm(text, pattern, d, q):
    n = len(text)
    m = len(pattern)
    h = pow(d, m - 1) % q
    p = 0  # Hash value for the pattern
    t = 0  # Hash value for the text provided
    result = []

    # Preprocessing: Calculation of hash values for the pattern
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for s in range(n - m + 1):
        if p == t:
            if text[s:s + m] == pattern:
                result.append(s)
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q

            if t < 0:
                t = t + q

    return result


d = 256
q = 101  # it is going to reduce the likelihood of hash collisions = spurious hits

#user input
text = input("Enter the text: ")
pattern = input("Enter the pattern: ")


matches = RabinKarpAlgorithm(text, pattern, d, q)

if matches:
    print(f"Here are the matches: {matches}")
else:
    print("No matches")