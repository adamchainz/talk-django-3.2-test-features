import os
import signal

from django.test import SimpleTestCase


class FaulthandlerTests(SimpleTestCase):
    def test_segv(self):
        # Directly trigger the segmentation fault
        # signal, which normally occurs due to
        # unsafe memory access in C
        os.kill(os.getpid(), signal.SIGSEGV)
