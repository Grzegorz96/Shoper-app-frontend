class Conversation:
    """Conversation class used to create conversation objects and display them in messages page."""
    def __init__(self, conversation_id, announcement_id, title, first_name):
        """Constructor for the Conversation class."""
        self.conversation_id = conversation_id
        self.announcement_id = announcement_id
        self.title = title
        self.first_name = first_name
