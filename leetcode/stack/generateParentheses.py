def generateParenthesis(self, n):
        stack=[]
        results=[]

        def generate(opened,closed):
            if opened==0 and closed==0:
                results.append(''.join(stack))
                return
            
            if opened>0:
                #add for this sequence
                stack.append('(')
                #continue generation
                generate(opened-1,closed)
                #once all string variants are all built with this paren, pop off
                stack.pop()
            
            if closed>opened:
                stack.append(')')
                generate(opened,closed-1)
                stack.pop()
            
        generate(n,n)
        return results

#pass string as you go (this is slightly worse performan
#imo makes it slightly more intuitive for what principle this solution implements.)ce wise and uses more of a 'conceptual stack' approach (with some avoided string slicing that would be 1:1 correspondent), but 

def generateParenthesis(self, n):
        string=''
        results=[]

        def generate(opened,closed,string):
            if opened==0 and closed==0:
                results.append(string)
                return
            
            if opened>0:
                generate(opened-1,closed,string+'(')
            
            if closed>opened:
                generate(opened,closed-1,string+')')
            
        generate(n,n,'')
        return results