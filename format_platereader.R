#Script to parse plate reader data
#Shawn Whitefield April 2015

#first save Excel doc as .csv
#read in csv file
	Plate_reader_data<-read.table("26032015-001.csv", sep=",")

#delete empty column 14 and every 9th row
	Plate_reader_data<-Plate_reader_data[-c(seq(from=1, to =433, by = 9)),-c(14,15)]

#add time point variable
#you can change this depending on how many plates you have or how far apart your readings are
	time<-seq(from=0, to = 24, by = .5)
	
# function to add the time values to the time column for each 96 well plate reading in the file
# you can change the number of rows on each plate, defaults to 8
reptime<-function(time,rows=8){
  timevec<-vector()
  for(i in 1:length(time)){
      timeadd<-(rep(time[i],rows))
      timevec<-append(timevec,timeadd)  
    }
    timevec<<-timevec
  }
#run the function to return timevec and make this a column in your dataframe
	Plate_reader_data$timePoint<-reptime(time)

#label columns and rows
#Change the names to your bile acid names if you want:
	colnames(Plate_reader_data)<-c("row_letter","one","two","three",
									"four","five","six","seven","eight",
									"nine","ten","eleven","twelve","time_point")
	rownames(Plate_reader_data)<-NULL

#Your dataframe should be ready to go! 

####SUBSETTING DATA EXAMPLES

#Only want the first plate(time 0)
plate1<-subset(Plate_reader_data,Plate_reader_data$time_point==0)

#Only want row G from every plate
rowG<-subset(Plate_reader_data,Plate_reader_data$row_letter=="G")

#Want the first 3 columns from every plate
first3Col<-Plate_reader_data[,1:3]

#Want row G from first plate
rowG_Plate1<-subset(Plate_reader_data,Plate_reader_data$row_letter=="G" & Plate_reader_data$time_point==0)

#Want the average of timepoint 0, row G, columns 1:3
#this would be like for replicates
mean(as.numeric(rowG_Plate1[,2:4]))




