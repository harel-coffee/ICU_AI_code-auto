library(RColorBrewer)

mycols <-brewer.pal(5, "Set1")

df_outcome1 <- read.table("../../../data/patient/outcome1_train_test.txt",sep="\t",header=T)
df_days_of_stay <- read.table("../../../data/patient/days_of_stay_train_test.txt",sep="\t",header=T)

df1 <- df_days_of_stay[df_days_of_stay$dos_within_1w == 1,]
df2 <- df_days_of_stay[(df_days_of_stay$dos_within_1w == 0)&(df_days_of_stay$dos_more_2w == 0),]
df3 <- df_days_of_stay[df_days_of_stay$dos_more_2w == 1,]
df4 <- df_outcome1[df_outcome1$outcome1 == 1,]

file_name <- "boxplot_Lac.pdf"
quartz(type="pdf", file=file_name)
boxplot(
    df1[!is.na(df1$Lac),]$Lac, 
    df2[!is.na(df2$Lac),]$Lac, 
    df3[!is.na(df3$Lac),]$Lac, 
    df4[!is.na(df4$Lac),]$Lac, 
    names=c("<=1w","1-2w",">2w","outcome1=1"),
    outline=F,
    xlab="Lac"
)

file_name <- "boxplot_LDH.pdf"
quartz(type="pdf", file=file_name)
boxplot(
    df1[!is.na(df1$LDH),]$LDH, 
    df2[!is.na(df2$LDH),]$LDH, 
    df3[!is.na(df3$LDH),]$LDH, 
    df4[!is.na(df4$LDH),]$LDH, 
    names=c("<=1w","1-2w",">2w","outcome1=1"),
    outline=F,
    xlab="LDH"
)

file_name <- "boxplot_PLT.pdf"
quartz(type="pdf", file=file_name)
boxplot(
    df1[!is.na(df1$PLT),]$PLT, 
    df2[!is.na(df2$PLT),]$PLT, 
    df3[!is.na(df3$PLT),]$PLT, 
    df4[!is.na(df4$PLT),]$PLT, 
    names=c("<=1w","1-2w",">2w","outcome1=1"),
    outline=F,
    xlab="PLT"
)

file_name <- "boxplot_NBPs.pdf"
quartz(type="pdf", file=file_name)
boxplot(
    df1[!is.na(df1$NBPs),]$NBPs, 
    df2[!is.na(df2$NBPs),]$NBPs, 
    df3[!is.na(df3$NBPs),]$NBPs, 
    df4[!is.na(df4$NBPs),]$NBPs, 
    names=c("<=1w","1-2w",">2w","outcome1=1"),
    outline=F,
    xlab="NBPs"
)

file_name <- "boxplot_UN.pdf"
quartz(type="pdf", file=file_name)
boxplot(
    df1[!is.na(df1$UN),]$UN, 
    df2[!is.na(df2$UN),]$UN, 
    df3[!is.na(df3$UN),]$UN, 
    df4[!is.na(df4$UN),]$UN, 
    names=c("<=1w","1-2w",">2w","outcome1=1"),
    outline=F,
    xlab="UN"
)

file_name <- "boxplot_HR.pdf"
quartz(type="pdf", file=file_name)
boxplot(
    df1[!is.na(df1$HR),]$HR, 
    df2[!is.na(df2$HR),]$HR, 
    df3[!is.na(df3$HR),]$HR, 
    df4[!is.na(df4$HR),]$HR, 
    names=c("<=1w","1-2w",">2w","outcome1=1"),
    outline=F,
    xlab="HR"
)

file_name <- "boxplot_CRE.pdf"
quartz(type="pdf", file=file_name)
boxplot(
    df1[!is.na(df1$CRE),]$CRE, 
    df2[!is.na(df2$CRE),]$CRE, 
    df3[!is.na(df3$CRE),]$CRE, 
    df4[!is.na(df4$CRE),]$CRE, 
    names=c("<=1w","1-2w",">2w","outcome1=1"),
    outline=F,
    xlab="CRE"
)

file_name <- "boxplot_rResp_imp.pdf"
quartz(type="pdf", file=file_name)
boxplot(
    df1[!is.na(df1$rResp_imp),]$rResp_imp, 
    df2[!is.na(df2$rResp_imp),]$rResp_imp, 
    df3[!is.na(df3$rResp_imp),]$rResp_imp, 
    df4[!is.na(df4$rResp_imp),]$rResp_imp, 
    names=c("<=1w","1-2w",">2w","outcome1=1"),
    outline=F,
    xlab="rResp_imp"
)

dev.off()