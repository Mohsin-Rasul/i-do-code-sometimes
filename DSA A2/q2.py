class CardNode:
    # Node for the Doubly Linked List.
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.next = None
        self.prev = None

    def __str__(self):
        # Helper to print card nicely
        return f"{self.rank} of {self.suit}"

class CardHand:
    # This is the Doubly Linked List for managing the card hand.
    
    # We fix the suit order for grouping
    suitorder = ["Hearts", "Clubs", "Diamonds", "Spades"]

    def __init__(self):
        self.head = None
        self.tail = None
        # The four "fingers". They point to the LAST card of each suit
        self.suitfingers = {
            "Hearts": None,
            "Clubs": None,
            "Diamonds": None,
            "Spades": None
        }

    def _insertafter(self, existingnode, newcard):
        """
        Internal helper function to insert a new card
        after an existing node.
        """
        newcard.prev = existingnode
        if existingnode is None:
            # This means we are inserting at the head
            if self.head:
                newcard.next = self.head
                self.head.prev = newcard
            self.head = newcard
        else:
            # Inserting in the middle or end
            newcard.next = existingnode.next
            if existingnode.next:
                existingnode.next.prev = newcard
            existingnode.next = newcard
        
        # Check if it's the new tail
        if newcard.next is None:
            self.tail = newcard

    def _removenode(self, node):
        """
        Internal helper function to remove any node
        from the list.
        """
        if node.prev:
            node.prev.next = node.next
        else:
            # It was the head
            self.head = node.next
        
        if node.next:
            node.next.prev = node.prev
        else:
            # It was the tail
            self.tail = node.prev
        
        # Clear pointers
        node.next = None
        node.prev = None

    def addcard(self, r, s):
        """
        Adds a new card of rank r and suit s.
        It finds the correct finger and inserts after it
        to keep suits together.
        """
        newcard = CardNode(s, r)
        finger = self.suitfingers[s]

        if finger:
            # We already have cards of this suit. Add after the last one.
            self._insertafter(finger, newcard)
        else:
            # First card of this suit. Find where it goes.
            # We check for the finger of the suit *before* it.
            insertpoint = None
            prevsuitindex = self.suitorder.index(s) - 1
            while prevsuitindex >= 0:
                prevsuitname = self.suitorder[prevsuitindex]
                if self.suitfingers[prevsuitname]:
                    insertpoint = self.suitfingers[prevsuitname]
                    break
                prevsuitindex -= 1
            
            # insertpoint is now the last card of the previous suit group
            self._insertafter(insertpoint, newcard)
        
        # The new card is now the new finger for its suit
        self.suitfingers[s] = newcard

    def play(self, s):
        """
        Removes and returns a card of suit s.
        We remove the card at the 'finger' (last card of that suit).
        If no card of suit s, removes an arbitrary card (the tail).
        """
        finger = self.suitfingers[s]
        
        if finger:
            # We have a card of this suit. Play the one at the finger.
            cardtoplay = finger
            prevnode = finger.prev
            self._removenode(finger)
            
            # Update the finger.
            if prevnode and prevnode.suit == s:
                # The previous node is of the same suit, so it's the new finger
                self.suitfingers[s] = prevnode
            else:
                # We just removed the only/last card of this suit
                self.suitfingers[s] = None
            
            return f"Played: {cardtoplay}"
        else:
            # No card of suit s. Play an arbitrary card (the tail).
            if self.tail:
                arbitrarycard = self.tail
                # We must also update the finger of *whatever* suit this card was
                cardfinger = self.suitfingers[arbitrarycard.suit]
                if cardfinger == arbitrarycard: # if the tail was a finger
                    prevnode = arbitrarycard.prev
                    if prevnode and prevnode.suit == arbitrarycard.suit:
                        self.suitfingers[arbitrarycard.suit] = prevnode
                    else:
                        self.suitfingers[arbitrarycard.suit] = None

                self._removenode(arbitrarycard)
                return f"Played (arbitrary): {arbitrarycard}"
        
        return "No cards in hand to play."

    def __iter__(self):
        """
        Iterates through all cards from head to tail.
        """
        temp = self.head
        while temp:
            yield temp
            temp = temp.next

    def allofsuit(self, s):
        """
        Iterates through all cards of a specific suit.
        """
        for card in self: # Uses the __iter__ method
            if card.suit == s:
                yield card

# --- Main Program Execution ---
hand = CardHand()
hand.addcard("5", "Hearts")
hand.addcard("10", "Diamonds")
hand.addcard("3", "Clubs")
hand.addcard("King", "Hearts")
hand.addcard("7", "Diamonds")
hand.addcard("Ace", "Spades")
hand.addcard("4", "Clubs")

print("--- Full Hand (Suits are grouped) ---")
for card in hand:
    print(card)

print("\n--- All Diamonds ---")
for card in hand.allofsuit("Diamonds"):
    print(card)

print("\n--- Playing Cards ---")
print(hand.play("Hearts"))   # Plays King of Hearts (last Heart)
print(hand.play("Spades"))   # Plays Ace of Spades
print(hand.play("Spades"))   # No Spades left, plays arbitrary (tail)

print("\n--- Hand After Playing ---")
for card in hand:
    print(card)
