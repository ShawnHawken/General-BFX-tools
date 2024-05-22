# This script uses the APE package to convrt trees that have nodes with more than 3 descendents to have 2
# this is necessary for the recombination filtering program clonalframeML

setwd("/Users/shawnwhitefield/Desktop/Snitkin_lab_Winter_2015/VRE/alignments_and_trees/VRE_alignments_and_trees")

library(ape)

#read in the trees

tree_0p5_perc<-read.tree("2015-06-04_09-41-56_SNPs_among_VRE_isolates_within_0p5_perc_ID_minDist2_noRecFilt.tree")
tree_1_perc<-read.tree("2015-06-04_12-30-23_SNPs_among_VRE_isolates_within_1_perc_ID_minDist2_noRecFilt.tree")
tree_5_perc<-read.tree("2015-06-03_23-18-58_SNPs_among_VRE_isolates_within_5_perc_ID_minDist2_noRecFilt.tree")

#convert to collapse multichotomies
multi_resolved_0p5_tree<-multi2di(tree_0p5_perc)
multi_resolved_1_tree<-multi2di(tree_1_perc)
multi_resolved_5_tree<-multi2di(tree_5_perc)

#write these new trees to files

write.tree(multi_resolved_0p5_tree, file="multi_resolved_0p5.tree")
write.tree(multi_resolved_1_tree, file="multi_resolved_1.tree")
write.tree(multi_resolved_5_tree, file="multi_resolved_5.tree")
