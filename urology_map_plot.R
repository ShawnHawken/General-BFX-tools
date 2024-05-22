# plot a urology map of the US
library(maps)
library(mapdata)
library(mapplots)
library(colorRamp)
library(ggmap)

urology<-read.table("Desktop/urology.txt")
#clean up data
urology<-urology$V1[ c(rep(TRUE,3),FALSE)] # delete every 4th row

urology<-urology[ c(rep(FALSE,2),TRUE)] #keep every 3rd row = percent

urology<-as.data.frame(urology) #make into dataframe

#remove alaska and hawaii
urology<-urology[c(-11,-1),]
urology$

rbPal <- colorRampPalette(c("white","blue","red")) #create color pallette
urology$Col <- rbPal(6)[as.numeric(cut(urology$urology,breaks = c(0,5,10,20,30,40)))] #plot

leg.txt <- c("0-5%", "5-10%", "10-20%", "20-30%", "Over 30%")
map("state",interior = FALSE, fill = T, col=urology$Col)

map("world", "USA:hawaii", add=T)
map("world", c("USA:Alaska", add=T
legend("bottom", leg.txt, horiz = TRUE, fill = urology$Col, cex=.5)
title("Percentage of Urologists", cex=.8)


map("world", c("USA", "hawaii"),interior=T,fill=T, xlim = c(-180, -65), ylim = c(19, 72))


urology$colorBuckets <- c(5,10,20,30)))
leg.txt <- c("<2%", "2-4%", "4-6%", "6-8%", "8-10%", ">10%")
