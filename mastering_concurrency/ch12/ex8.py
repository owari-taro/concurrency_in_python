import threading
import time


class Spouse(threading.Thread):

    def __init__(self, name, partner):
        threading.Thread.__init__(self)
        self.name = name
        self.partner = partner
        self.hungry = True

    def run(self):
        while self.hungry:
            print('%s is hungry and wants to eat.' % self.name)

            if self.partner.hungry:
                print('%s is waiting for their partner to eat first...' %
                      self.name)
                time.sleep(1)
                print(f"\n{self.hungry}\n")

            else:
                with fork:
                    print('%s has stared eating.' % self.name)
                    time.sleep(5)
                    print('%s is now full.' % self.name)
                    self.hungry = False
                    print(f"\n{self.hungry}\n")


if __name__ == "__main__":

    fork = threading.Lock()

    partner1 = Spouse('Wife', None)
    partner2 = Spouse('Husband', partner1)
    partner1.partner = partner2

    partner1.start()
    partner2.start()
