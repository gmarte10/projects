import unittest
import app_time_tracking as att

class TestGetWindowInfo(unittest.TestCase):
    def test1(self):
        tracking = att.AppTimeTracking()
        window_info = tracking.get_window_info("test_log2.txt")

        test_log2 = [
            ["youtube — mozilla firefox",
            "google news - chromium",
            "weather - google search - opera",
            "new tab - chromium",
            "subscriptions - youtube — mozilla firefox"],
            [12, 1509, 63, 21, 2145]
        ]
        self.assertEqual(window_info, test_log2)

class TestGetAppWithTime(unittest.TestCase):
    def test1(self):
        tracking = att.AppTimeTracking()
        names = ["firefox", "chromium", "opera"]
        window_info = tracking.get_window_info("test_log2.txt")
        app_times = tracking.get_app_with_time(names, window_info)

        test_app = {
            "firefox":2157,
            "chromium":1530,
            "opera":63
        }
        self.assertEqual(app_times, test_app)

if __name__ == "__main__":
    unittest.main()
