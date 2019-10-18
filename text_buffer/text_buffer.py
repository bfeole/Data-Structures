from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class TextBuffer:
    def __init__(self, init=None):
        self.storage = DoublyLinkedList()

        if init:
            for char in init:
                self.storage.add_to_tail(char)

    def __str__(self):
        # Print the contents of the buffer
        # Iterate through start at the head and do awhile loop
        s = ""
        current = self.storage.head
        while current:
            s += current.value
            # next item in linked list nodes
            current = current.next
        return s

    def append(self, string_to_add):
        for char in string_to_add:
            self.storage.add_to_tail(char)

    def prepend(self, string_to_add):
        # [::-1] easy backwards for each python
        for char in string_to_add[::-1]:
            self.storage.add_to_head(char)

    def delete_front(self, chars_to_remove):
        for _ in range(chars_to_remove):
            self.storage.remove_from_head()

    def delete_back(self, chars_to_remove):
        for _ in range(chars_to_remove):
            self.storage.remove_from_tail()

    def join(self, other_buffer):
        # TODO:
        # What do we do if something other than a
        # TextBuffer is passed in?

        self.storage.tail.next = other_buffer.storage.head
        other_buffer.storage.head.prev = self.storage.tail
        other_buffer.storage.head = self.storage.head
        self.storage.tail = other_buffer.storage.tail

    def split(self, split_location):
        # Split at the nth character
        # make a counter
        # make string
        # iterate through LL
        # add N chars to string
        # put string into new buffer (init)
        # return new buffer
        pass

    def join_string(self, string_to_join):
        # new_buffer = TextBuffer(string_to_join)
        # self.join(new_buffer)

        self.append(string_to_join)


if __name__ == '__main__':
    text = TextBuffer("Super")

    print(text)

    text.join_string("califragilisticexpeadlidocious")

    print(text)

    text.append(" is ")
    text.join(TextBuffer("weird."))

    print(text)

    text.delete_back(6)

    print(text)

    text.prepend("Hey! ")
    print(text)

    text.delete_front(4)
    print(text)
