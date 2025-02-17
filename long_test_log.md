### State at the beginning
- Top card in discard pile: GREEN THREE
- Player Alice has 7 cards: [(RED ZERO),(RED REVERSE),(GREEN FOUR),(GREEN SEVEN),(GREEN NINE),(YELLOW FIVE),(YELLOW SEVEN)]
- Player Bob has 7 cards: [(RED FOUR),(RED SEVEN),(RED NINE),(BLUE ONE),(BLUE SEVEN),(YELLOW FIVE),(YELLOW REVERSE)]
- Player Charlie has 7 cards: [(RED FIVE),(BLUE FIVE),(BLUE SKIP),(GREEN ONE),(GREEN TWO),(YELLOW ZERO),(YELLOW SKIP)]
### Round 1
- **Current Player**: Alice
- **Current color: GREEN Current label: THREE**
- **Action**: Alice plays GREEN FOUR
- **State after the round**
	- Player Bob has 7 cards: [(RED FOUR),(RED SEVEN),(RED NINE),(BLUE ONE),(BLUE SEVEN),(YELLOW FIVE),(YELLOW REVERSE)]
	- Player Charlie has 7 cards: [(RED FIVE),(BLUE FIVE),(BLUE SKIP),(GREEN ONE),(GREEN TWO),(YELLOW ZERO),(YELLOW SKIP)]
	- Player Alice has 6 cards: [(RED ZERO),(RED REVERSE),(GREEN SEVEN),(GREEN NINE),(YELLOW FIVE),(YELLOW SEVEN)]

### Round 2
- **Current Player**: Bob
- **Current color: GREEN Current label: FOUR**
- **Action**: Bob plays RED FOUR
- **State after the round**
	- Player Charlie has 7 cards: [(RED FIVE),(BLUE FIVE),(BLUE SKIP),(GREEN ONE),(GREEN TWO),(YELLOW ZERO),(YELLOW SKIP)]
	- Player Alice has 6 cards: [(RED ZERO),(RED REVERSE),(GREEN SEVEN),(GREEN NINE),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Bob has 6 cards: [(RED SEVEN),(RED NINE),(BLUE ONE),(BLUE SEVEN),(YELLOW FIVE),(YELLOW REVERSE)]

### Round 3
- **Current Player**: Charlie
- **Current color: RED Current label: FOUR**
- **Action**: Charlie plays RED FIVE
- **State after the round**
	- Player Alice has 6 cards: [(RED ZERO),(RED REVERSE),(GREEN SEVEN),(GREEN NINE),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Bob has 6 cards: [(RED SEVEN),(RED NINE),(BLUE ONE),(BLUE SEVEN),(YELLOW FIVE),(YELLOW REVERSE)]
	- Player Charlie has 6 cards: [(BLUE FIVE),(BLUE SKIP),(GREEN ONE),(GREEN TWO),(YELLOW ZERO),(YELLOW SKIP)]

### Round 4
- **Current Player**: Alice
- **Current color: RED Current label: FIVE**
- **Action**: Alice plays RED ZERO
- **State after the round**
	- Player Bob has 6 cards: [(RED SEVEN),(RED NINE),(BLUE ONE),(BLUE SEVEN),(YELLOW FIVE),(YELLOW REVERSE)]
	- Player Charlie has 6 cards: [(BLUE FIVE),(BLUE SKIP),(GREEN ONE),(GREEN TWO),(YELLOW ZERO),(YELLOW SKIP)]
	- Player Alice has 5 cards: [(RED REVERSE),(GREEN SEVEN),(GREEN NINE),(YELLOW FIVE),(YELLOW SEVEN)]

### Round 5
- **Current Player**: Bob
- **Current color: RED Current label: ZERO**
- **Action**: Bob plays RED SEVEN
- **State after the round**
	- Player Charlie has 6 cards: [(BLUE FIVE),(BLUE SKIP),(GREEN ONE),(GREEN TWO),(YELLOW ZERO),(YELLOW SKIP)]
	- Player Alice has 5 cards: [(RED REVERSE),(GREEN SEVEN),(GREEN NINE),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Bob has 5 cards: [(RED NINE),(BLUE ONE),(BLUE SEVEN),(YELLOW FIVE),(YELLOW REVERSE)]

### Round 6
- **Current Player**: Charlie
- **Current color: RED Current label: SEVEN**
- **Action**: Charlie draws a card into their hand.
- **State after the round**
	- Player Alice has 5 cards: [(RED REVERSE),(GREEN SEVEN),(GREEN NINE),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Bob has 5 cards: [(RED NINE),(BLUE ONE),(BLUE SEVEN),(YELLOW FIVE),(YELLOW REVERSE)]
	- Player Charlie has 7 cards: [(BLUE FIVE),(BLUE SKIP),(GREEN ONE),(GREEN TWO),(GREEN FIVE),(YELLOW ZERO),(YELLOW SKIP)]

### Round 7
- **Current Player**: Alice
- **Current color: RED Current label: SEVEN**
- **Action**: Alice plays RED REVERSE
- **State after the round**
	- Player Charlie has 7 cards: [(BLUE FIVE),(BLUE SKIP),(GREEN ONE),(GREEN TWO),(GREEN FIVE),(YELLOW ZERO),(YELLOW SKIP)]
	- Player Bob has 5 cards: [(RED NINE),(BLUE ONE),(BLUE SEVEN),(YELLOW FIVE),(YELLOW REVERSE)]
	- Player Alice has 4 cards: [(GREEN SEVEN),(GREEN NINE),(YELLOW FIVE),(YELLOW SEVEN)]

### Round 8
- **Current Player**: Charlie
- **Current color: RED Current label: REVERSE**
- **Action**: Charlie draws a card RED ONE and plays it.
- **State after the round**
	- Player Bob has 5 cards: [(RED NINE),(BLUE ONE),(BLUE SEVEN),(YELLOW FIVE),(YELLOW REVERSE)]
	- Player Alice has 4 cards: [(GREEN SEVEN),(GREEN NINE),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Charlie has 7 cards: [(BLUE FIVE),(BLUE SKIP),(GREEN ONE),(GREEN TWO),(GREEN FIVE),(YELLOW ZERO),(YELLOW SKIP)]

### Round 9
- **Current Player**: Bob
- **Current color: RED Current label: ONE**
- **Action**: Bob plays RED NINE
- **State after the round**
	- Player Alice has 4 cards: [(GREEN SEVEN),(GREEN NINE),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Charlie has 7 cards: [(BLUE FIVE),(BLUE SKIP),(GREEN ONE),(GREEN TWO),(GREEN FIVE),(YELLOW ZERO),(YELLOW SKIP)]
	- Player Bob has 4 cards: [(BLUE ONE),(BLUE SEVEN),(YELLOW FIVE),(YELLOW REVERSE)]

### Round 10
- **Current Player**: Alice
- **Current color: RED Current label: NINE**
- **Action**: Alice plays GREEN NINE
- **State after the round**
	- Player Charlie has 7 cards: [(BLUE FIVE),(BLUE SKIP),(GREEN ONE),(GREEN TWO),(GREEN FIVE),(YELLOW ZERO),(YELLOW SKIP)]
	- Player Bob has 4 cards: [(BLUE ONE),(BLUE SEVEN),(YELLOW FIVE),(YELLOW REVERSE)]
	- Player Alice has 3 cards: [(GREEN SEVEN),(YELLOW FIVE),(YELLOW SEVEN)]

### Round 11
- **Current Player**: Charlie
- **Current color: GREEN Current label: NINE**
- **Action**: Charlie plays GREEN ONE
- **State after the round**
	- Player Bob has 4 cards: [(BLUE ONE),(BLUE SEVEN),(YELLOW FIVE),(YELLOW REVERSE)]
	- Player Alice has 3 cards: [(GREEN SEVEN),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Charlie has 6 cards: [(BLUE FIVE),(BLUE SKIP),(GREEN TWO),(GREEN FIVE),(YELLOW ZERO),(YELLOW SKIP)]

### Round 12
- **Current Player**: Bob
- **Current color: GREEN Current label: ONE**
- **Action**: Bob plays BLUE ONE
- **State after the round**
	- Player Alice has 3 cards: [(GREEN SEVEN),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Charlie has 6 cards: [(BLUE FIVE),(BLUE SKIP),(GREEN TWO),(GREEN FIVE),(YELLOW ZERO),(YELLOW SKIP)]
	- Player Bob has 3 cards: [(BLUE SEVEN),(YELLOW FIVE),(YELLOW REVERSE)]

### Round 13
- **Current Player**: Alice
- **Current color: BLUE Current label: ONE**
- **Action**: Alice draws a card into their hand.
- **State after the round**
	- Player Charlie has 6 cards: [(BLUE FIVE),(BLUE SKIP),(GREEN TWO),(GREEN FIVE),(YELLOW ZERO),(YELLOW SKIP)]
	- Player Bob has 3 cards: [(BLUE SEVEN),(YELLOW FIVE),(YELLOW REVERSE)]
	- Player Alice has 4 cards: [(RED TWO),(GREEN SEVEN),(YELLOW FIVE),(YELLOW SEVEN)]

### Round 14
- **Current Player**: Charlie
- **Current color: BLUE Current label: ONE**
- **Action**: Charlie plays BLUE FIVE
- **State after the round**
	- Player Bob has 3 cards: [(BLUE SEVEN),(YELLOW FIVE),(YELLOW REVERSE)]
	- Player Alice has 4 cards: [(RED TWO),(GREEN SEVEN),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Charlie has 5 cards: [(BLUE SKIP),(GREEN TWO),(GREEN FIVE),(YELLOW ZERO),(YELLOW SKIP)]

### Round 15
- **Current Player**: Bob
- **Current color: BLUE Current label: FIVE**
- **Action**: Bob plays BLUE SEVEN
- **State after the round**
	- Player Alice has 4 cards: [(RED TWO),(GREEN SEVEN),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Charlie has 5 cards: [(BLUE SKIP),(GREEN TWO),(GREEN FIVE),(YELLOW ZERO),(YELLOW SKIP)]
	- Player Bob has 2 cards: [(YELLOW FIVE),(YELLOW REVERSE)]

### Round 16
- **Current Player**: Alice
- **Current color: BLUE Current label: SEVEN**
- **Action**: Alice plays GREEN SEVEN
- **State after the round**
	- Player Charlie has 5 cards: [(BLUE SKIP),(GREEN TWO),(GREEN FIVE),(YELLOW ZERO),(YELLOW SKIP)]
	- Player Bob has 2 cards: [(YELLOW FIVE),(YELLOW REVERSE)]
	- Player Alice has 3 cards: [(RED TWO),(YELLOW FIVE),(YELLOW SEVEN)]

### Round 17
- **Current Player**: Charlie
- **Current color: GREEN Current label: SEVEN**
- **Action**: Charlie plays GREEN TWO
- **State after the round**
	- Player Bob has 2 cards: [(YELLOW FIVE),(YELLOW REVERSE)]
	- Player Alice has 3 cards: [(RED TWO),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Charlie has 4 cards: [(BLUE SKIP),(GREEN FIVE),(YELLOW ZERO),(YELLOW SKIP)]

### Round 18
- **Current Player**: Bob
- **Current color: GREEN Current label: TWO**
- **Action**: Bob draws a card into their hand.
- **State after the round**
	- Player Alice has 3 cards: [(RED TWO),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Charlie has 4 cards: [(BLUE SKIP),(GREEN FIVE),(YELLOW ZERO),(YELLOW SKIP)]
	- Player Bob has 3 cards: [(YELLOW FIVE),(YELLOW SIX),(YELLOW REVERSE)]

### Round 19
- **Current Player**: Alice
- **Current color: GREEN Current label: TWO**
- **Action**: Alice plays RED TWO
- **State after the round**
	- Player Charlie has 4 cards: [(BLUE SKIP),(GREEN FIVE),(YELLOW ZERO),(YELLOW SKIP)]
	- Player Bob has 3 cards: [(YELLOW FIVE),(YELLOW SIX),(YELLOW REVERSE)]
	- Player Alice has 2 cards: [(YELLOW FIVE),(YELLOW SEVEN)]

### Round 20
- **Current Player**: Charlie
- **Current color: RED Current label: TWO**
- **Action**: Charlie draws a card into their hand.
- **State after the round**
	- Player Bob has 3 cards: [(YELLOW FIVE),(YELLOW SIX),(YELLOW REVERSE)]
	- Player Alice has 2 cards: [(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Charlie has 5 cards: [(BLUE SKIP),(BLUE DRAW_TWO),(GREEN FIVE),(YELLOW ZERO),(YELLOW SKIP)]

### Round 21
- **Current Player**: Bob
- **Current color: RED Current label: TWO**
- **Action**: Bob draws a card into their hand.
- **State after the round**
	- Player Alice has 2 cards: [(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Charlie has 5 cards: [(BLUE SKIP),(BLUE DRAW_TWO),(GREEN FIVE),(YELLOW ZERO),(YELLOW SKIP)]
	- Player Bob has 4 cards: [(BLUE EIGHT),(YELLOW FIVE),(YELLOW SIX),(YELLOW REVERSE)]

### Round 22
- **Current Player**: Alice
- **Current color: RED Current label: TWO**
- **Action**: Alice draws a card into their hand.
- **State after the round**
	- Player Charlie has 5 cards: [(BLUE SKIP),(BLUE DRAW_TWO),(GREEN FIVE),(YELLOW ZERO),(YELLOW SKIP)]
	- Player Bob has 4 cards: [(BLUE EIGHT),(YELLOW FIVE),(YELLOW SIX),(YELLOW REVERSE)]
	- Player Alice has 3 cards: [(YELLOW ZERO),(YELLOW FIVE),(YELLOW SEVEN)]

### Round 23
- **Current Player**: Charlie
- **Current color: RED Current label: TWO**
- **Action**: Charlie draws a card into their hand.
- **State after the round**
	- Player Bob has 4 cards: [(BLUE EIGHT),(YELLOW FIVE),(YELLOW SIX),(YELLOW REVERSE)]
	- Player Alice has 3 cards: [(YELLOW ZERO),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Charlie has 6 cards: [(BLUE SEVEN),(BLUE SKIP),(BLUE DRAW_TWO),(GREEN FIVE),(YELLOW ZERO),(YELLOW SKIP)]

### Round 24
- **Current Player**: Bob
- **Current color: RED Current label: TWO**
- **Action**: Bob draws a card into their hand.
- **State after the round**
	- Player Alice has 3 cards: [(YELLOW ZERO),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Charlie has 6 cards: [(BLUE SEVEN),(BLUE SKIP),(BLUE DRAW_TWO),(GREEN FIVE),(YELLOW ZERO),(YELLOW SKIP)]
	- Player Bob has 5 cards: [(BLUE EIGHT),(YELLOW FIVE),(YELLOW SIX),(YELLOW EIGHT),(YELLOW REVERSE)]

### Round 25
- **Current Player**: Alice
- **Current color: RED Current label: TWO**
- **Action**: Alice draws a card RED SIX and plays it.
- **State after the round**
	- Player Charlie has 6 cards: [(BLUE SEVEN),(BLUE SKIP),(BLUE DRAW_TWO),(GREEN FIVE),(YELLOW ZERO),(YELLOW SKIP)]
	- Player Bob has 5 cards: [(BLUE EIGHT),(YELLOW FIVE),(YELLOW SIX),(YELLOW EIGHT),(YELLOW REVERSE)]
	- Player Alice has 3 cards: [(YELLOW ZERO),(YELLOW FIVE),(YELLOW SEVEN)]

### Round 26
- **Current Player**: Charlie
- **Current color: RED Current label: SIX**
- **Action**: Charlie draws a card into their hand.
- **State after the round**
	- Player Bob has 5 cards: [(BLUE EIGHT),(YELLOW FIVE),(YELLOW SIX),(YELLOW EIGHT),(YELLOW REVERSE)]
	- Player Alice has 3 cards: [(YELLOW ZERO),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Charlie has 7 cards: [(BLUE SEVEN),(BLUE SKIP),(BLUE DRAW_TWO),(GREEN FIVE),(YELLOW ZERO),(YELLOW SKIP),(YELLOW DRAW_TWO)]

### Round 27
- **Current Player**: Bob
- **Current color: RED Current label: SIX**
- **Action**: Bob plays YELLOW SIX
- **State after the round**
	- Player Alice has 3 cards: [(YELLOW ZERO),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Charlie has 7 cards: [(BLUE SEVEN),(BLUE SKIP),(BLUE DRAW_TWO),(GREEN FIVE),(YELLOW ZERO),(YELLOW SKIP),(YELLOW DRAW_TWO)]
	- Player Bob has 4 cards: [(BLUE EIGHT),(YELLOW FIVE),(YELLOW EIGHT),(YELLOW REVERSE)]

### Round 28
- **Current Player**: Alice
- **Current color: YELLOW Current label: SIX**
- **Action**: Alice plays YELLOW ZERO
- **State after the round**
	- Player Charlie has 7 cards: [(BLUE SEVEN),(BLUE SKIP),(BLUE DRAW_TWO),(GREEN FIVE),(YELLOW ZERO),(YELLOW SKIP),(YELLOW DRAW_TWO)]
	- Player Bob has 4 cards: [(BLUE EIGHT),(YELLOW FIVE),(YELLOW EIGHT),(YELLOW REVERSE)]
	- Player Alice has 2 cards: [(YELLOW FIVE),(YELLOW SEVEN)]

### Round 29
- **Current Player**: Charlie
- **Current color: YELLOW Current label: ZERO**
- **Action**: Charlie plays YELLOW ZERO
- **State after the round**
	- Player Bob has 4 cards: [(BLUE EIGHT),(YELLOW FIVE),(YELLOW EIGHT),(YELLOW REVERSE)]
	- Player Alice has 2 cards: [(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Charlie has 6 cards: [(BLUE SEVEN),(BLUE SKIP),(BLUE DRAW_TWO),(GREEN FIVE),(YELLOW SKIP),(YELLOW DRAW_TWO)]

### Round 30
- **Current Player**: Bob
- **Current color: YELLOW Current label: ZERO**
- **Action**: Bob plays YELLOW FIVE
- **State after the round**
	- Player Alice has 2 cards: [(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Charlie has 6 cards: [(BLUE SEVEN),(BLUE SKIP),(BLUE DRAW_TWO),(GREEN FIVE),(YELLOW SKIP),(YELLOW DRAW_TWO)]
	- Player Bob has 3 cards: [(BLUE EIGHT),(YELLOW EIGHT),(YELLOW REVERSE)]

### Round 31
- **Current Player**: Alice
- **Current color: YELLOW Current label: FIVE**
- **Action**: Alice plays YELLOW FIVE
- **State after the round**
	- Player Charlie has 6 cards: [(BLUE SEVEN),(BLUE SKIP),(BLUE DRAW_TWO),(GREEN FIVE),(YELLOW SKIP),(YELLOW DRAW_TWO)]
	- Player Bob has 3 cards: [(BLUE EIGHT),(YELLOW EIGHT),(YELLOW REVERSE)]
	- Player Alice has 1 cards: [(YELLOW SEVEN)]

### Round 32
- **Current Player**: Charlie
- **Current color: YELLOW Current label: FIVE**
- **Action**: Charlie plays GREEN FIVE
- **State after the round**
	- Player Bob has 3 cards: [(BLUE EIGHT),(YELLOW EIGHT),(YELLOW REVERSE)]
	- Player Alice has 1 cards: [(YELLOW SEVEN)]
	- Player Charlie has 5 cards: [(BLUE SEVEN),(BLUE SKIP),(BLUE DRAW_TWO),(YELLOW SKIP),(YELLOW DRAW_TWO)]

### Round 33
- **Current Player**: Bob
- **Current color: GREEN Current label: FIVE**
- **Action**: Bob draws a card GREEN FIVE and plays it.
- **State after the round**
	- Player Alice has 1 cards: [(YELLOW SEVEN)]
	- Player Charlie has 5 cards: [(BLUE SEVEN),(BLUE SKIP),(BLUE DRAW_TWO),(YELLOW SKIP),(YELLOW DRAW_TWO)]
	- Player Bob has 3 cards: [(BLUE EIGHT),(YELLOW EIGHT),(YELLOW REVERSE)]

### Round 34
- **Current Player**: Alice
- **Current color: GREEN Current label: FIVE**
- **Action**: Alice draws a card GREEN ZERO and plays it.
- **State after the round**
	- Player Charlie has 5 cards: [(BLUE SEVEN),(BLUE SKIP),(BLUE DRAW_TWO),(YELLOW SKIP),(YELLOW DRAW_TWO)]
	- Player Bob has 3 cards: [(BLUE EIGHT),(YELLOW EIGHT),(YELLOW REVERSE)]
	- Player Alice has 1 cards: [(YELLOW SEVEN)]

### Round 35
- **Current Player**: Charlie
- **Current color: GREEN Current label: ZERO**
- **Action**: Charlie draws a card GREEN SKIP and plays it.
- **State after the round**
	- Player Alice has 1 cards: [(YELLOW SEVEN)]
	- Player Charlie has 5 cards: [(BLUE SEVEN),(BLUE SKIP),(BLUE DRAW_TWO),(YELLOW SKIP),(YELLOW DRAW_TWO)]
	- Player Bob has 3 cards: [(BLUE EIGHT),(YELLOW EIGHT),(YELLOW REVERSE)]

### Round 36
- **Current Player**: Alice
- **Current color: GREEN Current label: SKIP**
- **Action**: Alice draws a card GREEN TWO and plays it.
- **State after the round**
	- Player Charlie has 5 cards: [(BLUE SEVEN),(BLUE SKIP),(BLUE DRAW_TWO),(YELLOW SKIP),(YELLOW DRAW_TWO)]
	- Player Bob has 3 cards: [(BLUE EIGHT),(YELLOW EIGHT),(YELLOW REVERSE)]
	- Player Alice has 1 cards: [(YELLOW SEVEN)]

### Round 37
- **Current Player**: Charlie
- **Current color: GREEN Current label: TWO**
- **Action**: Charlie draws a card into their hand.
- **State after the round**
	- Player Bob has 3 cards: [(BLUE EIGHT),(YELLOW EIGHT),(YELLOW REVERSE)]
	- Player Alice has 1 cards: [(YELLOW SEVEN)]
	- Player Charlie has 6 cards: [(BLUE SEVEN),(BLUE SKIP),(BLUE DRAW_TWO),(YELLOW SEVEN),(YELLOW SKIP),(YELLOW DRAW_TWO)]

### Round 38
- **Current Player**: Bob
- **Current color: GREEN Current label: TWO**
- **Action**: Bob draws a card into their hand.
- **State after the round**
	- Player Alice has 1 cards: [(YELLOW SEVEN)]
	- Player Charlie has 6 cards: [(BLUE SEVEN),(BLUE SKIP),(BLUE DRAW_TWO),(YELLOW SEVEN),(YELLOW SKIP),(YELLOW DRAW_TWO)]
	- Player Bob has 4 cards: [(RED EIGHT),(BLUE EIGHT),(YELLOW EIGHT),(YELLOW REVERSE)]

### Round 39
- **Current Player**: Alice
- **Current color: GREEN Current label: TWO**
- **Action**: Alice draws a card GREEN REVERSE and plays it.
- **State after the round**
	- Player Bob has 4 cards: [(RED EIGHT),(BLUE EIGHT),(YELLOW EIGHT),(YELLOW REVERSE)]
	- Player Charlie has 6 cards: [(BLUE SEVEN),(BLUE SKIP),(BLUE DRAW_TWO),(YELLOW SEVEN),(YELLOW SKIP),(YELLOW DRAW_TWO)]
	- Player Alice has 1 cards: [(YELLOW SEVEN)]

### Round 40
- **Current Player**: Bob
- **Current color: GREEN Current label: REVERSE**
- **Action**: Bob plays YELLOW REVERSE
- **State after the round**
	- Player Alice has 1 cards: [(YELLOW SEVEN)]
	- Player Charlie has 6 cards: [(BLUE SEVEN),(BLUE SKIP),(BLUE DRAW_TWO),(YELLOW SEVEN),(YELLOW SKIP),(YELLOW DRAW_TWO)]
	- Player Bob has 3 cards: [(RED EIGHT),(BLUE EIGHT),(YELLOW EIGHT)]

### Round 41
- **Current Player**: Alice
- **Current color: YELLOW Current label: REVERSE**
- **Action**: Alice plays YELLOW SEVEN
## End of Game, winner: Alice
