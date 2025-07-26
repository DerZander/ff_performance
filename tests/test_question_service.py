from unittest import TestCase

from services.question_service import get_question_by_id


class Test(TestCase):
    def test_get_question_by_id(self):
        self.assertRaises(FileNotFoundError, lambda: get_question_by_id(2, 2025))
        # self.fail()

    def test_get_all_questions(self):
        from services.question_service import get_all_questions
        questions = get_all_questions(2025)
        self.assertIsInstance(questions, list)
        self.assertGreater(len(questions), 0)
