#Non-stack based solution
def evalRPN(self, tokens):
    iter=0
    while len(tokens)!=1:
        if tokens[iter] in "+-*/":
            result='('+tokens[iter-2]+tokens[iter]+tokens[iter-1]+')'
            if tokens[iter]=="/":
                result= "int({})".format(result)
            tokens=tokens[:iter-2]+[str(eval(result))]+tokens[iter+1:]
            iter-=2
        else:
            iter+=1
    return int(tokens[0])

#stack based approach: when seeing operator, pop off two vals from top and use for equation.
#then push this value to top of stack
# 
# otherwise, push to stack 