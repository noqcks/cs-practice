class Node(object):
  """ A node in a singly linked list """
  def __init__(self, val, next=None):
    self._val = val
    self._next = next

  """ val returns the data value for the node """
  @property
  def val(self) -> int:
    return self._val

  """ val setter will set the data value for a node """
  @val.setter
  def val(self, num: int) -> int:
    self._val = num
    return self._val

  """ next property will return the next node in the linked list """
  @property
  def next(self):
    return self._next

  """ next setter will set the next node in the linked list """
  @next.setter
  def next(self, next):
    self._next = next
    return self._next

class SinglyLinkedList:
  """ This class implements a basic singly linked list"""
  def __init__(self):
    self.head = None
    self.length = 0

  """ ___len___ returns the length of the list """
  def __len__(self):
    return self.length

  """ prepend will add a node to the beginning of the linked list """
  def prepend(self, data):
    new_head = Node(data)
    new_head.next = self.head
    self.head = new_head
    self.length += 1

  """ append will add a node to the end of the linked list """
  def append(self, data):
    new_node = Node(data)

    if self.head == None:
      self.head = new_node
      self.length += 1
    else:
      iter_node = self.head

      # find last node
      while iter_node.next:
        iter_node = iter_node.next

      # update last node reference
      iter_node.next = new_node
      self.length += 1

  """ remove will remove a node from the linked list """
  def remove(self, data):
    prev = None

    for node in self:
      if node.val == data:
        if prev:
          # bridge old and new node
          prev.next = node.next
        else:
          # we are at beginning, next is new head
          self.head = node.next

        self.length -= 1
        return True

      prev = node

    return False

  """
  __iter___ overrides the python default function so that we can easily
  iterate over the linked list
  """
  def __iter__(self):
    iter_node = self.head
    while iter_node:
      yield iter_node
      iter_node = iter_node.next

  """
  __list__ will return a python list of all node values
  """
  def __list__(self):
    arr = []
    for node in self:
      arr.append(node.val)
    return arr

  """
  __str__ will create a string representation of the linked list
  """
  def __str__(self):
    node = self.head
    s = ''
    for node in self:
      s += str(node.val) + ' => '
      node = node.next
    return s + 'None'

  """
  __repr__ will return a string representation of the linked list
  """
  def __repr__(self):
    return self.__str__()


