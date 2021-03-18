# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 18:57:27 2020

@author: ayush
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head= new_node

    def insertAfter(self,prev_node,new_data):
        if prev_node is None:
            print("The give previous node must in LinkedList.")
            return
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node

    def append(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last=self.head
        while (last.next):
            last=last.next
        last.next=new_node

    def deleteNode(self,key):
        temp=self.head
        if(temp is not None):
            if(temp.data==key):
                self.head=temp.next
                temp=None
                return
        while(temp is not None):
            if temp.data==key:
                break
            prev=temp
            temp=temp.next
        if (temp==None):
            return
        prev.next=temp.next
        temp=None

    def printList(self):
        temp=self.head
        while(temp):
            print("%d" %(temp.data))
            temp=temp.next

    def deleteNode(self, position):
        if self.head == None: 
            return
        temp = self.head
        if position == 0: 
            self.head = temp.next
            temp = None
            return
        for i in range(position -1):
            temp = temp.next
            if temp is None: 
                break
        if temp is None: 
            return 
        if temp.next is None: 
            return
        next = temp.next.next
        temp.next = None
        temp.next = next

    def deleteList(self):
        current = self.head 
        while current: 
            prev = current.next
            del current.data
            current = prev

    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 

if __name__=='__main__':
    # Start with the empty list 
    llist = LinkedList() 
  
    # Insert 6.  So linked list becomes 6->None 
    llist.append(6) 
  
    # Insert 7 at the beginning. So linked list becomes 7->6->None 
    llist.push(7)
  
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None 
    llist.push(1)
  
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None 
    llist.append(4) 
  
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None 
    llist.insertAfter(llist.head.next, 8) 
  
    print('Created linked list is:') 
    llist.printList() 
    llist.deleteNode(1)  
    print ("\nLinked List after Deletion of 1:") 
    llist.printList()
    print("Deleting linked list") 
    llist.deleteList()      
    print("Linked list deleted")