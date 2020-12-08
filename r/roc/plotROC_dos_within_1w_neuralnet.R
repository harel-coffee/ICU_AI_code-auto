library(pROC)
library(RColorBrewer)


mycols <-brewer.pal(5, "Set1")

prob_nn <- read.table("./dos_within_1w_neuralnet_24h/roc_dos_within_1w_neuralnet_24h_mean.txt",sep="\t",header=T)

roc.res.nn <- roc(prob_nn$test, prob_nn$predict)

print(pROC::auc(roc.res.nn))

rocplot <- "roc_dos_within_1w_neuralnet_24h_mean.pdf"
pdf(rocplot,useDingbats=FALSE)
plot.roc(roc.res.nn,col=mycols[1])

dev.off()