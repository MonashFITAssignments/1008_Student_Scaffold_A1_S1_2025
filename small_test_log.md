### State at the beginning
- Top card in discard pile: GREEN TWO
- Player Alice has 2 cards: [(RED ZERO),(YELLOW FIVE)]
- Player Bob has 2 cards: [(BLUE FIVE),(YELLOW REVERSE)]
- Player Charlie has 2 cards: [(RED REVERSE),(BLUE SKIP)]
- Player David has 2 cards: [(RED NINE),(GREEN NINE)]
### Round 1
- **Current Player**: Alice
- **Current color: GREEN Current label: TWO**
- **Action**: Alice draws a card into their hand.
- **State**
	- Player Bob has 2 cards: [(BLUE FIVE),(YELLOW REVERSE)]
	- Player Charlie has 2 cards: [(RED REVERSE),(BLUE SKIP)]
	- Player David has 2 cards: [(RED NINE),(GREEN NINE)]
	- Player Alice has 3 cards: [(RED ZERO),(YELLOW FIVE),(YELLOW SEVEN)]

### Round 2
- **Current Player**: Bob
- **Current color: GREEN Current label: TWO**
- **Action**: Bob draws a card into their hand.
- **State**
	- Player Charlie has 2 cards: [(RED REVERSE),(BLUE SKIP)]
	- Player David has 2 cards: [(RED NINE),(GREEN NINE)]
	- Player Alice has 3 cards: [(RED ZERO),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Bob has 3 cards: [(BLUE ONE),(BLUE FIVE),(YELLOW REVERSE)]

### Round 3
- **Current Player**: Charlie
- **Current color: GREEN Current label: TWO**
- **Action**: Charlie draws a card into their hand.
- **State**
	- Player David has 2 cards: [(RED NINE),(GREEN NINE)]
	- Player Alice has 3 cards: [(RED ZERO),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Bob has 3 cards: [(BLUE ONE),(BLUE FIVE),(YELLOW REVERSE)]
	- Player Charlie has 3 cards: [(RED REVERSE),(BLUE SKIP),(YELLOW ZERO)]

### Round 4
- **Current Player**: David
- **Current color: GREEN Current label: TWO**
- **Action**: David plays GREEN NINE
- **State**
	- Player Alice has 3 cards: [(RED ZERO),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Bob has 3 cards: [(BLUE ONE),(BLUE FIVE),(YELLOW REVERSE)]
	- Player Charlie has 3 cards: [(RED REVERSE),(BLUE SKIP),(YELLOW ZERO)]
	- Player David has 1 cards: [(RED NINE)]

### Round 5
- **Current Player**: Alice
- **Current color: GREEN Current label: NINE**
- **Action**: Alice draws a card GREEN SEVEN and plays it.
- **State**
	- Player Bob has 3 cards: [(BLUE ONE),(BLUE FIVE),(YELLOW REVERSE)]
	- Player Charlie has 3 cards: [(RED REVERSE),(BLUE SKIP),(YELLOW ZERO)]
	- Player David has 1 cards: [(RED NINE)]
	- Player Alice has 3 cards: [(RED ZERO),(YELLOW FIVE),(YELLOW SEVEN)]

### Round 6
- **Current Player**: Bob
- **Current color: GREEN Current label: SEVEN**
- **Action**: Bob draws a card RED SEVEN and plays it.
- **State**
	- Player Charlie has 3 cards: [(RED REVERSE),(BLUE SKIP),(YELLOW ZERO)]
	- Player David has 1 cards: [(RED NINE)]
	- Player Alice has 3 cards: [(RED ZERO),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Bob has 3 cards: [(BLUE ONE),(BLUE FIVE),(YELLOW REVERSE)]

### Round 7
- **Current Player**: Charlie
- **Current color: RED Current label: SEVEN**
- **Action**: Charlie plays RED REVERSE
- **State**
	- Player Bob has 3 cards: [(BLUE ONE),(BLUE FIVE),(YELLOW REVERSE)]
	- Player Alice has 3 cards: [(RED ZERO),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player David has 1 cards: [(RED NINE)]
	- Player Charlie has 2 cards: [(BLUE SKIP),(YELLOW ZERO)]

### Round 8
- **Current Player**: Bob
- **Current color: RED Current label: REVERSE**
- **Action**: Bob plays YELLOW REVERSE
- **State**
	- Player Charlie has 2 cards: [(BLUE SKIP),(YELLOW ZERO)]
	- Player David has 1 cards: [(RED NINE)]
	- Player Alice has 3 cards: [(RED ZERO),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Bob has 2 cards: [(BLUE ONE),(BLUE FIVE)]

### Round 9
- **Current Player**: Charlie
- **Current color: YELLOW Current label: REVERSE**
- **Action**: Charlie plays YELLOW ZERO
- **State**
	- Player David has 1 cards: [(RED NINE)]
	- Player Alice has 3 cards: [(RED ZERO),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Bob has 2 cards: [(BLUE ONE),(BLUE FIVE)]
	- Player Charlie has 1 cards: [(BLUE SKIP)]

### Round 10
- **Current Player**: David
- **Current color: YELLOW Current label: ZERO**
- **Action**: David draws a card YELLOW SKIP and plays it.
- **State**
	- Player Bob has 2 cards: [(BLUE ONE),(BLUE FIVE)]
	- Player Charlie has 1 cards: [(BLUE SKIP)]
	- Player David has 1 cards: [(RED NINE)]
	- Player Alice has 3 cards: [(RED ZERO),(YELLOW FIVE),(YELLOW SEVEN)]

### Round 11
- **Current Player**: Bob
- **Current color: YELLOW Current label: SKIP**
- **Action**: Bob draws a card into their hand.
- **State**
	- Player Charlie has 1 cards: [(BLUE SKIP)]
	- Player David has 1 cards: [(RED NINE)]
	- Player Alice has 3 cards: [(RED ZERO),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Bob has 3 cards: [(BLUE ONE),(BLUE FIVE),(GREEN FOUR)]

### Round 12
- **Current Player**: Charlie
- **Current color: YELLOW Current label: SKIP**
- **Action**: Charlie plays BLUE SKIP
## End of Game, winner: Charlie
