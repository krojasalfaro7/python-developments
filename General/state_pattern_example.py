from __future__ import annotations
from abc import ABC, abstractmethod

# the context class contains a _state that references the concrete state and setState method to change between states.
class Context:

    _state = None

    def __init__(self, state: State) -> None:
        self.setState(state)

    def setState(self, state: State):

        print(f"Context: Transitioning to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def doSomething(self):
        self._state.doSomething()

class State(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def doSomething(self) -> None:
        pass


class ConcreteStateA(State):
    def doSomething(self) -> None:
        print("The context is in the state of ConcreteStateA.")
        print("ConcreteStateA now changes the state of the context.")
        self.context.setState(ConcreteStateB())


class ConcreteStateB(State):
    def doSomething(self) -> None:
        print("The context is in the state of ConcreteStateB.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.setState(ConcreteStateA())

# sample application
app = Context(ConcreteStateA())
app.doSomething()    # this method is executed as in state 1
app.doSomething()    # this method is executed as in state 2
