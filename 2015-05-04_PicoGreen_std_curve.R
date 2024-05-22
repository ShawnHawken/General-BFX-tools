# R code to make standard curve to figure out concentrations from fluorometer readings
# using picogreen
# Written by Shawn Whitefield April 2015


#SETUP WORKSPACE
setwd("path/to/parsed/spec/files")
library(xlsx)
#ENTER CONCENTRATIONS FOR STANDARDS
#this is the high concentration curve
concentrations<-c(1,1,.1,.1,.01,.01,.001,.001,0,0)

#READ IN DATA AND MAKE DATAFRAMES FROM THE STANDARD AND EXPERIMENT MEASUREMENTS
  #standard plate
  #add concentrations to dataframe
standardPlate<-read.delim("./std_plate.txt", header=F)
standardPlate<-standardPlate[,-13:14]
colnames(standardPlate)<-(1:12)
fluorescence<-rapply(standardPlate[1:2,1:5],c)

# MAKE DATAFRAME OF CONCENTRATIONS AND FLUORESCENCE
standardPlate<-as.data.frame(cbind(concentrations, fluorescence))
colnames(standardPlate)<-c('concentrations', 'fluorescence')

#EXPERIMENT PLATE
experimentPlate<-read.delim("./experiment_plate.txt", header=F)
experimentPlate<-experimentPlate[,-c(13:14)]
colnames(experimentPlate)<-(1:12)

# SETUP DATAFRAME TO ENTER INTO MODEL
fluorescence<-rapply(experimentPlate,c)
experimentPlate<-as.data.frame(fluorescence)
experimentPlate$cell<-1:96
rownames(experimentPlate)<-NULL

#LOOK AT CORRELATION BETWEEN FLUORESCENCE AND CONCENTRATION FOR STANDARDS
cor.test(standardPlate$fluorescence,standardPlate$concentrations)

#MAKE MODEL TO PREDICT FROM WITH STANDARDS
standardGLM<-glm(concentrations ~ fluorescence, data =standardPlate)
summary(standardGLM)

#CALCULATE EXPERIMENT PLATE CONCENTRATIONS
Predict<-predict(standardGLM, newdata=experimentPlate)
Predict
#ADD PREDICTIONS TO EXPERIMENT DATA FRAME
experimentPlate$predictedConc<-Predict

#PLOT CURVE
#standard
plot(standardPlate$concentrations~standardPlate$fluorescence, col="red", 
ylab="concentration ug/mL", xlab="fluorescence", ylim=c(0,2))
#experiment
points(experimentPlate$predictedConc~experimentPlate$fluorescence, col="blue", pch=5)


#MAKE PLATE MAP WITH CONCENTRATIONS
#MULTIPLY BY 200 TO ADJUST FOR DILUTION 
predict_corrected<-Predict*200
#add predictions to experiment dataframe
experimentPlate$predictedConc<-predict_corrected
ConcMatrix<-matrix(experimentPlate$predictedConc, nrow=8, ncol=12)
colnames(ConcMatrix)<-c(1:12)
rownames(ConcMatrix)<-c("a","b","c","d","e","f","g","h")
write.xlsx(ConcMatrix, file="KPC_LTACH_107-202.xls")

#LOOK AT CONCENTRATION RANGES
sortedExp<-experimentPlate[order(experimentPlate$predictedConc),]
head(sortedExp)
tail(sortedExp)
median(sortedExp$predictedConc)
