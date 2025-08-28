from zeitgeist import schwurbel
def test_kein_crash(): assert isinstance(schwurbel(), str)
def test_format(): assert "–" in schwurbel()
def test_coverage(): assert schwurbel() in schwurbel.__globals__["ZITATE"]
