# FP-Growth

Many techniques have been proposed to further improve the performance of
frequent itemset mining algorithms. Taking FP-tree– based frequent pattern
growth algorithms (e.g., FP-growth) as an example, implement one of the fol-
lowing optimization techniques.
• Top-Down Projection Technique : The conventional approach in-
volves using a bottom-up projection technique to generate conditional
pattern bases . However, one can develop a top-down projection tech-
nique, that is, project onto the suffix path of an item p in the generation
of a conditional pattern base. This may or may not improve the perfor-
mance and hence in improved implementations, a case handling is done
to use either of the projection techniques .
• Merging strategy : It is time and space consuming to generate nu-
merous conditional pattern bases during pattern-growth mining. An in-
teresting alternative is to push right the branches that have been mined
for a particular item p, that is, to push them to the remaining branch(es)
of the FP-tree. This is done so that fewer conditional pattern bases have
to be generated and additional sharing can be explored when mining the
remaining FP-tree branches.


Tasks :
• Implement the entire FP-growth algorithm in any of the allowed languages
using any 1 of the above strategies . Run the algorithm on few datasets
from the given dataset library .
• Explain clearly how have you used any of the optimisation in your algo-
rithm.
• Compare the performance of your new implementation with the unopti-
mised version.
