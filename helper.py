
def fetch_data(selected_user,df):
    if selected_user != "Overall":
        df = df[df["user"] == selected_user]
    # fetch num of messages
    num_messages =df.shape[0]

    #fetch num of words
    words=[]
    for message in df['message']:
        words.extend(message.split())

    #fetch num of media messages
    num_media_messages= df[df['message']== '<Media omitted>\n'].shape[0]

    return num_messages, len(words), num_media_messages


    #     # fetch no. of messages
    #     num_messages = df.shape[0]
    #
    #     # number of words
    #     words = []
    #     for message in df['message']:
    #         words.extend(message.split())
    #
    #     return num_messages,len(words)
    #
    # else:
    #
    #     new_df= df[df["user"]==  selected_user ]
    #     num_messages = new_df.shape[0]                 ## shape[0] mean no. of row in the selected user dataframe
    #     words = []
    #     for message in new_df['message']:
    #         words.extend(message.split())
    #
    #     return num_messages,len(words)