class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


emails = []
console_input = input()

while console_input != "Stop":
    sender, receiver, content = console_input.split()

    email = Email(sender, receiver, content)
    emails.append(email)
    console_input = input()

indexces_sent_emails = [int(x) for x in input().split(", ")]

for x in indexces_sent_emails:
    emails[x].send()
for email in emails:
    print(email.get_info())
