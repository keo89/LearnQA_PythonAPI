phrase = input("Set a phrase: ")

class TestExample:
    def test_check_length(self):
        assert len(phrase) < 15, f"Phrase is longer than 15"
