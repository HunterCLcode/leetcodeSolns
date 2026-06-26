class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Dict: card -> freq
        card_map, start_cards = defaultdict(int), defaultdict(int)
        for card in hand: card_map[card] += 1

        # Dict: start_card -> freq
        for card, count in card_map.items():
            prev_freq = card_map[card - 1] if card - 1 in card_map else 0
            if count > prev_freq:
                start_cards[card] += count - prev_freq

        while start_cards:
            # Pop card from starting cards
            cur_card = list(start_cards.keys())[-1]
            start_cards[cur_card] -= 1
            if start_cards[cur_card] == 0:
                start_cards.pop(cur_card)

            # Add cards until size reached or no more cards
            size = 0
            while size < groupSize and cur_card in card_map:
                card_map[cur_card] -= 1
                if card_map[cur_card] == 0:
                    card_map.pop(cur_card)
                size += 1
                cur_card += 1
            
            if size < groupSize: return False
            
            # If current card > prev card, add a card to starting cards
            if (cur_card in card_map
                and (cur_card - 1 in card_map 
                    and card_map[cur_card] > card_map[cur_card - 1] 
                    or not cur_card - 1 in card_map)
                ):
                start_cards[cur_card] += 1
        return not bool(card_map)
