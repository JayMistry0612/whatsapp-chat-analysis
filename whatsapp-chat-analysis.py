
#In[]:
import pandas as pd
import re
import matplotlib.pyplot as plot
import emoji

def no_ofmsg_perperson():
    author_value_counts = df['Author'].value_counts() # Number of messages per author
    top_10_author_value_counts = author_value_counts.head(10) # Number of messages per author for the top 10 most active authors
    print("\nNo of Messages per user:\n" ,author_value_counts)
    top_10_author_value_counts.plot.barh()
    plot.xlabel("No. of Messages")
    plot.ylabel("User")
    plot.title("Top 10 Messages per User")
    

def no_ofemoji_ingroup():
    #Find Top 10 emojis used in Group
    y = df['Author'].unique()
    emo=[]
    for name in y:
        x=df.loc[df['Author'] == name,'Message']
        for z in x:
            my_str1 = str(z)
            for each in my_str1:
                if each in emoji.EMOJI_DATA:
                    emo.append([name,each])

    em_df1 = pd.DataFrame(emo,columns=['Name','Emoji'])
    print("\nTotal number of Emoji sent by Users:\n",em_df1['Name'].value_counts())
    print("\nTop 10 Emojis used in group:\n",em_df1['Emoji'].value_counts().head(10))
    
    
    
def media_perperson():
    #To find  Media sent by a user
    media = df[df['Message'] == " <Media omitted>"]
    author_media_messages_value_counts = media['Author'].value_counts()
    top_10_author_media_messages_value_counts = author_media_messages_value_counts.head(10)
    #top_10_author_media_messages_value_counts.plot.barh()
    #plot.ylabel('Author')
    #plot.xlabel('Media items sent')
    #plot.title('Top 10 Media Items sent per Author')
    print("\nNumber of Media file sent by users:\n",author_media_messages_value_counts)
    
    
def emoji_perperson():
    # Find Top 5 emoji used by per person
    y = df['Author'].unique()

    for name in y:
        x=df.loc[df['Author'] == name,'Message']
        emo=[]
        for z in x:
            my_str1 = str(z)
            for each in my_str1:
                if each in emoji.EMOJI_DATA:
                    emo.append(each)
        if len(emo) != 0: 
            em_df1 = pd.DataFrame(emo,columns=['Emoji Per Person'])
            print("\nTop 5 Emojis used by",name ,": \n" ,em_df1['Emoji Per Person'].value_counts().head(5))
        else:
            print("\n {} has not used emoji in this group".format(name))

            
      
file = open('Add your text files here','r', encoding="utf-8")
read = file.readlines()
data=[]
for x in read:
    x=x.strip()
    match = re.match(r'(\d+/\d+/\d+)',x) # MAtches the date format
    if match:
        splitLine = x.split(' - ') # splitLine = ['18/06/17, 22:47', 'Loki: Why do you have 2 numbers, Banner?']
        dateTime = splitLine[0] # dateTime = '18/06/17, 22:47'
        k= dateTime.split(', ') # date = '18/06/17'; time = '22:47'
        date=k[0]
        message = ' '.join(splitLine[1:]) 
        chck = re.findall(':',message) #checks if some1 left the group
        if chck:
            author,comments = message.split(":",1) #split at 1st ':'
            data.append([date, author, comments])
    else:
        if x!="":
            data.append([ date ,author ,x])

df=pd.DataFrame(data,columns=['Date', 'Author', 'Message'])

print("\nThe group was most active on {}\n".format(df['Date'].value_counts().head(1)))
mess_del = df[df['Message'] == ' This message was deleted']  #Cleaning the data frame by elemenating the messages deleted by user
df = df.drop(mess_del.index)

no_ofemoji_ingroup()
media_perperson()
emoji_perperson()
no_ofmsg_perperson()





# %%
