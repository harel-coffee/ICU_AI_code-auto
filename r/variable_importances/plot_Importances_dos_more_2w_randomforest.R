library(ggplot2)
library(RColorBrewer)

mycols <-brewer.pal(5, "Set1")

imp <- read.table("./dos_more_2w_randomforest_24h/variable_importances_dos_more_2w_randomforest_24h_mean.txt",sep="\t",header=T)

imp <- data.frame(imp)
imp <- imp[order(-imp$weight),]

data <- data.frame(
    feature = imp[1:20, "feature"],
    weight = imp[1:20, "weight"]
)

g <- ggplot(data, aes(x = reorder(feature, weight), y = weight)) + labs(x="feature", y="importance")
g <- g + geom_bar(stat = "identity", fill = mycols[2], color = mycols[2])
g <- g + coord_flip()

file_name <- "variable_importances_dos_more_2w_randomforest_24h_mean.pdf"
quartz(type="pdf", file=file_name)
theme_set(theme_bw(base_family="HiraKakuProN-W3"))

plot(g)

dev.off()