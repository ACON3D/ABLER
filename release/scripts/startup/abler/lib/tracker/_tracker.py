from abc import *
import enum


class EventKind(enum.Enum):
    login = "Login"
    login_fail = "Login Fail"
    login_auto = "Login Auto"
    render_quick = "Render Quick"
    import_blend = "Import *.blend"


class Tracker(metaclass=ABCMeta):
    def __init__(self):
        self._agreed = True

    @abstractmethod
    def _enqueue_event(self, event_name: str):
        """
        Enqueue a user event to be tracked.

        Implementations must be asynchronous.
        """
        pass

    @abstractmethod
    def _enqueue_email_update(self, email: str):
        """
        Enqueue update of user email.

        Implementations must be asynchronous.
        """
        pass

    def _track(self, event_name: str) -> bool:
        if not self._agreed:
            return False

        try:
            self._enqueue_event(event_name)
            print(f"TRACKING: {event_name}")
        except Exception as e:
            print(e)
            return False
        else:
            return True

    def login(self, email: str):
        if self._track(EventKind.login.value):
            self._enqueue_email_update(email)

    def login_fail(self):
        self._track(EventKind.login_fail.value)

    def login_auto(self):
        self._track(EventKind.login_auto.value)

    def render_quick(self):
        self._track(EventKind.render_quick.value)

    def import_blend(self):
        self._track(EventKind.import_blend.value)


class DummyTracker(Tracker):
    def __init__(self):
        super().__init__()
        self._agreed = False

    def _enqueue_event(self, event_name: str):
        pass

    def _enqueue_email_update(self, email: str):
        pass


class AggregateTracker(Tracker):
    def __init__(self, *trackers: Tracker):
        super().__init__()
        self.trackers = trackers

    def _enqueue_event(self, event_name: str):
        for t in self.trackers:
            t._enqueue_event(event_name)

    def _enqueue_email_update(self, email: str):
        for t in self.trackers:
            t._enqueue_email_update(email)
