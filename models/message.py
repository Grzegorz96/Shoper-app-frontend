class Message:
    """Message class used to create message objects and display them in the message window and messages page."""
    def __init__(self, conversation_id, message_id, customer_flag, content, post_date, user_id, first_name):
        """ Constructor for the Message class."""
        self.conversation_id = conversation_id
        self.message_id = message_id
        self.customer_flag = customer_flag
        self.content = content
        self.post_date = post_date
        self.user_id = user_id
        self.first_name = first_name
