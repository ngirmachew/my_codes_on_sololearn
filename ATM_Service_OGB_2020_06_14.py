def atm_queue_service():
    # Start the loop:
    while True:
        # go grab a response from the for loop 'name' variable and save it in 'resp':
        resp = (yield)
        if resp.strip().lower() in ('quit', 'q', 'end'):
            if not customers:
                print("Bye then!")
                return
            else:
                print(f"{len(customers)} people are queuing for service.\n")
                break
        #elif customers.get(resp.strip().lower(),None):
        elif resp.strip().lower() in customers.keys():
            print(f"'{resp}' is already in the queue. Try again.")
            yield
        else:
            customers[resp.strip().lower()] = len(customers)
            yield
    quest = input('Who are you looking for?: ')
    #if customers.get(quest.strip().lower(),None):
    if quest.strip().lower() in customers.keys():
        print(f"'{quest}' needs to wait for {customers[quest.strip().lower()]} more person(s) until s/he gets service")
        return
    else:
        print(f"'{quest}' is not in the queue.")
if __name__ == "__main__":
    welcome = """
†††*****************************†††
†† Welcome to ATM Queue Service. ††
†† Type 'q', 'end', or 'quit' to ††
†† end the service.              ††
†††*****************************†††
"""
    print(welcome)
    customers = dict()
    feed = atm_queue_service()
    for name in feed:
        name = input("Please input the name: ")
        try:
            feed.send(name)
        except StopIteration:
            break