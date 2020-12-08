library(pROC)
library(RColorBrewer)


mycols <-brewer.pal(5, "Set1")

prob_nn <- read.table("./dos_within_1w_neuralnet_24h/roc_dos_within_1w_neuralnet_24h_mean.txt",sep="\t",header=T)
prob_rf <- read.table("./dos_within_1w_randomforest_24h/roc_dos_within_1w_randomforest_24h_mean.txt",sep="\t",header=T)
prob_xgb <- read.table("./dos_within_1w_xgboost_24h/roc_dos_within_1w_xgboost_24h_mean.txt",sep="\t",header=T)

roc.res.nn <- roc(prob_nn$test, prob_nn$predict)
roc.res.rf <- roc(prob_rf$test, prob_rf$predict)
roc.res.xgb <- roc(prob_xgb$test, prob_xgb$predict)

print(pROC::auc(roc.res.nn))
print(pROC::auc(roc.res.rf))
print(pROC::auc(roc.res.xgb))

rocplot <- "roc_dos_within_1w_24h_mean.pdf"
pdf(rocplot,useDingbats=FALSE)
plot.roc(roc.res.nn,col=mycols[1])
lines.roc(roc.res.rf,col=mycols[2])
lines.roc(roc.res.xgb,col=mycols[3])

legend("bottomright", c("Neural Net", "Random Forest", "XGBoost"),
    lty=1, lwd=2, col=mycols)
dev.off()