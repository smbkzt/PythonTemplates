class Publisher:
    users = set()

    def register(self, user):
        self.users.add(user)

    def unregister(self, user):
        self.users.discard(user)

    def send_notification(self, message):
        for user in self.users:
            user.notify(message)


class Subscriber:

    def __init__(self, username):
        self.username = username

    def notify(self, message):
        print(self.username + ' received message: ' + message)

publisher = Publisher()

bucky = Subscriber('Bucky')
sally = Subscriber("Sally")
publisher.register(bucky)
publisher.register(sally)

publisher.send_notification('Some random message to users')
