import pr4

def test1_get_digits():
    assert pr4.get_digits('555') == '555'

def test2_get_digits():
    assert pr4.get_digits('asa555') == '555'

def test1_change_num():
    assert pr4.change_num('+79000000000') == '+1(900)000-00-00'
    assert pr4.change_num('79000000000') == '+1(900)000-00-00'
    assert pr4.change_num('+7(900) 000-00-00') == '+1(900)000-00-00'
    assert pr4.change_num('+900\n0000000') == '+1(900)000-00-00'
    assert pr4.change_num('+7(900)) 000-00-00') == '+1(900)000-00-00'

def test2_change_num():
    assert pr4.change_num('+900 аыфаы\n0000000') == '+900 аыфаы\n0000000'
    assert pr4.change_num('+7900 000 00фф 00') == '+7900 000 00фф 00'
    assert pr4.change_num('-7900000:0000') == '-7900000:0000'

    