import pandas as pd
import os
from matplotlib import pyplot as plt
import time

class InvalidInput(Exception):
    def error():
        print("Invalid input")
        print("Restarting")
        time.sleep(1)
        main()

class InvalidPath(Exception):
    def error():
        print("File does not exist")
        print("Restarting")
        time.sleep(1)
        main()
    
class InvalidFile(Exception):
    def error():
        print("File must be a .csv file")
        print("Restarting")
        time.sleep(1)
        main()

def selectData(headerRequested, filename):
    dataframe = pd.read_csv(filename)

    if int(headerRequested)>11:
        raise InvalidInput
        
    
    headers={"1":'Date',"2": 'Tweets published',"3": 'impressions',"4": 'engagements',
       "5":'engagement rate',"6": 'retweets',"7": 'replies',"8": 'likes',
       "9":'user profile clicks',"10": 'url clicks',"11": 'hashtag clicks'}

    os.system("cls")
    print(f"{headers[headerRequested]}")
    print(dataframe[headers[headerRequested]])


def tweetBasicData(filename):
    dataframe = pd.read_csv(filename)

    try:
        dates = [i.split("/")[1] for i in dataframe["Date"]]
    except IndexError as e:
        print("You have to open the csv file and make the width of column 1 wider")
        time.sleep(2)
        return

    labels = ["Tweets published","Impressions","Engagements"]
    #ticks = [i*50 for i in range(10)]
    fig = plt.figure(1)	#identifies the figure 
    plt.title("Tweet analytics-Tweets", fontsize='16')	#title
    plt.plot(dates,dataframe["Tweets published"])
    plt.plot(dates, dataframe["impressions"])	#plot the points
    plt.plot(dates, dataframe["engagements"])

    plt.xlabel("Dates",fontsize='13')	#adds a label in the x axis

    #plt.yticks(ticks)
    plt.ylabel("Tweet Data",fontsize='13')	#adds a label in the y axis
    plt.legend(labels,loc='best')	#creates a legend to identify the plot
    plt.savefig('Tweet_analytics_Tweets.png')	#saves the figure in the present directory
    plt.grid()	#shows a grid under the plot
    plt.show()


def tweetTweetData(filename):
    dataframe = pd.read_csv(filename)
    try:
        dates = [i.split("/")[1] for i in dataframe["Date"]]
    except IndexError as e:
        print("You have to open the csv file and make the width of column 1 wider")
        time.sleep(2)
        return
    labels = ["Tweets published","Retweets","Replies","Likes"]
    
    fig = plt.figure(1)	#identifies the figure 
    plt.title("Tweet analytics-Tweet info", fontsize='16')	#title
    plt.plot(dates,dataframe["Tweets published"])
    plt.plot(dates, dataframe["retweets"])	#plot the points
    plt.plot(dates, dataframe["replies"])
    plt.plot(dates, dataframe["likes"])
    plt.xlabel("Dates",fontsize='13')	#adds a label in the x axis
    plt.ylabel("Tweet Data",fontsize='13')	#adds a label in the y axis

    plt.legend(labels,loc='best')	#creates a legend to identify the plot
    plt.savefig('Tweet_analytics_Tweet_info.png')	#saves the figure in the present directory
    plt.grid()	#shows a grid under the plot
    plt.show()


def tweetTweetOtherData(filename):
    dataframe = pd.read_csv(filename)

    try:
        dates = [i.split("/")[1] for i in dataframe["Date"]]
    except IndexError as e:
        print("You have to open the csv file and make the width of column 1 wider")
        time.sleep(2)
        return

    labels = ["Tweets published","Profile clicks","URL clicks"]
    
    fig = plt.figure(1)	#identifies the figure 
    plt.title("Tweet analytics-Other", fontsize='16')	#title
    plt.plot(dates,dataframe["Tweets published"])
    plt.plot(dates, dataframe["user profile clicks"])	#plot the points
    plt.plot(dates, dataframe["url clicks"])
    plt.xlabel("Dates",fontsize='13')	#adds a label in the x axis
    plt.ylabel("Tweet Data",fontsize='13')	#adds a label in the y axis

    plt.legend(labels,loc='best')	#creates a legend to identify the plot
    plt.savefig('Tweet_analytics_Other.png')	#saves the figure in the present directory
    plt.grid()	#shows a grid under the plot
    plt.show()

def checkFileValid(fileName):
    if os.path.isfile(fileName):
        print("File exists")
    else:
        raise InvalidPath

    if fileName[-3:]=="csv":
        print("File is .csv")
    else:
        raise InvalidFile
    
def main():
    os.system("cls")
    file = input("Enter path of file:")
    try:
        checkFileValid(file)
    except InvalidPath:
        InvalidPath.error()
    except InvalidFile:
        InvalidFile.error()
    
    os.system("cls")
    print("Valid file")
    start= input("What data do you want to look at?\n1:Graph\n2:raw\n")
    if start=="1":
        graph = input("Which graph do you want to look at?\n1:impressions and engagement\n2:retweets/replies/likes\n3:profile clicks/url clicks\n")
        if graph=="1":
            tweetBasicData(file)
        elif graph=="2":
            tweetTweetData(file)
        elif graph=="3":
            tweetTweetOtherData(file)
        else:
            InvalidInput.error()

    elif start=="2":
        header = input(
        "What header do you want?\n1:Date\n2:Tweets published\n3:impressions\n4:engagements\n5:engagement rate\n6:retweets\n7:replies\n8:likes\n9:user profile clicks\n10:url clicks\n11:hashtag clicks\n"
        )
        try:
            selectData(header, file)
        except InvalidInput:
            InvalidInput.error()
    else:
       InvalidInput.error()


if __name__=="__main__":
    main()