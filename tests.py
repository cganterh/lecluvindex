"""Tests for lecluvindex module."""


from unittest import (
    main,
    TestCase,
)

from unittest.mock import MagicMock

from lecluvindex import start_uv_index


class TestStartUVIndexWithWrongArgumentOrder(TestCase):
    """Test the start_uv_index function with the arguments in wrong order."""

    def setUp(self):
        """Call start_uv_index with wrong argument order."""
        self.bot = MagicMock()
        self.update = MagicMock()
        self.job_queue = MagicMock()

        start_uv_index(
            self.bot, self.update, self.job_queue, ['santiago', '12', '00'])

    def test_feedback_message_is_send_after_wrong_argument_order_call(self):
        """Test msg is send if start_uv_index called with wrong arg order."""
        text = (
            'You seem to have entered a wrong integer number. Check '
            'that you are passing well formatted integers and that '
            'the parameters in the correct order (hour, minute, '
            'place).'
        )

        self.bot.send_message.assert_called_with(
            self.update.message.chat_id, text)


if __name__ == '__main__':
    main()
