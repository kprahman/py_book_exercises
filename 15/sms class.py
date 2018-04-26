class SMS_store:


    def __init__(self):
        self.list_of_messages = []

    def __str__(self):
        if len(self.list_of_messages) == 0:
            return "Nothing here!"
        return "{}".format(self.list_of_messages)


    def add_new_arrival(self):
        import time
        has_read = False
        from_number = str(input("What number are you sending this message from?"))
        text_of_sms = str(input("What message would you like to send?"))
        time_arrived = time.asctime()
        message = has_read,from_number,time_arrived,text_of_sms
        self.list_of_messages.append(message)

    def count_messages(self):
        return len(self.list_of_messages)

    def get_unread_indexes(self):
        unread_indexes = []
        for i in range(0,len(self.list_of_messages)):
            if not self.list_of_messages[i][0]:
                unread_indexes.append(i)
        return "Unread messages:{}".format(unread_indexes)

    def get_message(self,i):
        self.list_of_messages[i] = ("read",) + self.list_of_messages[i][1:4]
        return self.list_of_messages[i][1:4]


my_inbox =  SMS_store()
my_inbox.add_new_arrival()
my_inbox.add_new_arrival()
print(my_inbox.get_unread_indexes())
print(my_inbox.get_message(1))
print(my_inbox.get_unread_indexes())