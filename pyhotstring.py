from pynput.keyboard import Key, Listener, Controller
h_str = {
    "'b'':'':'": "ß",
    "'o'':'':'": "ö",
    "'u'':'':'": "ü",
    "'a'':'':'": "ä"
}


class hotstring():

    def __init__(self):
        self.store = ["f", "i", "l"]
        # Collect events until released
        self.kb = Controller()
        with Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()

    def on_press(self, key):
        self.one_iter(key)
        self.is_match()
       # print('{0} pressed'.format(key))

    def on_release(self, key):
        #print('{0} release'.format(key))

        # Stop listener
        if key == Key.esc:
            return False

    def one_iter(self, key):
        if key != Key.shift_r:
            self.store.pop(0)
            self.store.append("{}".format(key))

    def is_match(self):
        m = h_str.get("".join(self.store))
        if m:
            print(f"match!: {self.store}")
            self.kb.press(Key.backspace)
            self.kb.release(Key.backspace)
            self.kb.press(Key.backspace)
            self.kb.release(Key.backspace)
            self.kb.press(Key.backspace)
            self.kb.release(Key.backspace)
            self.kb.press(m)
            self.kb.release(m)


x = hotstring()
