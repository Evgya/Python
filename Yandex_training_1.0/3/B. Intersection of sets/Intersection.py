_in = open('input.txt', 'r')
_out = open('output.txt', 'w')
A, B = (map(int, line.split()) for line in _in)
_out.write(" ".join(map(str, sorted(set(A) & set(B)))))
_out.close()
_in.close()
