import random
import DFA

# machine pattern most wrote here
machine = {0:[[1,"a"],[0,"b"]],1:[[2,"b"]],2:["end"]}
# for example : 
#   this pattern is -> b*ab
 
machine2 = {0:[[0,"a"],[1,"b"]],1:[[0,"b"],[2,"a"]],2:[[2,"a"],[3,"b"]],3:["end"]}

machine3 = {0:[[0,"a"],[1,"b"]],1:[[0,"b"],[2,"a"]],2:[[2,"a"],[3,"b"]],3:[[3,"b"],[0,"a"],"end"]}


print(DFA.dfa(machine,"bbbbbbbbbab"))
print(DFA.dfa(machine,"aab"))
# Test Machine 2
print(DFA.dfa(machine2,"aaaaaaabbbaaaaaaaaaab"))
print(DFA.dfa(machine2,"aaaaaaabbbbaaaaaaaaab"))
# Test Machine 3
print(DFA.dfa(machine3,"abbabaaaaabbabab"))
print(DFA.dfa(machine3,"abbabaaaaabbababa"))
