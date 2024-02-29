"""
File: HouNodesLinkedList.py
Author: CVoellmann
Date: 2/16/2024
Description: Assignment 1 for Rebelway Python for Production.
    A Houdini node network manager with the mindset of linked lists.
    Prints the list of all linked nodes from head to tail.
    Has a class method for inserting a node.
"""


#------------------------------------------------------------
import hou

#------------------------------------------------------------




class HouNodesLinkedList:
    """"""

    #------------------------------------------------------------
    def __init__(self, headNode=None):
        """Can either pass in a node as the head node, or will
        determine a defualt head node form a slection of nodes.
        """
        
        if headNode == None:
            self.selNodeList = hou.selectedNodes()
            self.headNode = self.selNodeList[0]
        else:
            self.headNode = headNode
            
    #------------------------------------------------------------
    def getHeadNode(self):
        """returns the Head node"""
        
        return self.headNode
    
    #------------------------------------------------------------
    def getTailNode(self):
        """"""
        tail = None
        node = self.headNode
        
        while node is not None:
            tail = node
            node = self.getNextNode(node)
        
        return tail
            
    #------------------------------------------------------------
    def getNextNode(self, node):
        """"""
        nextNode = None
        
        if len(node.outputs()):
            nextNode = node.outputs()[0]
            
        return nextNode
            
    #------------------------------------------------------------
    def printNetworkList(self):
        """From the head node, prints the connected nodes to the tail node."""
        
        node = self.headNode
        
        while node is not None:
            print(node)
            node = self.getNextNode(node)
                
            
    #------------------------------------------------------------
    def insertNode(self, insertNode):
        """"""
        node = self.headNode
        prevNode = None
        nextNode = None
        
        while node is not None:
            node = self.getNextNode(node)
            if node.name() == insertNode:
                prevNode = node
                nextNode = self.getNextNode(prevNode)
                insertNode = prevNode.createOutputNode('null', "Inserted_Null")
                nextNode.setInput(0, insertNode)
                return insertNode
                
                

#Testing the above Class and methods

houNet = HouNodesLinkedList()
print("------------------------------------------------------------")
print("The network node list:")
houNet.printNetworkList()
print("------------------------------------------------------------")
print(f"Head node: {houNet.headNode}")
print(f"Tail node: {houNet.getTailNode()}")
print("------------------------------------------------------------")
insertedNode = houNet.insertNode("node2")
print(f"Inserted node: {insertedNode}")
print("------------------------------------------------------------")
houNet.printNetworkList()
print("------------------------------------------------------------")

        
        
        
        
        
        
        
        
        
            
        
        
        
    
    