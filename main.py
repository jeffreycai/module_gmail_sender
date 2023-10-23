from gmail_sender import GmailSender

def main():
    sender = GmailSender()
    sender.send('Test subject', 'Test message')

if __name__ == '__main__':
    main()
