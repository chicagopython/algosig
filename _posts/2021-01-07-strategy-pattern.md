---
title: "Design Pattern: Strategy Pattern"
category:
link:
author:
gh_comments_issue_id:
tags:
  - Design Patterns
---

## Description

> The **strategy pattern** defines a family of algorithms, encapsulates each one, and makes them interchangeable.
> Strategy lets the algorithm vary independently from the clients who use it.

In object-oriented programming (OOP), the strategy pattern is useful when objects cannot be cleanly represented through inheritance.

Take the following diagram, for example:

![Strategy Pattern UML]({{ '/assets/img/strategy-pattern-uml.svg' | relative_url }})

If we attempted to use inheritance alone, we would have to overwrite the `move()` and `call()` methods any time we wanted different behavior than the base `Animal` class provides. We would also have to duplicate code (like for `Dragon.move()` and `Bat.move()`, which are the same thing but different than the base `Animal.move()`).

To solve this, we can define a `MoveBehaviorInterface` (a "strategy") with a `move()` method, and then subclass this to define various types of movement (like `Swim.move()` or `Fly.move()`). Finally, we can pass this behavior in when we instantiate an animal, e.g. `bird = Animal(move_behavior=Fly())`.

Your task is to fill in the missing pieces in the below code (where you see comments):

```python
from abc import ABC, abstractmethod

class MoveBehaviorInterface(ABC):
  """This is an 'abstract' class. It CAN'T be instantiated."""
  @abstractmethod
  def move(self):
    pass

class Swim(MoveBehaviorInterface):
  """This is a 'concrete' class. It CAN be instantiated."""
  def move(self):
    return "splash splash"

# Create a Fly class that inherits from MoveBehaviorInterface.
# It should have a move() method that returns "flap flap"

# Create a new interface, CallBehaviorInterface.
# It should have a call() method

# Create a EchoLocate class that inherits from CallBehaviorInterface.
# It should have a call() method that returns "click click"

# Create a Roar class that inherits from CallBehaviorInterface.
# It should have a call() method that returns "RooAAarr!"

class Animal:
  def __init__(
    self,
    move_behavior: MoveBehaviorInterface,
    call_behavior: CallBehaviorInterface
  ):
    self.move_behavior = move_behavior
    # store the call_behavior as an instance variable

  def move(self):
    return self.move_behavior.move()

  # create a call() method that runs the call behavior
```

The completed code should be used like this:
```python
dolphin = Animal(move_behavior=Swim(), call_behavior=EchoLocate())

bat = Animal(move_behavior=Fly(), call_behavior=EchoLocate())

dragon = Animal(move_behavior=Fly(), call_behavior=Roar())

assert dolphin.move() == "splash splash"
assert dolphin.call() == "click click"
assert bat.move() == "flap flap"
assert bat.call() == "click click"
assert dragon.move() == "flap flap"
assert dragon.call() == "RooAAarr!"
```

#### Further Reading
* [Christopher Okhravi: Strategy Pattern – Design Patterns](https://www.youtube.com/watch?v=v9ejT8FO-7I)
* [Refactoring Guru: Strategy in Python](https://refactoring.guru/design-patterns/strategy/python/example)


## Solution

```python
from abc import ABC, abstractmethod

class MoveBehaviorInterface(ABC):
  """This is an 'abstract' class. It CAN'T be instantiated."""
  @abstractmethod
  def move(self):
    pass

class CallBehaviorInterface(ABC):
  """This is an 'abstract' class. It CAN'T be instantiated."""
  @abstractmethod
  def call(self):
    pass

class Swim(MoveBehaviorInterface):
  """This is a 'concrete' class. It CAN be instantiated."""
  def move(self):
    return "splash splash"

class Fly(MoveBehaviorInterface):
  def move(self):
    return "flap flap"

class EchoLocate(CallBehaviorInterface):
  def call(self):
    return "click click"

class Roar(CallBehaviorInterface):
  def call(self):
    return "RooAAarr!"

class Animal:
  def __init__(
    self,
    move_behavior: MoveBehaviorInterface,
    call_behavior: CallBehaviorInterface
  ):
    self.move_behavior = move_behavior
    self.call_behavior = call_behavior

  def move(self):
    return self.move_behavior.move()

  def call(self):
    return self.call_behavior.call()
```
