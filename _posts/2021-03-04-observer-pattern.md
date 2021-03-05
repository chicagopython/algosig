---
title: "Design Pattern: Observer Pattern"
category:
link:
author:
gh_comments_issue_id:
tags:
  - Design Patterns
---

## Description

> The **observer pattern** defines a one to many dependency between objects so that when one object changes state, all of its dependencies are notified and updated automatically.

Watch the below video for an excellent explanation of this pattern in plain English (no code), or check out [Refactoring Guru: Observer in Python](https://refactoring.guru/design-patterns/observer/python/example).

<div style="text-align:center">
<iframe width="95%" height="315" src="https://www.youtube.com/embed/_BpmfnqjgzQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

In this challenge, you will be implementing this pattern for a `WeatherStation` and a number of `Displays`. This is the scenario presented in the second half of the above video.

```python
class WeatherStation:
  def __init__(self):
    self.displays = []
    self.temperature = None

  def add_display(self):  # incomplete args
    pass

  def notify(self):
    pass

  def set_temperature(self):  # incomplete args
    # Imagine that instead of the WeatherStation
    # measuring the temperature, the user provides
    # a temperature value to this method
    pass

  def get_temperature(self):
    pass


class Display:
  def __init__(self):  # incomplete args
    pass

  def update(self):
    pass
```

Your code should be used as follows:
```python
from time import sleep

w = WeatherStation()
w.add_display(Display(w))
w.add_display(Display(w))

temp_feed = [32, 32, 32, 35, 34, 38, 40, 35]

for t in temp_feed:
  w.set_temperature(t)
  sleep(1)
```

In the output we should see that 2 `Display` instances are reporting their new temperature each time the `WeatherStation` gets a new value:
```
Display temperature set to 32
Display temperature set to 32
Display temperature set to 35
Display temperature set to 35
Display temperature set to 34
Display temperature set to 34
Display temperature set to 38
Display temperature set to 38
Display temperature set to 40
Display temperature set to 40
Display temperature set to 35
Display temperature set to 35
```

## Solution

```python
# Submit your solution here
class WeatherStation:
  def __init__(self):
    self.displays = []
    self.temperature = None

  def add_display(self,display):  # incomplete args
    self.displays.append(display)

  def notify(self):
    for display in self.displays:
      display.update()

  def set_temperature(self, temp):  # incomplete args
    # Imagine that instead of the WeatherStation
    # measuring the temperature, the user provides
    # a temperature value to this method
    if self.temperature is None or self.temperature!=temp:
      self.temperature=temp
      self.notify()

  def get_temperature(self):
    return self.temperature


class Display:
  def __init__(self, station):  # incomplete args
    self.station=station

  def update(self):
    print('Display temperature set to ',self.station.get_temperature())
```
