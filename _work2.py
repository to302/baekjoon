f = "-101 + -11*( -10 / 2.5 ) + -3 "
stk = []
_t = ""
for c in f:
    if (c.isspace()):
        continue
    elif (c.isdigit() or c == "."):
        _t += c
    elif c in "+-*/()":
        if c == "-":
            if (len(stk) < 1 or stk[-1] in "+-*/()"):
                _t += c
                continue
                
        if (_t != ""):
            stk.append(_t)
            _t = ""
        stk.append(c)

stk.append(_t)
        
print(stk)       
print(eval("".join(stk)))
print(eval(f))